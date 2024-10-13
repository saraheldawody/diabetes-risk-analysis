# Diabetes Risk Analysis Project

## Overview
This project aims to analyze factors contributing to diabetes risk by examining various health metrics such as Glucose, BMI, Age, and others. The analysis employs statistical methods and visualizations to identify key predictors of diabetes outcomes and provide actionable recommendations.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Data Description](#data-description)
- [Key Findings](#key-findings)
- [Visualizations](#visualizations)
- [Conclusions & Recommendations](#conclusions--recommendations)
- [Limitations & Future Work](#limitations--future-work)

## Installation
To run this project, ensure you have Python installed along with the following packages:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Usage
1. Clone the repository:

```bash
git clone <repository_url>
cd diabetes-risk-analysis
```

2. Open a Jupyter Notebook or a Python script and run the analysis.
3. Load the dataset and execute the analysis code to generate visualizations and insights.

## Data Description
The dataset consists of various health metrics for 768 individuals. The key features include:
- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
- **BloodPressure**: Diastolic blood pressure (mm Hg)
- **SkinThickness**: Triceps skin fold thickness (mm)
- **Insulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)^2)
- **DiabetesPedigreeFunction**: A function that scores the likelihood of diabetes based on family history
- **Age**: Age (years)
- **Outcome**: Class variable (0 or 1) indicating whether a patient is diabetic

## Key Findings
- Glucose is the strongest predictor of diabetes outcomes.
- Non-diabetic individuals exhibit lower glucose levels compared to diabetic individuals.
- A positive relationship exists between Insulin and Glucose.
- Age and BMI significantly influence diabetes risk.

## Visualizations
The project includes various visualizations, such as:
- Heatmaps showing correlation between features
- Violin plots to visualize glucose distribution by outcome
- KDE plots for glucose levels by diabetes outcome
- Scatter plots with trend lines illustrating relationships between glucose and insulin

## Conclusions & Recommendations
The analysis emphasizes the importance of regular glucose screening, promoting lifestyle changes, and enhancing insulin monitoring. Machine learning techniques are recommended for future investigations to better understand the non-linear relationships in the data.

## Limitations & Future Work
The analysis is limited by data constraints, generalizability, and the cross-sectional nature of the dataset. Future work should focus on incorporating a wider range of data and evaluating specific interventions aimed at reducing diabetes risk.

