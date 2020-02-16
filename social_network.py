import networkx as nx
import matplotlib.pyplot as plt
# from operator import itemgetter


practice_graph = nx.Graph()

practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
practice_graph.add_edge("B", "D")
practice_graph.add_edge("C", "F")
practice_graph.add_edge("C", "D")
practice_graph.add_edge("D", "F")
practice_graph.add_edge("D", "E")
nx.draw_networkx(practice_graph)
plt.show()

assert len(practice_graph.nodes()) == 6
assert len(practice_graph.edges()) == 8

# Test shape of practice graph
assert set(practice_graph.neighbors("A")) == set(["B", "C"])
assert set(practice_graph.neighbors("B")) == set(["A", "D", "C"])
assert set(practice_graph.neighbors("C")) == set(["A", "B", "D", "F"])
assert set(practice_graph.neighbors("D")) == set(["B", "C", "E", "F"])
assert set(practice_graph.neighbors("E")) == set(["D"])
assert set(practice_graph.neighbors("F")) == set(["C", "D"])


def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()

# draw_practice_graph(practice_graph)


rj = nx.Graph()

rj.add_edge("Juliet", "Nurse")
rj.add_edge("Juliet", "Tybalt")
rj.add_edge("Juliet", "Capulet")
rj.add_edge("Juliet", "Friar Laurence")
rj.add_edge("Juliet", "Romeo")
rj.add_edge("Romeo", "Friar Laurence")
rj.add_edge("Romeo", "Benvolio")
rj.add_edge("Romeo", "Montague")
rj.add_edge("Romeo", "Mercutio")
rj.add_edge("Capulet", "Tybalt")
rj.add_edge("Capulet", "Escalus")
rj.add_edge("Capulet", "Paris")
rj.add_edge("Mercutio", "Escalus")
rj.add_edge("Mercutio", "Paris")
rj.add_edge("Montague", "Benvolio")
rj.add_edge("Montague", "Escalus")
rj.add_edge("Escalus", "Paris")

nx.draw_networkx(rj)
plt.show()

assert len(rj.nodes()) == 11
assert len(rj.edges()) == 17

# Test shape of Romeo-and-Juliet graph
assert set(rj.neighbors("Nurse")) == set(["Juliet"])
assert set(rj.neighbors("Friar Laurence")) == set(["Juliet", "Romeo"])
assert set(rj.neighbors("Tybalt")) == set(["Juliet", "Capulet"])
assert set(rj.neighbors("Benvolio")) == set(["Romeo", "Montague"])
assert set(rj.neighbors("Paris")) == set(["Escalus", "Capulet", "Mercutio"])
assert set(rj.neighbors("Mercutio")) == set(["Paris", "Escalus", "Romeo"])
assert set(rj.neighbors("Montague")) == set(["Escalus", "Romeo", "Benvolio"])
assert set(rj.neighbors("Capulet")) == \
    set(["Juliet", "Tybalt", "Paris", "Escalus"])
assert set(rj.neighbors("Escalus")) == \
    set(["Paris", "Mercutio", "Montague", "Capulet"])
assert set(rj.neighbors("Juliet")) == \
    set(["Nurse", "Tybalt", "Capulet", "Friar Laurence", "Romeo"])
assert set(rj.neighbors("Romeo")) == \
    set(["Juliet", "Friar Laurence", "Benvolio", "Montague", "Mercutio"])


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()

# draw_rj(rj)


def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    return set(graph.neighbors(user))


assert friends(rj, "Mercutio") == set(['Romeo', 'Escalus', 'Paris'])


def friends_of_friends(graph, user):
    """Returns a set of friends of friends of the given user, in the given
    graph. The result does not include the given user nor any of that user's
    friends.
    """
    friends_of_friends_set = set()
    for friend in friends(graph, user):
        friends_of_friends_set = friends_of_friends_set | \
            set(graph.neighbors(friend))
    return (friends_of_friends_set - friends(graph, user) - {user})


assert friends_of_friends(rj, "Mercutio") == \
    set(['Benvolio', 'Capulet', 'Friar Laurence', 'Juliet', 'Montague'])


def common_friends(graph, user1, user2):
    """Returns the set of friends that user1 and user2 have in common.
    """
    return friends(graph, user1) & friends(graph, user2) - {user1, user2}


assert common_friends(practice_graph, "A", "B") == set(['C'])
assert common_friends(practice_graph, "A", "D") == set(['B', 'C'])
assert common_friends(practice_graph, "A", "E") == set([])
assert common_friends(practice_graph, "A", "F") == set(['C'])
assert common_friends(rj, "Mercutio", "Nurse") == set()
assert common_friends(rj, "Mercutio", "Romeo") == set()
assert common_friends(rj, "Mercutio", "Juliet") == set(["Romeo"])
assert common_friends(rj, "Mercutio", "Capulet") == set(["Escalus", "Paris"])


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      number_of_common_friends_map(my_graph, "X")  =>   {'Y': 2, 'Z': 1}
    """
    friends_map = {}
    for guy in friends_of_friends(graph, user):
        friends_map[guy] = len(common_friends(graph, user, guy))
    return friends_map


assert number_of_common_friends_map(practice_graph, "A") == {'D': 2, 'F': 1}
assert number_of_common_friends_map(rj, "Mercutio") == \
    {'Benvolio': 1, 'Capulet': 2, 'Friar Laurence': 1,
     'Juliet': 1, 'Montague': 2}


def number_map_to_sorted_list(map_with_number_vals):
    """Given map_with_number_vals, a dictionary whose values are numbers,
    return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.
    """
    map = map_with_number_vals
    # Sort keys alphabetically first
    sortedmap1 = {k: v for k, v in sorted
                  (map.items(), key=lambda item: item[0], reverse=False)}
    # Then sort by value (descending)
    sortedmap2 = {k: v for k, v in sorted
                  (sortedmap1.items(), key=lambda item: item[1], reverse=True)}
    sorted_list = []
    for key in sortedmap2.keys():
        sorted_list.append(key)
    return(sorted_list)


assert number_map_to_sorted_list({"a": 5, "b": 2, "c": 7, "d": 5, "e": 5}) == \
    ['c', 'a', 'd', 'e', 'b']


def recommend_by_number_of_common_friends(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user. The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first). In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    return(number_map_to_sorted_list
           (number_of_common_friends_map(graph, user)))


assert recommend_by_number_of_common_friends(practice_graph, "A") == ['D', 'F']
assert recommend_by_number_of_common_friends(rj, "Mercutio") == \
    ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """
    inf_map = {}
    for guy in friends_of_friends(graph, user):
        influence = 0
        for friend in common_friends(graph, user, guy):
            influence += 1/len(friends(graph, friend))
        inf_map[guy] = influence
    return inf_map


assert influence_map(rj, "Mercutio") == \
    {'Benvolio': 0.2, 'Capulet': 0.5833333333333333,
     'Friar Laurence': 0.2, 'Juliet': 0.2, 'Montague': 0.45}


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user. The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first). In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    return(number_map_to_sorted_list(influence_map(graph, user)))


assert recommend_by_influence(rj, "Mercutio") == \
    ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


unchanged = []
changed = []
for user in rj.nodes:
    if recommend_by_number_of_common_friends(rj, user) ==\
      recommend_by_influence(rj, user):
        unchanged.append(user)
    else:
        changed.append(user)

print("Unchanged Recommendations: ", sorted(unchanged))
print("Changed Recommendations: ", sorted(changed))


# Read data file into list
# fbfile = open("facebook-links-small.txt")
fbfile = open("facebook-links.txt")
fblines = []
for line_of_text in fbfile:
    fblines.append(line_of_text)

# Graph facebook data
facebook = nx.Graph()
for line_of_text in fblines:
    word_list = line_of_text.split()
    facebook.add_edge(int(word_list[0]), int(word_list[1]))

assert len(facebook.nodes()) == 63731
assert len(facebook.edges()) == 817090


for ID in sorted(facebook.nodes()):
    if ID % 1000 == 0:  # ID multiple of 1000
        rec = recommend_by_number_of_common_friends(facebook, ID)
        print(str(ID) + ' (by number_of_common_friends): ' + str(rec[0:10]))


for ID in sorted(facebook.nodes()):
    if ID % 1000 == 0:  # ID multiple of 1000
        rec = recommend_by_influence(facebook, ID)
        print(str(ID) + ' (by influence): ' + str(rec[0:10]))


same = 0
different = 0
for ID in facebook.nodes():
    if ID % 1000 == 0:  # ID multiple of 1000
        if recommend_by_number_of_common_friends(facebook, ID) ==\
           recommend_by_influence(facebook, ID):
            same += 1
        else:
            different += 1

print('Same: ' + str(same))
print('Different: ' + str(different))
