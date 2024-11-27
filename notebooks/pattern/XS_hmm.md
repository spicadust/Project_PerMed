#  HMM

First I filtered out the records with N06A drugs (Antidepressants), and then sampled 1000 people for analysis.

I fit a Hidden Markov Model (HMM) to model the drug use pattern. For each person, the drug use is modeled as a sequence of days, and each day has 1 emission (drug use on that day, identified by drug_concept_id; no drug use is also an emission). Hidden states are not pre-defined, and can be interpreted as the health states. 

**HMM Model Performance Results (the number of hidden states = 10)**
| Model Performance Metrics | Value |
|--------------------------|-------|
| Training Log-likelihood  | -281,695.90 |
| Testing Log-likelihood   | -77,256.04 |

It can be seen that the result is poor. Actually I have tried fitting the model with all drugs or changing the number of hidden states and the results are also poor. It seems that HMM is hard to fit the complex drug use pattern.