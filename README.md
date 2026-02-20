# AI Data Center Policy Model  
## Evaluation of Emission Policies Under Uncertainty

---

## Project Overview

This project uses a quantitative model to evaluate the effectiveness of different economic policies at reducing the environmental impact of AI related data centers. Emissions are modeled using the below framework:

E = Y x C  

Variables:

- E = emissions (million metric tons of CO2 per year)
- Y = electricity consumption (in TWh)
- C = Carbon intensity (grams of CO2 per kWh)

The model compares carbon taxes, clean energy subsidies, dynamic energy pricing, clean energy mandates, and the proposed policy combination from the paper.

---

## Methodology

### Deterministic Policy Model
- Calibrated to the 2028 baseline
- Computes emissions, government costs, firm costs and total cost per ton
- Creates a baseline ranking for each policy for later analysis

### Sensitivity Analysis
- Applies a +/-10% shock to both electricity demand and carbon intensity in the model
- Evaluates the stability of each policy under uncertainty

### Monte Carlo Simulation (10,000 sims)
Computes:
- expected emissions
- downside emissions (95th percentile)
- distribution of cost per ton
- 90% dispersion range
- Policies are evaluated as risk-adjusted decisions

### Portfolio Policy Evaluation
- Compares the proposed Dynamic Energy Pricing + Clean Energy Mandate combination to the single-policy approaches
- Evaluates the tradeoffs of the combination between emission reductions and cost efficiency

---

## Key Findings

- Clean Energy Mandate has strong emission changes but includes highest cost volatility
- Clean Energy Subsidy produces the lowest forecasted emissions
- Carbon Taxes provide moderate emission changes at the best fiscal cost
- Dynamic Energy Pricing + Clean Energy Mandate improves emissions performance relative to other options while keeping costs to government and firms low, preserving innovation incentive
- Policy ranking effectiveness are preserved under the +/- 10% sensitivity shock

---

## Structure

data/           Reserved for later calibration inputs  
src/            Core emissions and cost metric functions  
notebooks/      Structured analytical workflow  
outputs/        Generated figures and tables  

---

## Reproducibility

To reproduce results:

Install dependencies from requirements.txt  

Run notebooks in order:

- 01_deterministic_model.ipynb  
- 02_sensitivity_analysis.ipynb  
- 03_monte_carlo_simulation.ipynb  
- 04_policy_portfolio.ipynb  

---

## Author

Finn Case
