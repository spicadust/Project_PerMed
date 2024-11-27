# Drug Switch Data Preparation

## terminology

For better clarity, we define some terminology here:

we say drug era B is a **subsequent drug era** for drug era A if:
- drug era A and drug era B are with the same person, and
- drug_era_end_date of B > drug_era_start_date of A (i.e. B starts after A ends)

we say drug era B is the **closest subsequent drug era** for drug era A if:
- among all the subsequent drug eras of A, B has the ealiest start date (i.e. |drug_era_start_date of B - drug_era_end_date of A| achieves its minimum) \
(theoretically, for one drug era, there could be multiple closest subsequent drug eras)


## data overview

total number of drug eras: 19,959,413
total number of people: 281,690

## multiple closest subsequent drug eras

43.56% of drug eras have multiple closest subsequent drug eras.
among them, total number of switch combinations: 27,022,386
these drug eras have in avg 3.11 switch combinations.


### case study 1 


drug era id: 438086668536
244 days

drug: 1115008 naproxen G02CC02,M01AE02,M02AA12
start date: 2011-03-18
end date: 2011-04-14

subsequent drug eras:
723013	diazepam	N05BA01
2011-12-14	2011-12-19

1125315	acetaminophen	N02BE01
2011-12-14	2012-01-12

1189596	dihydrocodeine	N02AA08
2011-12-14	2012-01-12

It seems like diazepam, acetaminophen, and dihydrocodeine are used together to treat pain.

### case study 2

drug era id: 893353273051
drug 755695	fluoxetine	N06AB03
start date: 2004-06-15
end date: 2004-09-12

subsequent drug eras: 

all start after 43 days

755695	fluoxetine	N06AB03
start date: 2004-10-25
end date: 2005-05-15

963742	gramicidin	R02AB30
start date: 2004-10-25
end date: 2004-11-23

915981	neomycin	A01AB08,A07AA01,B05CA09,D06AX04,J01GB05,R02AB01,S01AA03,S02AA07,S03AA01
start date: 2004-10-25
end date: 2004-11-23

903963	triamcinolone	A01AC01,C05AA12,D07AB09,D07XB02,H02AB08,R01AD11,R03BA06,S01BA05
start date: 2004-10-25
end date: 2004-11-23

1118117	naratriptan	N02CC02
start date: 2004-10-25
end date: 2004-11-17

922570	nystatin	A07AA02,D01AA01,G01AA01
start date: 2004-10-25
end date: 2004-11-23

it seems that some drugs are relevant to fluoxetine while some are not.



