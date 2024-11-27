# Drug Switch Data Preparation by Xinlu Shi

## terminology

For better clarification, we define some terminology here:

We say drug era B is a **subsequent drug era** for drug era A if:
- drug era A and drug era B are for the same person, and
- drug_era_start_date of B > drug_era_end_date of A (i.e. B starts after A ends)

and we call |drug_era_start_date of B - drug_era_end_date of A| a **switch interval**.

We say drug era B is the **closest subsequent drug era** for drug era A if:
- among all the subsequent drug eras of A, B has the ealiest start date (i.e. B minimizes the switch interval) 

For one drug era, there could be multiple closest subsequent drug eras.

There could also be cases where a drug era has no subsequent drug eras. This happens when:
- the person has only one drug era, or
- all drug eras (for the same person) start before this drug era ends. (note that this does not necessarily mean that this drug era has the last start date or end date.)

## method

A function is defined to find all the closest subsequent drug eras for each drug era in the original dataset. 
It takes as input a dataframe consisting of drug eras and outputs two dataframes:
- a dataframe with all the switch combinations for all drug eras that have subsequent drug eras
- a dataframe with all the drug eras that have no subsequent drug eras 

For the drug eras that have multiple closest subsequent drug eras, all the closest subsequent drug eras are included in the output in different rows.

The sum of number of unique `drug_era_id`s in the two dataframes should equal the number of unique `drug_era_id`s in the original dataset. This can be used to check the validity of the function and ensure that all drug eras are handled.

This function can be further optimized to add more customized functionalities and options.


## multiple closest subsequent drug eras

number of drug eras in the original dataset: 19,959,413 \
number of drug eras that have multiple closest subsequent drug eras: 8,694,698 \
Therefore, 43.56% of drug eras have multiple closest subsequent drug eras.

For the 8,694,698 drug eras that have multiple closest subsequent drug eras, total number of switch combinations is 27,022,386, which means that these drug eras have in average 3.11 switch combinations.



### case study 1 

For drug era id: 438086668536:

| Drug Era ID | Drug Name | ATC Code | Start Date | End Date |
|-------------|------------|-----------|------------|-----------|
|438086668536 | naproxen | G02CC02,M01AE02,M02AA12 | 2011-03-18 | 2011-04-14 |

it has 3 closest subsequent drug eras (switch interval = 244 days):

| Drug Name | ATC Code | Start Date | End Date |
|-----------|-----------|------------|-----------|
| diazepam | N05BA01 | 2011-12-14 | 2011-12-19 |
| acetaminophen | N02BE01 | 2011-12-14 | 2012-01-12 |
| dihydrocodeine | N02AA08 | 2011-12-14 | 2012-01-12 |

It seems that diazepam, acetaminophen, and dihydrocodeine are used together to treat pain.

### case study 2

For drug era id: 893353273051:

| Drug Era ID   | Drug Name  | ATC Code | Start Date | End Date   |
|---------------|------------|----------|------------|------------|
| 893353273051  | fluoxetine | N06AB03  | 2004-06-15 | 2004-09-12 |

it has 6 closest subsequent drug eras (switch interval = 43 days):

| Drug Name | ATC Code | Start Date | End Date |
|-----------|----------|------------|-----------|
| fluoxetine | N06AB03 | 2004-10-25 | 2005-05-15 |
| gramicidin | R02AB30 | 2004-10-25 | 2004-11-23 |
| neomycin | A01AB08,A07AA01,B05CA09,D06AX04,J01GB05,R02AB01,S01AA03,S02AA07,S03AA01 | 2004-10-25 | 2004-11-23 |
| triamcinolone | A01AC01,C05AA12,D07AB09,D07XB02,H02AB08,R01AD11,R03BA06,S01BA05 | 2004-10-25 | 2004-11-23 |
| naratriptan | N02CC02 | 2004-10-25 | 2004-11-17 |
| nystatin | A07AA02,D01AA01,G01AA01 | 2004-10-25 | 2004-11-23 |

It seems that some drugs are relevant to fluoxetine while some are not.



