# EDA Analysis Conclusions for UK Biobank Databases

## 1. Comparison Between `gp_scripts`, `omop_era`, and `omop_exposure`

### `gp_scripts` vs. `omop_era`
- Many `eid`s contain information in `omop_era` but not in `gp_scripts`. This is because:
  - **`gp_scripts` drug names are highly variable**, making it difficult to filter all prescriptions accurately.
  - **`omop_era` captures the drug at the ingredient level**, allowing more prescriptions to be included in the filtering process.
- Some `eid`s only contain information in `gp_scripts`, likely due to the **constant renewal of the `gp_scripts` database**.
- Many start dates in `omop_era` match the first issue date in `gp_scripts`. However:
  - Whit **`omop_era` we capture more prescriptions** after filtering, leading to discrepancies in total matches.
  - Therefore, a **perfect coincidence** is not observed.

### `gp_scripts` vs. `omop_exposure`
- Comparing these datasets reveals **higher coincidence** because `omop_exposure` also filters by drug name.
- Quantities and the number of exposures/issue dates align, showing that:
  - **`omop_exposure` is essentially a standardized format of `gp_scripts`.**
- However, **`omop_exposure` is less practical for comparing quantities** because it does not account for varying formats (e.g., ml, packs, tablets).

### Key Takeaway
- **`omop_era` is more practical to use** because:
  - It is standardized.
  - Filtering by ingredient makes it easier to capture all relevant prescriptions.

---

## 2. Opioids EDA  in `omop_era`

### Key Observations
- **Loperamide** is the drug taken by the most people.
- **Morphine** has the highest total exposure across the population.
- More than **half of the people taking Fentanyl have also taken Morphine.**
  - This makes the study of switching between these two drugs particularly interesting, as both are analgesics.

---

## 3. Morphine and Fentanyl Analysis in `omop_era`

### Key Conclusion
- **Longer treatment durations do not imply greater adherence.**
  - Total drug exposure can be lower due to **larger gaps between exposures.**
- To effectively study adherence, it is crucial to:
  - Account for **treatment duration**.
  - Include **exposure counts**.
  - Consider **gaps between exposures and between eras**.
- There is a lot of people that have only 1 exposure to the drug

---

## 4. Drug Switching Between Morphine and Fentanyl

### Key Metrics
- **Number of common `eid`s**: 977
- **Number of `eid`s only in morphine**: 6240
- **Number of `eid`s only in fentanyl**: 707
- **People switching from morphine to fentanyl**: 563
- **People switching from fentanyl to morphine**: 414
- **Total people who switched more than once**: 294

### Observations
- A significant number of individuals switch between the two drugs.
- This underscores the importance of analyzing the **patterns of switching** to understand treatment trajectories and outcomes.
- In the histograms we can see again that a lot of the people have 1 exposure to the drugs.
---
