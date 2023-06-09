# Life Expectancy Community Health Factor Modeling

## Project Overview:
The goal of this project is to build a full modeling pipeline to predict life expectancy of United States counties based on county health data. This library leverages Pandas for data manipulation and Scikit-Learn for data pre-processing and modeling.

## Getting Started:
1. In a bash terminal run 'source ./setup.sh' to install all dependencies

## Running the Pipeline, Unit Tests, and Coverage
2. in a bash terminal, the following scripts can be run to execute the pipeline or testing/coverage: 
    python main.py
    python -m pytest
    python -m pytest --cov=src

## Dataset Overview:
2023 County Health Rankings National Data used is sourced from the University of Wisconsin Population Health Institute and can be found at: https://www.countyhealthrankings.org/explore-health-rankings/rankings-data-documentation

The original dataset from the link above has been adapted outside of this repo as a starting point for this pipeline and can be found at 'input/community_health_factors.csv'. The original excel-based document has been edited to remove extranneous formatting and combine multiple tabs of data before saving as a csv.

## Identifying Features
FIPS identifier, state, county

## Health Measures of Interest
percent_fair_or_poor_health, avg_phys_unhealthy_days, avg_mentally_unhealthy_days, percent_adults_smoking, percent_adults_w_obesity, percent_physically_inactive, percent_w_access_to_excercise, percent_excessive_drinking, percent_unemployed income_ratio , age_adj_death_rate, child_mortality_rate, infant_mortality_rate, percent_frequent_physical_distress, percent_frequent_mental_distress, percent_adults_w_diabetes, percent_food_insecure, percent_limited_access_to_healthy_foods, percent_insufficient_sleep, spending_per_pupil, school_funding_adequacy, gender_pay_gap, median_household_income, percent_enrolled_in_free_or_reduced_lunch, homicide_rate, age_adj_suicide_rate, percent_voter_turnout, percent_homeowners, percent_households_w_severe_cost_burden, percent_under_18, percent_over_65, percent_rural

## Health Outcomes of Interest
life expectancy, age-adjusted death rate, suicide rate (age-adjusted), frequent physical distress, frequent mental distress