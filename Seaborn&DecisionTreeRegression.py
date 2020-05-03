import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor


def compare_bachelors_1980(data):
    """
    Determines percentages of men and women
    who earned a Bachelor's Degree in 1980.
    Inputs: parse csv data
    Outputs: dataset with index, sex, and percentage
    """

    f_mask = data['Sex'] == "F"
    m_mask = data['Sex'] == "M"
    bachelors_mask = data['Min degree'] == "bachelor's"
    mask_1980 = data['Year'] == 1980

    # filters with given mask parameters
    filtered_df = data[(f_mask | m_mask) & bachelors_mask & mask_1980]
    # condenses data frame to only show Sex and Total columns
    condensed_df = filtered_df.loc[:, ['Sex', 'Total']]

    return condensed_df


def top_2_2000s(data):
    """
    Determines the two commonly awarded academic degrees
    between 2000 and 2010 (inclusive)
    Uses the mean of percent earned.
    Returns a series with top two.
    """

    mask_2000 = data['Year'] >= 2000
    mask_2010 = data['Year'] <= 2010
    all_mask = data['Sex'] == 'A'

    filtered_df = data[mask_2000 & mask_2010 & all_mask]

    grouped_avg = filtered_df.groupby('Min degree')['Total'].mean()

    top_2 = grouped_avg.nlargest(2)

    return top_2


def percent_change_bachelors_2000s(data, sex='A'):
    """
    determines percent change in bachelor's attainment between 2000 and 2010.
    User may specify sex as a string input, but defaults to "A".
    """

    mask_2000 = data['Year'] == 2000
    mask_2010 = data['Year'] == 2010

    sex_mask = data['Sex'] == sex
    bachelor_mask = data['Min degree'] == "bachelor's"

    filtered_df = data[(mask_2000 | mask_2010) & sex_mask & bachelor_mask]
    indexes = filtered_df.index

    difference = filtered_df.loc[indexes[1], 'Total'] \
        - filtered_df.loc[indexes[0], 'Total']

    return difference


def line_plot_bachelors(data):
    """
    Plots percent change of attainment of
    bachelor's degrees as a function of time (in years)
    """

    mask_all = data['Sex'] == 'A'
    mask_bachelors = data['Min degree'] == "bachelor's"
    filt_data = data[mask_all & mask_bachelors]
    # Relational Plot
    sns.relplot(x="Year", y="Total", kind="line", data=filt_data)
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.title("Percentage Earning Bachelor's Over Time")
    plt.grid()
    plt.savefig('line_plot_bachelors.png', bbox_inches='tight')


def bar_chart_high_school(data):
    """
    Plots the total percentage of men and women who
    attained a high school diploma in 2009 as a bar chart
    """

    mask_highschool = data['Min degree'] == 'high school'
    mask_2009 = data['Year'] == 2009

    filtered_df = data[mask_highschool & mask_2009]
    # Categorial Plot
    sns.catplot(x='Sex', y="Total", data=filtered_df, kind="bar")
    plt.xlabel('Sex')
    plt.ylabel('Percentage')
    plt.title("Percentage Completed High School by Sex")
    plt.savefig('bar_chart_high_school.png', bbox_inches='tight')


def plot_hispanic_min_degree(data):
    """
    Plots progression of high school and bachelor's degree
    attainment for hispanics between 1990 and 2010 (inclusive)
    """
    # Masks required for this data set, notice inclusivity of years
    mask_1990 = data['Year'] >= 1990
    mask_2010 = data['Year'] <= 2010
    mask_highschool = data['Min degree'] == 'high school'
    mask_bachelors = data['Min degree'] == "bachelor's"
    mask_sex = data['Sex'] == 'A'

    df = data[mask_1990 & mask_2010 &
              (mask_highschool | mask_bachelors) & mask_sex]
    # Relational Plot
    sns.relplot(x="Year", y="Hispanic", data=df,
                hue='Min degree', kind="line")
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    # rotate x-axis labels by -45 degrees
    plt.xticks(rotation=-45)
    plt.title("Percent change of attainment of high school and" +
              "bachelor's degrees by Hispanics, 1990-2010")
    plt.savefig('plot_hispanic_min_degree.png', bbox_inches='tight')


def fit_and_predict_degrees(data):
    """
    Prediction model using decision tree regressor for this data set,
    performs prediction on test set, which is 20% of data.
    Checks accuracy with mean squared error.
    Features are Year, Min Degree, and Sex, with labels being Total.
    NaN values are dropped from filtered data
    """

    data = data.loc[:, ['Year', 'Min degree', 'Sex', 'Total']]
    data = data.dropna()

    features = data.loc[:, data.columns != 'Total']
    features = pd.get_dummies(features)  # One Hot Encoding
    labels = data['Total']

    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.2)

    model = DecisionTreeRegressor()
    model.fit(features_train, labels_train)

    test_pred = model.predict(features_test)
    test_acc = mean_squared_error(labels_test, test_pred)

    return test_acc


def main():

    data = pd.read_csv("hw3-nces-ed-attainment.csv", na_values='---')
    compare_bachelors_1980(data)
    top_2_2000s(data)
    percent_change_bachelors_2000s(data)
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    fit_and_predict_degrees(data)


if __name__ == "__main__":
    main()
