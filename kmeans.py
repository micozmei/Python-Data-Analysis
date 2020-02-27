import os
import math
from utils import converged, plot_2d, plot_centroids, read_data, \
    load_centroids, write_centroids_tofile
import matplotlib.pyplot as plt


# problem for students
def euclidean_distance_between_data(dp1, dp2):
    """Calculate the Euclidean distance between two data points.

    Arguments:
        dp1: a list of floats representing a data point
        dp2: a list of floats representing a data point

    Returns: the Euclidean distance between two data points
    """
    sum = 0
    for index in range(len(dp1)):
        sum += (dp1[index]-dp2[index]) ** 2
        distance = math.sqrt(sum)
    return distance


# problem for students
def assign_data_to_closest_centroid(data_point, centroids):
    """Assign a single data point to the closest centroid. You should use
    euclidean_distance_between_data function (that you previously implemented).

    Arguments:
        data_point: a list of floats representing a data point
        centroids: a dictionary representing the centroids where the keys are
                   strings (centroid names) and the values are lists of
                   centroid locations

    Returns: a string as the key name of the closest centroid to the data point
    """
    mindistance = float("inf")
    closest = ""
    for key in centroids.keys():
        if euclidean_distance_between_data(data_point, centroids[key]) < \
           mindistance:
            mindistance = \
                euclidean_distance_between_data(data_point, centroids[key])
            closest = key
    return closest


# problem for students
def update_assignment(data, centroids):
    """Assign all data points to the closest centroids. You should use
    assign_data_to_closest_centroid function (that you previously
    implemented).

    Arguments:
        data: a list of lists representing all data points
        centroids: a dictionary representing the centroids where the keys are
                   strings (centroid names) and the values are lists of
                   centroid locations

    Returns: a new dictionary whose keys are the centroids' key names and
             values are lists of points that belong to the centroid
    """
    point_assignment = {}
    for index in range(len(data)):
        closest_centroid = \
            assign_data_to_closest_centroid(data[index], centroids)
        if closest_centroid not in point_assignment.keys():
            point_assignment[closest_centroid] = []
        point_assignment[closest_centroid].append(data[index])
    return point_assignment


# problem for students
def mean_of_points(data):
    """Calculate the mean of a given group of data points. You should NOT hard
    -code the dimensionality of the data points).

    Arguments:
        data: a list of lists representing a group of data points

    Returns: a list of floats as the mean of the given data points
    """
    mean_list = []
    for col in range(len(data[0])):  # len(data[0]) = dimensions
        sum = 0
        for row in range(len(data)):  # len(data) = number of points
            sum += data[row][col]
        mean_list.append(sum / len(data))
    return mean_list


# problem for students
def update_centroids(assignment_dict):
    """Update centroid locations as the mean of all data points that belong
    to the cluster. You should use mean_of_points function (that you previously
    implemented).

    Arguments:
        assignment_dict: the dictionary returned by update_assignment function

    Returns: A new dictionary representing the updated centroids
    """
    new_centroids = {}
    for centroid_name in assignment_dict.keys():
        mean = mean_of_points(assignment_dict[centroid_name])
        new_centroids[centroid_name] = mean
    return new_centroids


def main_2d(data, init_centroids):
    #######################################################
    # You do not need to change anything in this function #
    #######################################################
    centroids = init_centroids
    old_centroids = None
    step = 0
    while not converged(centroids, old_centroids):
        # save old centroid
        old_centroids = centroids
        # new assignment
        assignment_dict = update_assignment(data, old_centroids)
        # update centroids
        centroids = update_centroids(assignment_dict)
        # plot centroid
        fig = plot_2d(assignment_dict, centroids)
        plt.title(f"step{step}")
        fig.savefig(os.path.join("results", "2D", f"step{step}.png"))
        plt.clf()
        step += 1
    print(f"K-means converged after {step} steps.")
    return centroids


def main_mnist(data, init_centroids):
    #######################################################
    # You do not need to change anything in this function #
    #######################################################
    centroids = init_centroids
    # plot initial centroids
    plot_centroids(centroids, "init")
    old_centroids = None
    step = 0
    while not converged(centroids, old_centroids):
        # save old centroid
        old_centroids = centroids
        # new assignment
        assignment_dict = update_assignment(data, old_centroids)
        # update centroids
        centroids = update_centroids(assignment_dict)
        step += 1
    print(f"K-means converged after {step} steps.")
    # plot final centroids
    plot_centroids(centroids, "final")
    return centroids


if __name__ == '__main__':
    data, label = read_data("data/data_2d.csv")
    init_c = load_centroids("data/2d_init_centroids.csv")
    final_c = main_2d(data, init_c)
    write_centroids_tofile("2d_final_centroids.csv", final_c)

# if __name__ == '__main__':
#     data, label = read_data("data/mnist.csv")
#     init_c = load_centroids("data/mnist_init_centroids.csv")
#     final_c = main_mnist(data, init_c)
#     write_centroids_tofile("mnist_final_centroids.csv", final_c)
