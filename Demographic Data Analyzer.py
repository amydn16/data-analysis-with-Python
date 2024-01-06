import sys
sys.path.append('/usr/local/lib/python3.9/site-packages')

import pandas as pd

# Define function to analyze csv of demographic data
def calculate_demographic_data(print_data = True):

    # Import csv file as df
    df = pd.read_csv("adult.data.csv")

    # How many people of each race are represented
    # In csv, this is column indexed by 'race'
    race_count = df['race'].value_counts()

    # Calculate the average age of men
    men_df = df[df['sex'] == 'Male'] # Series containing only males
    total_age_men = men_df['age'].sum() # Sum of age column
    # Len returns number of rows; use len(df.columns) for columns
    average_age_men = float(str(round(total_age_men / len(men_df),1)))

    # Calculate percentage of people with bachelors degree
    bachelor_yes = df[df['education'] == 'Bachelors']
    percentage_bachelors = float(str(round((len(bachelor_yes) / len(df)) * 100, 1)))

    # Calculate percentage of people with higher edu that make > $50K
    a_df = df[ (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    rich_df = a_df[a_df['salary'] == '>50K']
    higher_education_rich = float(str(round((len(rich_df) / len(a_df)) * 100, 1 )))

    # Calculate percentage of people without higher edu that make > $50K
    a_df = df[ (df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate') ]
    rich_df = a_df[a_df['salary'] == '>50K']
    lower_education_rich = float(str(round((len(rich_df) / len(a_df)) * 100, 1 )))

    # Find minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # Calculate percentage who work minimum hours per week and make > $50K
    a_df = df[df['hours-per-week'] == int(min_work_hours)]
    rich_df = a_df[a_df['salary'] == '>50K']
    rich_percentage = float(str(round((len(rich_df) / len(a_df)) * 100, 1 )))

    # Find country with highest percentage that earn > $50K
    country_count = df['native-country'].value_counts()
    rich_df = df[df['salary'] == '>50K']
    the_dict = {}

    for item, value in country_count.items():
      a_df = rich_df[rich_df['native-country'] == item]
      the_dict[item] = float((len(a_df) / value) * 100)

    country_count = pd.Series(the_dict)
    highest_earning_country = country_count.idxmax()
    highest_earning_country_percentage = float(str(round(country_count.max(),1)))

    # Identify most popular occupation for those in India making > $50K
    rich_df = df[ (df['native-country'] == 'India') & (df['salary'] == '>50K') ]
    occup_df = rich_df['occupation'].value_counts()
    top_IN_occupation = occup_df.idxmax()

    if print_data:
        print(df.head())
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation}

calculate_demographic_data(print_data = True)
