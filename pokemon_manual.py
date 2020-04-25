"""
Dictionary Functions
"""


def species_count(data):
    """
    Returns number of unique species in list of dictionaries set data
    """

    count = 0
    species_set = set()
    # checks if species is already in the species_set
    # before adding to count
    for line in data:
        if line['name'] not in species_set:
            count += 1
            species_set.add(line['name'])
    return count


def max_level(data):
    """
    From data, returns the name of the pokemon with the max level.
    In the event of a tie, will return the pokemon that appeared
    first in the data
    """

    max_lvl = 0
    name = ''

    for line in data:
        if line['level'] > max_lvl:
            max_lvl = line['level']
            name = line['name']
    return (name, max_lvl)


def filter_range(data, small, large):
    """
    Inputs: data - dataset to be evaluated
            low - low value in range (inclusive)
            high - high value in range (exclusive)

    Outputs: list of pokemon names which have levels
             within specified range
    """

    range_list = []
    # checks if level is in range and then appends if so
    for line in data:
        if line['level'] >= small and line['level'] < large:
            range_list.append(line['name'])

    return range_list


def mean_attack_for_type(data, string):
    """
    Input: data - dataset to be evaluated
           string - name of pokemon type to be evaluated
    Output: average atk value for pokemon type string in dataset data.
            if string is not in data, returns None.
    """
    type_sum = 0
    type_count = 0

    for line in data:
        if line['type'] == string:
            type_sum += line['atk']
            type_count += 1

    if type_count == 0:
        return None

    return type_sum / type_count


def count_types(data):
    """
    Input: data - dataset to be evaluated
    Output: dictionary with pokemon types as keys and
            number of occurences of each type as values.
    """

    type_dict = {}

    # iterates through data set and adds type to keys and updates
    # value for each count
    for line in data:
        poke_type = line['type']

        if poke_type in type_dict:
            type_dict[poke_type] += 1

        else:
            type_dict[poke_type] = 1

    return type_dict


def highest_stage_per_type(data):
    """
    Input: data - dataset to be evaluated
    Output: returns a dictionary with pokemon types as
            keys and highest stage of each type as values
    """
    # iterates through data and updates if
    # maximum val is higher than current max
    stage_dict = {}
    for line in data:
        poke_type = line['type']
        stage = line['stage']
        if poke_type in stage_dict.keys():
            if stage > stage_dict[poke_type]:
                stage_dict[poke_type] = stage

        else:
            stage_dict[poke_type] = stage

    return stage_dict


def mean_attack_per_type(data):
    """
    Input: data - dataset to be evalulated
    Output: returns a dictionary with pokemon types
            as keys and mean attack of each type as values
    """

    mean_dict = {}
    count_dict = {}
    sum_dict = {}

    # iterates and appends count and sum dictionaries for
    # each type
    for line in data:
        atk_val = line['atk']
        type_val = line['type']

        if type_val in count_dict.keys():
            count_dict[type_val] += 1
            sum_dict[type_val] += atk_val
        else:
            count_dict[type_val] = 1
            sum_dict[type_val] = atk_val

    mean_dict = dict.fromkeys(count_dict.keys())
    # computes average from sum and count
    for key in mean_dict.keys():
        mean_dict[key] = sum_dict[key] / count_dict[key]

    return mean_dict
