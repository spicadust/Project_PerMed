 # Exploration on Drug Properties

 ## Handling of the datasets
 
 The dataset was processed for further plotting, and the results are summarized in the table below. It shows the intersections of drugs across four datasets: Ingredients, ATC, DrugBank, and ChEBI. Each row represents a unique combination of whether a drug is present (True) or absent (False) in these datasets, with the corresponding count shown in the rightmost column. The table highlights how many drugs are shared between the datasets and which combinations of presence and absence occur.
 <div align="center">
  <img src="../../figures/eda_drug_properties/eda_datahandling.png" alt="Drug Intersections" width="400"/>
  <p><b>Table 1:</b> Drug Intersections</p>
</div>

 ## Venn diagram

 The Venn diagram shown below illustrates the overlap of drugs across the four datasets: Ingredients, ATC, DrugBank, and ChEBI. 
  <div align="center">
  <img src="../../figures/eda_drug_properties/eda_venn.png" alt="Venn Diagram" width="500"/>
  <p><b>Figure 1 </b></p>
</div>

 ## Upset plot

 The UpSet plot shown below provides a detailed visualization of the intersections between the Ingredients, ATC, DrugBank, and ChEBI datasets. It displays the size of each intersection, offering a clearer insight into the distribution of shared and unique drugs across the datasets.
   <div align="center">
  <img src="../../figures/eda_drug_properties/eda_upset.png" alt="UpSet Plot" width="500"/>
  <p><b>Figure 2 </b></p>
</div>



  ## Overview of the Missing Properties
  
  From the plots and summarized data, several key observations can be made. **ChEBI** and **Ingredients** are almost always present across the datasets. Only 4 drugs lack ingredient information, and just 10 drugs lack a ChEBI code. This is expected, as substances inherently have ingredients, and most drugs tend to have a corresponding ChEBI code due to their chemical nature. Among all missing properties, the absence of an **ATC code** is the most common.

The tables below provide information on a subset of the drugs missing these properties, as displaying all drugs would be impractical due to the large number of entries (e.g. 431 drugs are missing ATC Codes). For the full drug lists of missing properties, see `lacks_atc.csv`, `lacks_drugbank.csv`, `lacks_chebi.csv` and `lacks_ingredients.csv`.
<div align="center">
<img src="../../figures/eda_drug_properties/eda_lacking.png" alt="Missing Ingredient" width="400"/>
<p><b>Table 2:</b> Missing Ingredient</p>
</div>
<div align="center">
<img src="../../figures/eda_drug_properties/eda_lackchebi.png" alt="Missing ChEBI Code" width="400"/>
<p><b>Table 3:</b> Missing ChEBI Code</p>
</div>
<div align="center">
<img src="../../figures/eda_drug_properties/eda_lackatc.png" alt="Missing ATC Code" width="400"/>
<p><b>Table 4:</b> Missing ATC Code</p>
</div>
<div align="center">
<img src="../../figures/eda_drug_properties/eda_lackdrugbank.png" alt="Missing DrugBank" width="400"/>
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

