# Diabetes Risk Analysis

An exploratory Python analysis of health measurements and a recorded binary diabetes outcome. The project demonstrates data-quality checks, missing-measurement handling, and visual exploration. **No predictive model or model performance result is included.** This is an educational portfolio project, not a clinical tool.

## What is implemented

- Inspect the bundled CSV and summarize feature distributions and class counts.
- Audit zero-coded missing measurements and apply outcome-independent median imputation for EDA.
- Explore correlations, pair plots, outcome counts, violin/KDE plots, and scatter plots.
- Flag IQR outliers without automatically capping observations.

## Repository guide

| Path | Purpose |
| --- | --- |
| `diabetes.csv` | Bundled input dataset; unchanged by analysis |
| `diabetes.ipynb` | Main analysis, with outputs cleared after preprocessing corrections |
| `scripts/check_analysis.py` | Dataset integrity checks and headless execution of every code cell |
| `requirements.txt` | Pinned direct analysis dependencies |
| `requirements-notebook.txt` | Optional interactive notebook tooling |
| `docs/REVIEW.md` | Review findings, remaining gaps, and evaluation acceptance criteria |

## Run locally

Use Python 3.12 (the headless verification environment).

```bash
git clone https://github.com/saraheldawody/diabetes-risk-analysis.git
cd diabetes-risk-analysis
python -m venv .venv
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python scripts/check_analysis.py
```

For interactive exploration:

```bash
python -m pip install -r requirements-notebook.txt
jupyter lab diabetes.ipynb
```

Run notebook cells from top to bottom with the repository root as the working directory. The headless check executes Python cells in sequence but does not validate Jupyter rendering or write outputs into the notebook. The direct dependencies are pinned, but a complete transitive lockfile and clean-environment installation check remain outstanding.

## Data and descriptive findings

The CSV contains **768 rows, eight input columns, and `Outcome`**. There are **500 records labeled 0** and **268 labeled 1**. These are dataset counts, not predictive results.

| Column | Meaning documented in the original notebook |
| --- | --- |
| Pregnancies | Number of pregnancies |
| Glucose | Glucose measurement |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skinfold thickness |
| Insulin | Serum insulin measurement |
| BMI | Body mass index |
| DiabetesPedigreeFunction | Diabetes pedigree score |
| Age | Age in years |
| Outcome | Recorded binary diabetes label |

The source citation, cohort definition, measurement protocol/units, target timing, and redistribution terms are **not established by the repository**. Verify these before presenting population-specific conclusions or redistributing the data under a new license. No project license is currently supplied.

Zero-coded missing measurements occur in Glucose (5), BloodPressure (35), SkinThickness (227), Insulin (374), and BMI (11). The corrected EDA replaces those zeros with missing values and then nonzero column medians, without consulting `Outcome`. Pregnancy and outcome zeros are retained. Median imputation is a documented exploratory choice, not evidence that missingness has been resolved without bias.

## Interpretation and limitations

Plots and correlations describe associations within this sample. They do not establish causality, statistical significance, future onset risk, treatment effects, or generalization to Egypt. Earlier numerical interpretations were removed after correcting preprocessing; rerun the notebook before interpreting its plots. No accuracy, recall, AUROC, or clinical benefit is claimed.

## Next priorities

1. Verify dataset provenance, cohort/target definitions, and licensing.
2. Compare raw versus imputed EDA and assess missingness sensitivity.
3. If extending to prediction, implement training-fold preprocessing, stratified validation, dummy/logistic baselines, and a held-out evaluation. See [the review and evaluation plan](docs/REVIEW.md).
