import pandas as pd
import numpy as np
from tqdm import tqdm
from project_permed.atc_utils import share_atc_level


def get_drug_switches(df: pd.DataFrame) -> pd.DataFrame:
    """
    Find the closest subsequent drug era B for each drug era A.
    Process one patient at a time to reduce memory usage.
    """
    # Ensure datetime format
    if df["drug_era_start_date"].dtype != "datetime64[ns]":
        df["drug_era_start_date"] = pd.to_datetime(
            df["drug_era_start_date"], format="%d/%m/%Y"
        )
    if df["drug_era_end_date"].dtype != "datetime64[ns]":
        df["drug_era_end_date"] = pd.to_datetime(
            df["drug_era_end_date"], format="%d/%m/%Y"
        )

    # Sort all data by eid and start date
    df_sorted = df.sort_values(["eid", "drug_era_start_date"]).reset_index(drop=True)

    # List to store results for each patient
    result_dfs = []

    # Process one patient at a time
    for _, patient_df in tqdm(df_sorted.groupby("eid")):
        if len(patient_df) < 2:  # Skip patients with single drug era
            continue

        # Create indices
        n_rows = len(patient_df)
        idx_A, idx_B = np.meshgrid(np.arange(n_rows), np.arange(n_rows))

        # Convert patient_df to a dictionary of numpy arrays for faster access
        patient_arrays = {col: patient_df[col].values for col in patient_df.columns}

        # Create pairs DataFrame more efficiently
        pairs = pd.DataFrame(
            {
                "eid": patient_arrays["eid"][idx_A.flatten()],
                "drug_era_id_A": patient_arrays["drug_era_id"][idx_A.flatten()],
                "drug_concept_id_A": patient_arrays["drug_concept_id"][idx_A.flatten()],
                "drug_era_start_date_A": patient_arrays["drug_era_start_date"][
                    idx_A.flatten()
                ],
                "drug_era_end_date_A": patient_arrays["drug_era_end_date"][
                    idx_A.flatten()
                ],
                "drug_exposure_count_A": patient_arrays["drug_exposure_count"][
                    idx_A.flatten()
                ],
                "gap_days_A": patient_arrays["gap_days"][idx_A.flatten()],
                "drug_era_id_B": patient_arrays["drug_era_id"][idx_B.flatten()],
                "drug_concept_id_B": patient_arrays["drug_concept_id"][idx_B.flatten()],
                "drug_era_start_date_B": patient_arrays["drug_era_start_date"][
                    idx_B.flatten()
                ],
                "drug_era_end_date_B": patient_arrays["drug_era_end_date"][
                    idx_B.flatten()
                ],
                "drug_exposure_count_B": patient_arrays["drug_exposure_count"][
                    idx_B.flatten()
                ],
                "gap_days_B": patient_arrays["gap_days"][idx_B.flatten()],
            }
        )

        # Calculate time differences
        pairs["switch_interval"] = (
            pairs["drug_era_start_date_B"] - pairs["drug_era_end_date_A"]
        )

        # Filter valid transitions
        pairs = pairs[pairs["switch_interval"] > pd.Timedelta(0)]

        if len(pairs) == 0:  # Skip if no valid transitions
            continue

        min_intervals = pairs.groupby("drug_era_id_A")["switch_interval"].min()
        pairs = pairs.merge(
            min_intervals.rename("min_interval"),
            left_on="drug_era_id_A",
            right_index=True,
        )
        pairs = pairs[pairs["switch_interval"] == pairs["min_interval"]]

        # Create result DataFrame for this patient
        patient_result = pd.DataFrame(
            {
                "eid": pairs["eid"],
                "A_drug_era_id": pairs["drug_era_id_A"],
                "A_drug_concept_id": pairs["drug_concept_id_A"],
                "A_drug_era_start_date": pairs["drug_era_start_date_A"],
                "A_drug_era_end_date": pairs["drug_era_end_date_A"],
                "A_drug_exposure_count": pairs["drug_exposure_count_A"],
                "A_gap_days": pairs["gap_days_A"],
                "B_drug_era_id": pairs["drug_era_id_B"],
                "B_drug_concept_id": pairs["drug_concept_id_B"],
                "B_drug_era_start_date": pairs["drug_era_start_date_B"],
                "B_drug_era_end_date": pairs["drug_era_end_date_B"],
                "B_drug_exposure_count": pairs["drug_exposure_count_B"],
                "B_gap_days": pairs["gap_days_B"],
                "switch_interval": pairs["switch_interval"],
            }
        )

        result_dfs.append(patient_result)

    # Combine all results at the end
    if result_dfs:
        return pd.concat(result_dfs, ignore_index=True)
    else:
        return pd.DataFrame()  # Return empty DataFrame if no results


def find_switches_within_atc_level(drug_switch_df, drug_dict, n):
    """
    Find drug switches where both drugs share ATC codes at level n
    Args:
        drug_switch_df: DataFrame with A_drug_concept_id and B_drug_concept_id columns
        drug_dict: dictionary mapping drug IDs to (atc_codes_tuple, drug_name)
        n: int, ATC level (1-5)
    Returns:
        DataFrame with only the rows where drugs share ATC codes at level n
    """
    if not 1 <= n <= 5:
        raise ValueError("ATC level must be between 1 and 5")

    mask = drug_switch_df.apply(
        lambda row: share_atc_level(
            row["A_drug_concept_id"], row["B_drug_concept_id"], n, drug_dict
        ),
        axis=1,
    )

    return drug_switch_df[mask]
