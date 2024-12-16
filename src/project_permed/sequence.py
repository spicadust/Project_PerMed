import numpy as np
import pandas as pd
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import linkage, fcluster


def from_eid_df(eid_df: pd.DataFrame):
    # Sort by start date
    eid_df = eid_df.sort_values("drug_era_start_date").reset_index(drop=True)

    # Convert to numpy arrays for faster operations
    counts = eid_df["drug_exposure_count"].to_numpy()
    codes = eid_df["atc_code_num"].to_numpy()

    # Calculate gaps
    next_starts = eid_df["drug_era_start_date"].shift(-1)
    gaps = (
        next_starts - eid_df["drug_era_end_date"] > pd.Timedelta(days=30)
    ).to_numpy()

    # Pre-calculate total sequence length
    sequence = []
    total_length = counts.sum() + gaps.sum()
    sequence = np.empty(int(total_length), dtype=int)

    # Fill sequence
    pos = 0
    for i, (count, code, needs_gap) in enumerate(zip(counts, codes, gaps)):
        sequence[pos : pos + count] = code
        pos += count
        if i < len(eid_df) - 1 and needs_gap:
            sequence[pos] = 0
            pos += 1

    return sequence[:pos].tolist()


def similarity_score(seq1: list, seq2: list) -> float:
    """
    Calculate similarity score between two sequences based on drug preferences in treatment periods.

    Args:
        seq1: First sequence of numbers (treatment periods separated by 0)
        seq2: Second sequence of numbers (treatment periods separated by 0)

    Returns:
        float: Normalized similarity score
    """
    # Split sequences into treatment periods
    periods1 = [period for period in "".join(map(str, seq1)).split("0") if period]
    periods2 = [period for period in "".join(map(str, seq2)).split("0") if period]

    # Convert periods to preference orders (removing duplicates, keeping last occurrence)
    def get_preferences(period):
        # Convert string of numbers back to ints and remove duplicates keeping last occurrence
        nums = [int(x) for x in period]
        seen = set()
        preferences = []
        for num in reversed(nums):
            if num not in seen:
                preferences.append(num)
                seen.add(num)
        return list(reversed(preferences))  # reverse back to get correct order

    pref_orders1 = [get_preferences(period) for period in periods1]
    pref_orders2 = [get_preferences(period) for period in periods2]

    raw_score = 0
    # Compare each pair of treatment periods
    for prefs1 in pref_orders1:
        for prefs2 in pref_orders2:
            # Find common drugs between the two preference lists
            common_drugs = set(prefs1) & set(prefs2)

            # award +3 points if the last drug is the same
            if prefs1[0] == prefs2[0]:
                raw_score += 1

            # Compare positions for each pair of common drugs
            for drug_i in common_drugs:
                for drug_j in common_drugs:
                    if drug_i != drug_j:
                        idx_i1 = prefs1.index(drug_i)
                        idx_j1 = prefs1.index(drug_j)
                        idx_i2 = prefs2.index(drug_i)
                        idx_j2 = prefs2.index(drug_j)

                        # If the relative ordering is the same in both preferences
                        if (idx_i1 < idx_j1) == (idx_i2 < idx_j2):
                            raw_score += 1

    # Normalize score using geometric mean of period counts
    n1, n2 = len(periods1), len(periods2)
    if n1 == 0 or n2 == 0:
        return 0.0

    normalized_score = raw_score / (n1 * n2) ** 0.5

    return normalized_score


def create_distance_matrix(sequences: list) -> np.ndarray:
    """
    Create a distance matrix using similarity scores between all pairs of sequences.
    Converts similarity scores to distances for clustering.
    """
    n = len(sequences)
    dist_matrix = np.zeros((n, n))

    # Calculate similarities and find max in a single pass
    max_similarity = 0
    similarities = {}  # Store (i,j) -> similarity

    for i in range(n):
        for j in range(i + 1, n):
            sim = similarity_score(sequences[i], sequences[j])
            similarities[(i, j)] = sim
            max_similarity = max(max_similarity, sim)

    # Fill the distance matrix
    for (i, j), sim in similarities.items():
        distance = max_similarity - sim
        dist_matrix[i, j] = distance
        dist_matrix[j, i] = distance

    return dist_matrix


def cluster(sequences: list, n_clusters: int = 5):
    """
    Cluster sequences using hierarchical clustering based on similarity scores

    Args:
        sequences: List of sequences to cluster
        n_clusters: Number of clusters
    """
    # Create distance matrix
    dist_matrix = create_distance_matrix(sequences)

    # Convert to condensed form required by linkage
    condensed_dist = squareform(dist_matrix)

    # Perform hierarchical clustering
    linkage_matrix = linkage(
        condensed_dist, method="average"
    )  # you can try 'single', 'complete', 'ward' etc.

    # Create clusters
    clusters = fcluster(linkage_matrix, n_clusters, criterion="maxclust")

    return clusters, linkage_matrix
