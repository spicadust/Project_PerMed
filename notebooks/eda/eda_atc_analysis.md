# Analysis on ATC Code

## ATC Code Distributions

The information on the number of unique ATC codes associated with each drug is stored in the file `atc_counts.tsv`. It includes columns for `drug_concept_id`, the corresponding `drug_concept_name`, and the count of distinct ATC codes (`atc_count`) linked to each drug. The dataset is sorted by `atc_count` in ascending order.
The figure below shows the distribution of ATC Codes per drug.
<div align="center">
<img src="../../figures/atc_count.png" alt="atc_count" width="600"/>
<p><b>Figure 3</b></p>
</div>

## Drug Classifications

### First Classification

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

### Second Classification

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
