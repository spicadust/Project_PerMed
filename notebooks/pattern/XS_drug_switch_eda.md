## basic info
for each drug era, its closest subsequent drug eras are found. \
each combination of (drug era A, its closest subsequent drug era B) is deemed as a drugswitch.

number of drug eras (in original dataset): 19,959,413 \
number of drug eras that have closest subsequent drug eras: 18,926,988 (94.82% of total) \
number of drug eras that have multiple closest subsequent drug eras: 8,694,698 (43.56% of total)

number of people in the original dataset: 281,690 \
number of people having had drug switches: 243,710

**total number of drug switches: 37,254,676** \
number of switches with same drug: 5,978,429 (16.05% of total) \
number of switches with different drugs: 31,276,247 (83.95% of total)

## switch interval
switch interval statistics: \
7.96% of the switches happens within 7 days, 27.44% happens within 1 month\
50% happens within 1.5 months, 75% happens within 2.5 months \
80.77% within 3 months, 96.49% happens within 1 year
| Statistic | Value |
|-----------|-------|
| count | 37,254,676 |
| mean | 85.46 |
| std | 194.23 |
| min | 1 |
| 25% | 27 |
| 50% | 43 |
| 75% | 73 |
| max | 9,660 |


some quantiles of switch interval:
| Quantile | Interval (days) |
|-----------|-------|
| 7.96% | 7 |
| 15.16% | 15 |
| 27.44% | 30 |
| 68.13% | 60 |
| 80.77% | 90 |
| 96.49% | 365 |

## atc code on total switches
**switch within same 3rd level atc code**: 7,173,001 (19.25% of total switches). only 1,685,028 among them are between **different drugs** (**4.52%** of total switches) \
note that this can be less the the actual ones because not all drugs are mapped to atc codes.

**switch within same 2nd level atc code**: 8,941,387 (24.00% of total switches). only 3,453,414 among them are between **different drugs** (**9.27%** of total switches) 

**switch within same 1st level atc code**: 13504325 (36.25% of total switches). 8016352 among them are between **different drugs** (**21.52%** of total switches) 


switch interval within same 3rd level atc code: \
no big difference from the switch interval of total switches. this is also the case for 2nd and 1st level atc code.
| Statistic | Value |
|-----------|-------|
| count | 7,173,001 |
| mean | 81.17 |
| std | 143.77 |
| min | 1 |
| 25% | 36 |
| 50% | 49 |
| 75% | 74 |
| max | 8,633 |

## switch frequency (by times)
for each drug switch pattern, how many times it occurs

drug switch pattern: identified by tuple: (A_drug_concept_id, B_drug_concept_id). \
total unique drug switch patterns: 442,781 \
among them, 1215 patterns are with same drug (0.27%), 441,566 patterns are with different drugs (99.73%)

statistics of switch count of total switches (by times): 
| Statistic | Value |
|-----------|-------|
| count | 442,781 |
| mean | 84.14 |
| std | 1,354.94 |
| min | 1 |
| 25% | 1 |
| 50% | 5 |
| 75% | 21 |
| max | 541,893 |

average times of total switches: 84.14 \
average times of switches with different drugs: 70.83 \
average times of switches with same drugs: 4920.52

## switch frequency (by people)
for each drug switch pattern, how many people have had the switch. I think this is probably more informative than the switch frequency by times.

average people count of switches: 48.07682804817732 \
average people count of switches with different drugs: 45.32904707337069 \
average people count of switches with same drugs: 1046.6995884773662

the switch patterns with top frequency mostly happen with some very popular drugs (among both switches with same drugs and different drugs), e.g. aspirin, acetaminophen, amoxicillin, etc. I think this is not very informative as people may take a common/popular drug immediately after another drug era by chance. \
I tried to filter the switches within certain switch interval (365/90/60/15/7 days etc.) but the most frequent switch patterns are still mostly with popular drugs.

the detailed results are saved in `/notebooks/pattern/output_switch`.

the top frequent switch patterns are still mostly with popular drugs so here I just report some case studies on some arbitrary meaningful atc code level or meaningful drugs. \
actually it seems that even within certain atc code level, the most frequent switches are still mostly with popular drugs in this category.



**case study 1**: top 5 frequent switch patterns with **same N06 drugs**:
| A_atc_codes | A_drug_concept_name | B_atc_codes | B_drug_concept_name | people_count | avg_switch_interval |
|-------------|-------------------|-------------|-------------------|--------------|-------------------|
| N06AA09 | amitriptyline | N06AA09 | amitriptyline | 15,261 | 54.28 |
| N06AB04 | citalopram | N06AB04 | citalopram | 8,507 | 59.68 |
| N06AB03 | fluoxetine | N06AB03 | fluoxetine | 6,797 | 72.94 |
| N06AA16 | dothiepin | N06AA16 | dothiepin | 3,780 | 57.90 |
| N06AB05 | paroxetine | N06AB05 | paroxetine | 2,829 | 67.15 |


**case study 2**: top 6 frequent switch patterns with **different N06 drugs**: \
(switch from a N06 drug to another N06 drug) 
| A_atc_codes | A_drug_concept_name | B_atc_codes | B_drug_concept_name | people_count | avg_switch_interval |
|-------------|---------------------|-------------|---------------------|--------------|---------------------|
| N06AA09     | amitriptyline       | N06AB04     | citalopram          | 1119         | 67.42               |
| N06AB04     | citalopram          | N06AA09     | amitriptyline       | 976          | 60.01               |
| N06AA09     | amitriptyline       | N06AB03     | fluoxetine          | 964          | 67.67               |
| N06AB03     | fluoxetine          | N06AA09     | amitriptyline       | 881          | 65.25               |
| N06AB03     | fluoxetine          | N06AB04     | citalopram          | 786          | 129.47              |
| N06AB04     | citalopram          | N06AB06     | sertraline          | 673          | 69.40               |


**case study 3**: top 11 frequent switch patterns that involve both **lorazepam(N05BA06)** and another `N` drug （self-switch included）:
| A_atc_codes | A_drug_concept_name | B_atc_codes | B_drug_concept_name | people_count | avg_switch_interval |
|-------------|---------------------|-------------|---------------------|--------------|---------------------|
| N05BA06     | lorazepam           | N05BA06     | lorazepam           | 291          | 74.20               |
| N02BE01     | acetaminophen       | N05BA06     | lorazepam           | 199          | 61.68               |
| N05BA06     | lorazepam           | N02BE01     | acetaminophen       | 183          | 62.82               |
| N05BA06     | lorazepam           | N02BA01     | aspirin             | 91           | 34.72               |
| N02BA01     | aspirin             | N05BA06     | lorazepam           | 90           | 40.69               |
| N05CF01     | zopiclone           | N05BA06     | lorazepam           | 84           | 39.44               |
| N05BA01     | diazepam            | N05BA06     | lorazepam           | 80           | 53.10               |
| N05BA06     | lorazepam           | N05BA01     | diazepam            | 76           | 64.40               |
| N05BA06     | lorazepam           | N06AB04     | citalopram          | 72           | 86.89               |
| N06AA09     | amitriptyline       | N05BA06     | lorazepam           | 67           | 56.32               |
| N05BA06     | lorazepam           | N05CF01     | zopiclone           | 67           | 63.41               |


**case study 4**: top 11 frequent switch patterns that involve both citalopram(N06AB04) and another `N` drug （self-switch included）:
| A_atc_codes | A_drug_concept_name | B_atc_codes | B_drug_concept_name | people_count | avg_switch_interval |
|-------------|---------------------|-------------|---------------------|--------------|---------------------|
| N06AB04     | citalopram          | N06AB04     | citalopram          | 8507         | 59.68               |
| N02BE01     | acetaminophen       | N06AB04     | citalopram          | 3144         | 77.01               |
| N06AB04     | citalopram          | N02BE01     | acetaminophen       | 2825         | 65.01               |
| N06AB04     | citalopram          | N02BA01     | aspirin             | 1531         | 43.89               |
| N02BA01     | aspirin             | N06AB04     | citalopram          | 1460         | 50.82               |
| N05BA01     | diazepam            | N06AB04     | citalopram          | 1123         | 89.81               |
| N06AA09     | amitriptyline       | N06AB04     | citalopram          | 1119         | 67.42               |
| N06AB04     | citalopram          | N06AA09     | amitriptyline       | 976          | 60.01               |
| N05CF01     | zopiclone           | N06AB04     | citalopram          | 942          | 80.28               |
| N06AB03     | fluoxetine          | N06AB04     | citalopram          | 786          | 129.47              |
| N06AB04     | citalopram          | N05BA01     | diazepam            | 706          | 82.60               |










## future work and questions

maybe filter out the most popular drugs to find more meaningful frequentdrug switch patterns.

I am not sure of the method of finding drug switches (definition for drug switch). Now I just deem (A, B) where B is the closest subsequent drug era of A as a drug switch. for A we only consider the closest subsequent ones to it; this method can lose some poteintial drug switches. \
maybe try another method of finding drug switches. e.g. drug eras that end with certain interval (e.g. 30, 90, 365 days) can be considered as a drug switch. this can include more potential drug switches but maybe also include more noise.
