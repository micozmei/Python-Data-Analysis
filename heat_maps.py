import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def load_in_data(shape, csv):
    """
    Loads in shapefile, shape, and csv with food access data.
    combines both datasets to be used for analysis. Filters only to data in WA
    """
    food_df = pd.read_csv(csv)
    shape_df = gpd.read_file(shape)

    merged_df = shape_df.merge(food_df, left_on="CTIDFP00",
                               right_on="CensusTract", how='left')

    return merged_df


def percentage_food_data(df):
    """
    Calculates percentage of census tracts in WA that have data.
    Value is a float between 0 and 100.
    """

    usable_count = len(usable_data(df))
    total = len(df['lapop10'])

    return usable_count / total * 100


def usable_data(df):
    """
    Helper function that returns usable data
    """

    usable = df[df['lapop10'].notna()]
    return usable


def plot_map(df):
    """
    Plots a map of Washington state with all census tracts
    """

    df_geom = df['geometry']
    df_geom.plot()
    plt.title("A map of Washington")
    plt.savefig("washington_map.png")


def plot_population_map(df):
    """
    Plots population of Washington by census tract
    """

    df = df[['POP2010', 'CensusTract', 'geometry']]
    population = df.dissolve(by="CensusTract", aggfunc='sum')

    population.plot(column="POP2010", legend=True)
    plt.title("Population with regards to CensusTract")
    plt.savefig('washington_population_map.png')


def plot_population_county_map(df):
    """
    Plots WA population by County
    """
    df = df[["POP2010", "County", "geometry"]]
    population = df.dissolve(by="County", aggfunc="sum")

    population.plot(column="POP2010", legend=True)
    plt.title("Population of Washington by County")
    plt.savefig("washington_county_population_map.png")


def plot_food_access_by_county(df):
    """
    Plots Food Access by County in WA
    """
    df = df[['County', 'geometry', 'POP2010', 'lapophalf',
            'lapop10', 'lalowihalf', 'lalowi10']].copy()
    # Perform dissolve by County with summation
    new_df = df.dissolve(by="County", aggfunc='sum')

    POP = new_df['POP2010']

    # Calculates ratio for each case in regards to total pop
    new_df['lapophalf_ratio'] = new_df['lapophalf'] / POP
    new_df['lapop10_ratio'] = new_df['lapop10'] / POP
    new_df['lalowihalf_ratio'] = new_df['lalowihalf'] / POP
    new_df['lalowi10_ratio'] = new_df['lalowi10'] / POP

    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, figsize=(20, 10), ncols=2)

    new_df.plot(column='lapophalf_ratio', legend=True, ax=ax1, vmin=0, vmax=1)
    new_df.plot(column='lapop10_ratio', legend=True, ax=ax3, vmin=0, vmax=1)
    new_df.plot(column='lalowihalf_ratio', legend=True, ax=ax2, vmin=0, vmax=1)
    new_df.plot(column='lalowi10_ratio', legend=True, ax=ax4, vmin=0, vmax=1)

    ax1.set_title('Low Access: Half')
    ax2.set_title('Low Access + Low Income: Half')
    ax3.set_title('Low Access: 10')
    ax4.set_title('Low Access + Low Income: 10')

    fig.savefig('washington_county_food_access.png')


def plot_low_access_tracts(df):
    """
    Plots low access census tracts in WA
    """

    # Produces copy of urban and rural data set
    urban = df[df['Urban'] == 1].copy()
    rural = df[df['Rural'] == 1].copy()

    # Provides geometry of tracts with data
    tract_with_data = usable_data(df)

    # Adds new column 'lowacccess' to each set that calculates
    # percentage of people who meet criteria
    urban['lowaccess'] = urban['lapophalf'] / urban['POP2010']
    rural['lowaccess'] = rural['lapop10'] / rural['POP2010']

    fig, axs = plt.subplots(nrows=1, figsize=(15, 7))

    df.plot(color='#EEEEEE', ax=axs)  # Graph initially all grey
    tract_with_data.plot(color='#AAAAAA', ax=axs)
    urban.plot(column="lowaccess", ax=axs, vmin=0, vmax=1)
    rural.plot(column='lowaccess', ax=axs, vmin=0, vmax=1)

    plt.title('Low Access to Food by County in WA')
    plt.savefig('washington_low_access.png')


def main():
    shape = '/course/food-access/tl_2010_53_tract00/tl_2010_53_tract00.shp'
    csv = '/course/food-access/food-access.csv'
    df = load_in_data(shape, csv)
    percentage_food_data(df)
    plot_map(df)
    plot_population_map(df)
    plot_population_county_map(df)
    plot_food_access_by_county(df)
    plot_low_access_tracts(df)


if __name__ == "__main__":
    main()
