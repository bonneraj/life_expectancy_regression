'''All constants used by the pipeline'''

INPUT_PATH = './input/county_health_data.csv'

INPUT_FIELD_NAMES = ['fips', 'state', 'county', 'years_of_potential_life_lost_rate', 'percent_fair_or_poor_health', 'avg_phys_unhealthy_days', 'avg_mentally_unhealthy_days', 'percent_low_birthweight', 'percent_adults_smoking', 'percent_adults_w_obesity', 'percent_physically_inactive', 'percent_w_access_to_excercise', 'percent_excessive_drinking', 'percent_driving_deaths_w_alc_involvement', 'preventable_hospitalization_rate', 'percent_vaccinated', 'percent_completed_high_school', 'percent_some_college', 'percent_unemployed', '80_percentile_income', '20_percentile_income', 'income_ratio', 'social_association_rate', 'percent_severe_housing_problems', 'life_expectancy', 'age_adj_death_rate', 'child_mortality_rate', 'infant_mortality_rate', 'percent_frequent_physical_distress', 'percent_frequent_mental_distress', 'percent_adults_w_diabetes', 'percent_food_insecure', 'percent_limited_access_to_healthy_foods', 'percent_insufficient_sleep', 'spending_per_pupil', 'school_funding_adequacy', 'gender_pay_gap', 'median_household_income', 'percent_enrolled_in_free_or_reduced_lunch', 'homicide_rate', 'age_adj_suicide_rate', 'percent_voter_turnout', 'percent_homeowners', 'percent_households_w_severe_cost_burden', 'percent_under_18', 'percent_over_65', 'percent_rural']

ID_FIELDS = ['fips', 'state', 'county']

FEATURE_FIELDS = ['years_of_potential_life_lost_rate', 'percent_fair_or_poor_health', 'avg_phys_unhealthy_days', 'avg_mentally_unhealthy_days', 'percent_low_birthweight', 'percent_adults_smoking', 'percent_adults_w_obesity', 'percent_physically_inactive', 'percent_w_access_to_excercise', 'percent_excessive_drinking', 'percent_driving_deaths_w_alc_involvement', 'preventable_hospitalization_rate', 'percent_vaccinated', 'percent_completed_high_school', 'percent_some_college', 'percent_unemployed', '80_percentile_income', '20_percentile_income', 'income_ratio', 'social_association_rate', 'percent_severe_housing_problems','child_mortality_rate', 'percent_adults_w_diabetes', 'percent_food_insecure', 'percent_limited_access_to_healthy_foods', 'percent_insufficient_sleep', 'spending_per_pupil', 'school_funding_adequacy', 'gender_pay_gap', 'median_household_income', 'percent_enrolled_in_free_or_reduced_lunch', 'percent_voter_turnout', 'percent_homeowners', 'percent_households_w_severe_cost_burden', 'percent_under_18', 'percent_over_65', 'percent_rural']

UNUSED_LABEL_FIELDS = ['age_adj_suicide_rate', 'age_adj_death_rate', 'percent_frequent_physical_distress', 'percent_frequent_mental_distress']

LABEL_FIELD = ['life_expectancy']

TEST_SIZE = .3

RANDOM_STATE = 42