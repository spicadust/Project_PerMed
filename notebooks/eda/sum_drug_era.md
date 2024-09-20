# Summary of Drug Era Data Structure

The following **drug_era** table is a component of the OMOP Common Data Model (CDM) designed to capture and summarize a patient's medication usage over time. Instead of listing every individual prescription or dispensing event, **drug_era** aggregates these events into continuous periods of drug exposure, making it easier to analyze treatment patterns and medication adherence.

<center>

| **Field Name**          | **Description**                                                                                                                |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `drug_era_id`           | A unique identifier for each drug era record.                                                                                  |
| `person_id`             | Links the drug era to a specific patient in the database.                                                                       |
| `drug_concept_id`       | Identifies the specific drug or substance (based on standardized vocabulary) that the patient was exposed to.                   |
| `drug_era_start_date`   | The date when the drug era begins, typically the date of the first recorded drug exposure.                                       |
| `drug_era_end_date`     | The date when the drug era ends, typically the last recorded drug exposure (accounting for gaps).                               |
| `drug_exposure_count`   | The total number of individual drug exposure events that were combined to form the drug era.                                     |
| `gap_days`              | The total number of days between consecutive drug exposures that were considered part of the same drug era (below the threshold).|

<p><b> Table: drug_era </b></p>
</center>

Additional information:
- A Drug Era represents a continuous period when a patient was exposed to a specific drug. It aggregates multiple exposures into a single era if gaps between them are below a predefined threshold. Drug eras facilitate longitudinal studies and analyses of drug adherence, usage trends, and treatment outcomes.
- The `gap_days` parameter allows for brief interruptions in drug use (e.g., delayed refills or stock shortages) without fragmenting treatment periods into separate eras.
- The Drug Concept refers to the specific drug or active ingredient being tracked, which is identified by a standardized concept ID in the OMOP Common Data Model.

For more details, refer to the [OMOP Drug Era documentation](https://www.ohdsi.org/web/wiki/doku.php?id=documentation:cdm:drug_era).


# Timeline Diagram

The following diagram illustrates how individual drug exposures are combined into a single drug era:
This timeline represents a more realistic scenario where a patient changes brands, experiences allowable gaps, and eventually starts a new drug era after a longer gap.

```
Time -->
|-------------|-------------|-------|-------------|--------|-----------|
| Exp 1 (30d) | Exp 2 (60d) | Gap 1 | Exp 3 (90d) | Gap 2  | New Era   |
|             |             | (5d)  |             | (45d)  |           |
|-------------|-------------|-------|-------------|--------|-----------|
|                     Drug Era 1                  | End of | Era 2     |
|                                                 | Era 1  | Starts    |
```
### Explanation

1. **Drug Exposure 1 (30 days)**: The patient begins taking the drug, marking the `drug_era_start_date` of **Drug Era 1**.

2. **Drug Exposure 2 (60 days)**: The patient continues the same drug (possibly a different brand). This is still part of **Drug Era 1** as it's the same `drug_concept_id`.

3. **Gap 1 (5 days)**: A 5-day gap occurs between exposures. This is within the allowable `gap_days` (e.g., 30 days), so **Drug Era 1** continues.

4. **Drug Exposure 3 (90 days)**: The patient resumes the drug, still part of **Drug Era 1**. The `drug_exposure_count` for this era is now 3.

5. **Gap 2 (45 days)**: After Exposure 3, there's a 45-day gap exceeding the `gap_days` limit. This ends **Drug Era 1**, setting the `drug_era_end_date`.

6. **New Drug Era**: If the patient resumes the drug after Gap 2, it starts a new `drug_era_id` with its own `drug_era_start_date`.

### Key Points

- **Drug Switching**: Switching between brands (Drug Exposure 1 and 2) without gaps is considered part of the same drug era.
- **Allowable Gaps**: Short gaps (like Gap 1) are tolerated and do not end the drug era.
- **Era Break**: A longer gap (like Gap 2) that exceeds the predefined maximum (e.g., 30 days) ends the current drug era and begins a new one if the drug is taken again.