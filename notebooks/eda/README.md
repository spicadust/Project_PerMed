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

The tables below provide information on a subset of the drugs missing these properties, as displaying all drugs would be impractical due to the large number of entries (e.g., 682 drugs are missing an ATC code).
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
  2. The drug name refers to a general substance (e.g., "Senna Leaves"), and the active ingredient is not explicitly known or recorded.

- **Missing ChEBI Code**:
  1. Some drugs missing a ChEBI code actually have one, but it was not recorded due to dataset errors.
  2. The drug name refers to a general substance without a clear active ingredient.

- **Missing ATC Code**:
  1. Certain drugs without an ATC code do have one, but it was omitted due to dataset inaccuracies (e.g., **Camphor**).
  2. The recorded substance is a general substance rather than an active ingredient (e.g., **coal tar**, **cod liver oil**).
  3. The active ingredient is known but not classified as a therapeutic drug, so it is excluded from the ATC system (e.g., **PPG-1-PEG-9 LAURYL GLYCOL ETHER**, a surfactant used in cosmetics; **Influenza A virus**, where the vaccine has an ATC code, but the virus itself does not).

- **Missing DrugBank Information**:
  The reasons for missing DrugBank information are similar to those for missing ATC codes, often due to the dataset's omission or the substance not fitting within the DrugBank classification system.

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

A bar plot and a pie plot illustrating the distribution of First Level ATC Codes are shown below. It can be seen that the drugs in the dataset are across all the 14 first ATC levels.
<div align="center">
<img src="../../figures/atc_level1_bar.png" alt="atc_level1_bar" width="600"/>
<p><b>Figure 4:</b> Distribution of ATC Codes by First Level (Bar Plot)</p>
</div>
<div align="center">
<img src="../../figures/atc_level1_pie.png" alt="atc_level1_pie" width="600"/>
<p><b>Figure 5:</b> Distribution of ATC Codes by First Level (Pie Plot)</p>
</div>

#### Second Classification
Pie plots illustrating the distribution of Second level ATC Codes for each First Level ATC Code are shown below.
<div align="center">
<img src="../../figures/atc_level2_A.png" alt="atc_level2_A" width="400"/>
<p><b>Figure 6 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_B.png" alt="atc_level2_B" width="400"/>
<p><b>Figure 7 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_C.png" alt="atc_level2_C" width="400"/>
<p><b>Figure 8 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_D.png" alt="atc_level2_D" width="400"/>
<p><b>Figure 9 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_G.png" alt="atc_level2_G" width="400"/>
<p><b>Figure 10 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_H.png" alt="atc_level2_H" width="400"/>
<p><b>Figure 11 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_J.png" alt="atc_level2_J" width="400"/>
<p><b>Figure 12 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_L.png" alt="atc_level2_L" width="400"/>
<p><b>Figure 13 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_M.png" alt="atc_level2_M" width="400"/>
<p><b>Figure 14 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_N.png" alt="atc_level2_N" width="400"/>
<p><b>Figure 15 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_P.png" alt="atc_level2_P" width="400"/>
<p><b>Figure 16 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_R.png" alt="atc_level2_R" width="400"/>
<p><b>Figure 17 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_S.png" alt="atc_level2_S" width="400"/>
<p><b>Figure 18 </b></p>
</div>
<div align="center">
<img src="../../figures/atc_level2_V.png" alt="atc_level2_V" width="400"/>
<p><b>Figure 19 </b></p>
</div>