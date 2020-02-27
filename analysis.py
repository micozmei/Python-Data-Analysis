from kmeans import assign_data_to_closest_centroid
from utils import load_centroids, read_data


def update_assignment(data, labels, centroids):
    """Assign all data points to the closest centroids and keep track of their
    labels. The i-th point in "data" corresponds to the i-th label in "label".

    Arguments:
        data: a list of lists representing all data points
        labels: a list of ints representing all data labels
        centroids: the centroid dictionary

    Returns: a new dictionary whose keys are the centroids' key names and
             values are a list of labels of the data points that are assigned
             to that centroid.
    """
    point_assignment = {}
    for index in range(len(data)):
        closest_centroid = \
            assign_data_to_closest_centroid(data[index], centroids)
        if closest_centroid not in point_assignment.keys():
            point_assignment[closest_centroid] = []
        point_assignment[closest_centroid].append(labels[index])
    return point_assignment


def majority_count(labels):
    """Return the count of the majority labels in the label list

    Arguments:
        labels: a list of labels

    Returns: the count of the majority labels in the list
    """
    counter = 0
    for num in labels:
        frequency = labels.count(num)
        if frequency > counter:
            counter = frequency
    return counter


def accuracy(data, labels, centroids):
    """Calculate the accuracy of the algorithm. You should use
    update_assignment and majority_count (that you previously implemented)

    Arguments:
        data: a list of lists representing all data points
        labels: a list of ints representing all data labels
        centroids: the centroid dictionary

    Returns: a float representing the accuracy of the algorithm
    """
    label_dict = update_assignment(data, labels, centroids)
    sum = 0
    for label_list in label_dict.values():
        sum += majority_count(label_list)
        accuracy = sum / len(labels)
    return accuracy


if __name__ == '__main__':
    centroids = load_centroids("mnist_final_centroids.csv")
    # print(len(centroids))
    data, label = read_data("data/mnist.csv")
    print(accuracy(data, label, centroids))


# 1) What happened to the centroids? Why are there fewer than 10?
#    There are now only 9 centroids. This is bacause there were centroids
#    that were not closest to any point and the algorithm takes these out.
#    This makes sense because the location of the centroids moved from where
#    they were randomly initialized to a more meaningful space that corresponds
#    to where the MNIST data is distributed.

# 2) What's the accuracy of the algorithm on MNIST? By looking at the
# centroids, which digits are easier to be distinguished by the algorithm,
# and which are harder?
#    The algorithm is 58.2% accurate on MNIST. This is to be expected when
#    digits such as 3 and 8 or 5 and 6 look similar. Distinct looking digits,
#    such as 0 and 1, are more easily recognized by the algorithm.
