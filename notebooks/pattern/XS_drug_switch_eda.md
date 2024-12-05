## basic info
for each drug era, its closest subsequent drug eras are found. \
each combination of (drug era A, its closest subsequent drug era B) is deemed as a drugswitch.

number of drug eras (in original dataset): 19,959,413 \
number of drug eras that have closest subsequent drug eras: 18,926,988 (94.82% of total) \
number of drug eras that have multiple closest subsequent drug eras: 8,694,698 (43.56% of total)

number of people in the original dataset: 281,690 \
number of people having had drug switches: 243,710

total number of drug switches: 37,254,676

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

## atc code
switch within same atc 3rd level code: 7,173,001 (19.25% of total switches). note that this can be less the the actual ones because not all drugs are mapped to atc codes. \
among them, 5,487,973 are within same drug (76.51% of same atc 3rd level code switches)

switch interval within same atc 3rd level code: \
no big difference from the switch interval of total switches.
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


switch within same atc 2nd level code: 8,941,387 (24.00% of total switches). note that this can be less the the actual ones because not all drugs are mapped to atc codes. \
among them, 6,487,973 are within same drug (61.38% of same atc 2nd level code switches)\
switch interval: no big difference from the switch interval of total switches either.

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
for each drug switch pattern, how many people have had the switch

average people count of switches: 48.07682804817732 \
average people count of switches with different drugs: 45.32904707337069 \
average people count of switches with same drugs: 1046.6995884773662