# Customer Churn: Executive Summary
**SWYNEX Technologies Data Science Internship, Task 2** | Dataset: IBM Telco Customer Churn (7,043 customers)

## Headline
**26.5% of customers churned (1,869). The loss is concentrated, predictable and addressable.** Churners hold 30.5% of monthly recurring revenue ($139K of $456K).

## What drives churn (all effects hold after statistical controls)
| Driver | Churn rate | Adjusted effect on churn odds |
|---|---|---|
| Month-to-month contract (vs two-year) | 42.7% vs 2.8% | Two-year: 74% lower |
| First 6 months of tenure (vs 49+) | 52.9% vs 9.5% | 31% lower per extra year |
| Fiber optic (vs DSL) | 41.9% vs 19.0% | 66% higher |
| No online security / no tech support | 41.8% / 41.6% vs 14.6% / 15.2% | 37% / 32% lower with the service |
| Electronic check (vs credit card) | 45.3% vs 15.2% | 55% higher |
| Paperless billing | 33.6% vs 16.3% | 45% higher |
| Senior citizen | 41.7% vs 23.6% | 28% higher |

Gender and phone service have no effect. Partner status is not significant once other features are controlled.

## Where to act first
**Month-to-month + fiber optic + electronic check customers:** 18.6% of customers, **42.2% of churners**, 60.4% churn rate (71.2% in their first year), **49% of lost monthly revenue**.

## The signal is usable
A plain logistic regression reaches ROC-AUC 0.84 and PR-AUC 0.65 (chance: 0.27) in cross-validation. The top 20% of customers by predicted risk contain 51% of all churners.

## Recommended actions
1. Offer annual-contract upgrades to the high-risk segment.
2. Build an onboarding and early-life retention programme for months 0 to 6.
3. Investigate the fiber optic experience (service quality, pricing, competitors).
4. Pilot discounted online security and tech support as a controlled test.
5. Promote autopay, starting with electronic-check customers.

## Caveats
Single static snapshot: associations, not proven causes. Validate retention actions with controlled experiments.

*Full analysis: `notebooks/02_exploratory_data_analysis.ipynb`*
