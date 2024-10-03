![Static Badge](https://img.shields.io/badge/Author-Xinlu%20Shi-blue)


# project-permed

## Setting up the workspace in VSCode

The project uses Rye for dependency management and Ruff for linting & formatting. Follow the steps below:
1. Install Rye. See https://rye.astral.sh/
2. Install Ruff Extension in VSCode
3. Run `rye sync` at root
4. Run `pre-commit install` at root

## Introduction

This project aims to advance personalized medicine by tailoring drug prescriptions based on individual genetic, molecular, pharmacological, and clinical data. Leveraging the extensive UK Biobank dataset, which includes prescription records and genomic data from 500,000 individuals, I will investigate patterns in medication use and treatment adherence, focusing specifically on their relationship to genetic factors. The scale and diversity of this dataset offer a unique opportunity to explore how genetic variability influences medication effectiveness and patient outcomes.

A key objective is to map individual treatment trajectories by tracking prescribed medications, medication adherence, and medication switches over time. This approach captures the complexity of real-world treatment scenarios, where patients may switch medications due to side effects, lack of efficacy, or other clinical factors. Understanding medication use patterns is crucial for identifying factors that influence treatment success and improving patient outcomes.

We will employ General Linear Models (GLMs) to model these medication use patterns. GLMs provide a robust statistical framework capable of analyzing relationships between multiple variables and accommodating different types of data distributions. By integrating genetic data into these models, we aim to identify significant genetic predictors of treatment switches and adherence, potentially revealing genetic markers associated with better or worse outcomes.

Managing and analyzing such a large-scale dataset presents significant challenges. To address these, we will utilize advanced data science methods for efficient data processing and analysis. Modern data visualization techniques will be employed to present our findings clearly, facilitating the interpretation of complex relationships and aiding in hypothesis generation.

By uncovering the connections between genetic factors and medication use patterns, we can contribute to the development of more effective, personalized treatment plans. This could lead to improved patient adherence, reduced adverse drug reactions, and better overall health outcomes. The insights gained may also inform future pharmacogenomic studies and support the integration of genetic testing into clinical practice, ultimately advancing healthcare toward more precise therapeutic interventions.

In summary, this work aims to bridge the gap between large-scale genetic data and practical clinical applications. By demonstrating how prescription and genetic data can be combined to inform treatment decisions, we hope to make contributions to personalized medicine, where treatments are tailored to the individual characteristics.