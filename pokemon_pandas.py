"""
Pandas Functions
"""


def species_count(data):
    """
    Returns number of unique species in data series data
    """
    name_series = data['name'].unique()

    return len(name_series)


def max_level(data):
    """
    From data, returns the name of the pokemon with the max level as a tuple.
    In the event of a tie, will return the pokemon that appeared
    first in the data
    """

    # Determines location of maximum value and it's value.
    max_loc = data['level'].idxmax()
    max_val = data['level'].max()

    # returns name of pokemon with max value and value as tuple
    return (data['name'].loc[max_loc], max_val)


def filter_range(data, low, high):
    """
    Inputs: data - dataset to be evaluated
            low - low value in range (inclusive)
            high - high value in range (exclusive)

    Outputs: list of pokemon names which have levels
             within specified range
    """

    lowmask = data['level'] >= low
    highmask = data['level'] < high

    filtered_data = data[lowmask & highmask]

    return list(filtered_data['name'])


def mean_attack_for_type(data, string):
    """
    Input: data - dataset to be evaluated
           string - name of pokemon type to be evaluated
    Output: average atk value for pokemon type string in dataset data.
            if string is not in data, returns None.
    """

    if string not in list(data['type']):
        return None

    avg = data.groupby('type')['atk'].mean()

    return avg[string]


def count_types(data):
    """
    Input: data - dataset to be evaluated
    Output: dictionary with pokemon types as keys and
            number of occurences of each type as values.
    """

    vals = data.groupby('type')['name'].count()

    return dict(vals)


def highest_stage_per_type(data):
    """
    Input: data - dataset to be evaluated
    Output: returns a dictionary with pokemon types as
            keys and highest stage of each type as values
    """

    return dict(data.groupby('type')['stage'].max())


def mean_attack_per_type(data):
    """
    Input: data - dataset to be evalulated
    Output: returns a dictionary with pokemon types
            as keys and mean attack of each type as values
    """

    return dict(data.groupby('type')['atk'].mean())
