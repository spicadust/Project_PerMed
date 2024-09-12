# Exploration on the datasets

 ## Venn diagram and UpSet plot

 ### Handling of the datasets
 
 The dataset was processed for further plotting, and the results are summarized in the table below. It shows the intersections of drugs across four datasets: Ingredients, ATC, DrugBank, and ChEBI. Each row represents a unique combination of whether a drug is present (True) or absent (False) in these datasets, with the corresponding count shown in the rightmost column. The table highlights how many drugs are shared between the datasets and which combinations of presence and absence occur.
 <div align="center">
  <img src="../../figures/eda_datahandling.png" alt="Drug Intersections" width="400"/>
  <p><b>Table 1:</b> Drug Intersections</p>
</div>

 ### Venn diagram

 The Venn diagram shown below illustrates the overlap of drugs across the four datasets: Ingredients, ATC, DrugBank, and ChEBI. 
  <div align="center">
  <img src="../../figures/eda_venn.png" alt="Venn Diagram" width="500"/>
  <p><b>Figure 1 </b></p>
</div>

 ### Upset plot

 The UpSet plot shown below provides a detailed visualization of the intersections between the Ingredients, ATC, DrugBank, and ChEBI datasets. It displays the size of each intersection, offering a clearer insight into the distribution of shared and unique drugs across the datasets.
   <div align="center">
  <img src="../../figures/eda_upset.png" alt="UpSet Plot" width="500"/>
  <p><b>Figure 2 </b></p>
</div>



  ### Overview of the Missing Properties
  
  From the plots and summarized data, several key observations can be made. **ChEBI** and **Ingredients** are almost always present across the datasets. Only 4 drugs lack ingredient information, and just 10 drugs lack a ChEBI code. This is expected, as substances inherently have ingredients, and most drugs tend to have a corresponding ChEBI code due to their chemical nature. Among all missing properties, the absence of an **ATC code** is the most common.

The tables below provide information on a subset of the drugs missing these properties, as displaying all drugs would be impractical due to the large number of entries (e.g. 431 drugs are missing ATC Codes). For the full drug lists of missing properties, see `lacks_atc.csv`, `lacks_drugbank.csv`, `lacks_chebi.csv` and `lacks_ingredients.csv`.
<div align="center">
<img src="../../figures/eda_lacking.png" alt="Missing Ingredient" width="400"/>
<p><b>Table 2:</b> Missing Ingredient</p>
</div>
<div align="center">
<img src="../../figures/eda_lackchebi.png" alt="Missing ChEBI Code" width="400"/>
<p><b>Table 3:</b> Missing ChEBI Code</p>
</div>
<div align="center">
<img src="../../figures/eda_lackatc.png" alt="Missing ATC Code" width="400"/>
<p><b>Table 4:</b> Missing ATC Code</p>
</div>
<div align="center">
<img src="../../figures/eda_lackdrugbank.png" alt="Missing DrugBank" width="400"/>
<p><b>Table 5:</b> Missing DrugBank Code</p>
</div>

#### Possible Reasons for Missing Information:

- **Missing Ingredients**:
  1. The ingredient information is actually indicated in the drug name, but the dataset fails to capture it.
  2. The drug name refers to a general substance (e.g. **Senna Leaves**), and the active ingredient is not explicitly recorded.

- **Missing ChEBI Code**:
  1. Some drugs missing a ChEBI code actually have one, but it was not recorded due to dataset errors.
  2. The drug name refers to a general substance without a clear active ingredient (e.g. **Senna pod**).
  3. Some drugs do not fit within the ChEBI classification system (e.g. **Lactobacillus paracasei**, a species of probiotic bacteria)

- **Missing ATC Code**:
  1. Certain drugs without an ATC code do have one, but it was omitted due to dataset inaccuracies (e.g. **Camphor**).
  2. The recorded substance is a general substance rather than an active ingredient.
  3. The active ingredient is known but not classified as a therapeutic drug, so it is excluded from the ATC system (e.g. **PPG-1-PEG-9 LAURYL GLYCOL ETHER**, a surfactant used in cosmetics).

- **Missing DrugBank Information**:
  The reasons for missing DrugBank information are similar to those for missing ATC codes, often due to the dataset's omission or the substance not fitting within the DrugBank classification system.

  The 74 drugs that lack only DrugBank seem counterintuitive beacuse if a drug has an ATC Code, it is highly likely that it has DrugBank information. To figure this out, the 74 drugs missing only DrugBank are filtered out (see `lacks_only_drugbank.csv`). It turns out that these drugs are mostly in DrugBank but lack DrugBank information due to the dataset's omission. 

## Analysis on ATC Code

### ATC Code Distributions

The information on the number of unique ATC codes associated with each drug is stored in the file `atc_counts.tsv`. It includes columns for `drug_concept_id`, the corresponding `drug_concept_name`, and the count of distinct ATC codes (`atc_count`) linked to each drug. The dataset is sorted by `atc_count` in ascending order.
The figure below shows the distribution of ATC Codes per drug.
<div align="center">
<img src="../../figures/atc_count.png" alt="atc_count" width="600"/>
<p><b>Figure 3</b></p>
</div>

### Drug Classifications

#### First Classification

A bar plot and a pie chart illustrating the distribution of First Level ATC Codes are shown below. It can be seen that the drugs in the dataset are distributed across all 14 first-level ATC codes. The largest categories include 'A: Alimentary Tract and Metabolism' and 'N: Nervous System', which together make up a significant portion of the dataset, as shown by their high counts in the bar chart and larger slices in the pie chart (13.8% and 13.5%, respectively). Other notable categories include 'D: Dermatologicals' and 'C: Cardiovascular System', each contributing over 9% to the total distribution. Smaller categories, such as 'V: Various', 'H: Systemic Hormonal Preparations', and 'P: Antiparasitic Products', represent only a small fraction of the dataset, as indicated by their smaller pie slices and lower counts in the bar chart.

For reference to the ATC classification system and the full class names for the first level ATC codes, please refer to the official [ATC/DDD Index](https://atcddd.fhi.no/atc_ddd_index/). Below is a list of the first-level ATC codes used in this analysis:

- A: Alimentary Tract and Metabolism
- B: Blood and Blood Forming Organs
- C: Cardiovascular System
- D: Dermatologicals
- G: Genito Urinary System and Sex Hormones
- H: Systemic Hormonal Preparations, Excl. Sex Hormones
- J: Antiinfectives for Systemic Use
- L: Antineoplastic and Immunomodulating Agents
- M: Musculo-Skeletal System
- N: Nervous System
- P: Antiparasitic Products, Insecticides and Repellents
- R: Respiratory System
- S: Sensory Organs
- V: Various

<div align="center">
<img src="../../figures/atc_level1_bar.png" alt="atc_level1_bar" width="600"/>
<p><b>Figure 4</b></p>
</div>
<div align="center">
<img src="../../figures/atc_level1_pie.png" alt="atc_level1_pie" width="1000"/>
<p><b>Figure 5</b></p>
</div>

#### Second Classification

The table below presents the statistics on the presence of drugs in our dataset, categorized by second-level ATC codes. It highlights the total number of drugs, their presence, absence, and the corresponding percentage of presence for each ATC category.

The table shows that most ATC categories have complete or near-complete drug representation in the dataset, with many categories (e.g., Cardiovascular System, Dermatologicals) showing 100% presence. However, certain categories like "Alimentary Tract and Metabolism" and "Various" have lower representation, with the presence percentages dropping to 81.25% and 55.56%, respectively. This indicates potential gaps in coverage for these specific categories.
| **ATC Code** | **Category**                                                | **Number of Second-Level Codes** | **Presence** | **Absence** | **Presence Percentage**          |
|--------------|-------------------------------------------------------------|------------------|--------------|-------------|-----------------------------------|
| **A**        | Alimentary Tract and Metabolism                              | **16**           | **13**       | **3**       | <span style="color:red">**81.25%**</span>  |
| **B**        | Blood and Blood Forming Organs                               | **5**            | **4**        | **1**       | <span style="color:red">**80.00%**</span>  |
| **C**        | Cardiovascular System                                        | **9**            | **9**        | **0**       | <span style="color:blue">**100.00%**</span> |
| **D**        | Dermatologicals                                              | **11**           | **11**       | **0**       | <span style="color:blue">**100.00%**</span> |
| **G**        | Genito Urinary System and Sex Hormones                       | **4**            | **4**        | **0**       | <span style="color:blue">**100.00%**</span> |
| **H**        | Systemic Hormonal Preparations, Excl. Sex Hormones           | **5**            | **5**        | **0**       | <span style="color:blue">**100.00%**</span> |
| **J**        | Antiinfectives for Systemic Use                              | **6**            | **6**        | **0**       | <span style="color:blue">**100.00%**</span> |
| **L**        | Antineoplastic and Immunomodulating Agents                   | **4**            | **4**        | **0**       | <span style="color:blue">**100.00%**</span> |
| **M**        | Musculo-Skeletal System                                      | **6**            | **5**        | **1**       | <span style="color:red">**83.33%**</span>  |
| **N**        | Nervous System                                               | **7**            | **7**        | **0**       | <span style="color:blue">**100.00%**</span> |
| **P**        | Antiparasitic Products, Insecticides and Repellents          | **3**            | **3**        | **0**       | <span style="color:blue">**100.00%**</span> |
| **R**        | Respiratory System                                           | **6**            | **5**        | **1**       | <span style="color:red">**83.33%**</span>  |
| **S**        | Sensory Organs                                               | **3**            | **3**        | **0**       | <span style="color:blue">**100.00%**</span> |
| **V**        | Various                                                      | **9**            | **5**        | **4**       | <span style="color:red">**55.56%**</span>  |
| **SUM**      |                                                              | **94**           | **84**       | **10**      | <span style="color:red">**89.36%**</span>  |

<p align="center"><b>Table 6: Statistics on the presence of drugs categorized by second-level ATC codes</b></p>


Below are bar charts showing the distribution of second-level ATC codes for each first-level ATC category. These charts display the percentage of drugs present in our dataset, as well as the absence of drugs (represented by zero percentages). For pie charts illustrating the same distribution, refer to `figures/atc_level2_pie`.

<div align="center">
<img src="../../figures/atc_level2_A.png" alt="atc_level2_A" width="1000"/>
<p><b>Figure 6 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_B.png" alt="atc_level2_B" width="800"/>
<p><b>Figure 7 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_C.png" alt="atc_level2_C" width="800"/>
<p><b>Figure 8 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_D.png" alt="atc_level2_D" width="900"/>
<p><b>Figure 9 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_G.png" alt="atc_level2_G" width="800"/>
<p><b>Figure 10 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_H.png" alt="atc_level2_H" width="800"/>
<p><b>Figure 11 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_J.png" alt="atc_level2_J" width="800"/>
<p><b>Figure 12 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_L.png" alt="atc_level2_L" width="700"/>
<p><b>Figure 13 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_M.png" alt="atc_level2_M" width="800"/>
<p><b>Figure 14 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_N.png" alt="atc_level2_N" width="800"/>
<p><b>Figure 15 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_P.png" alt="atc_level2_P" width="800"/>
<p><b>Figure 16 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_R.png" alt="atc_level2_R" width="800"/>
<p><b>Figure 17 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_S.png" alt="atc_level2_S" width="800"/>
<p><b>Figure 18 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_V.png" alt="atc_level2_V" width="800"/>
<p><b>Figure 19 </b></p>
</div>
