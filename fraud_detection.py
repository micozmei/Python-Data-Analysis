import csv
import random
import matplotlib.pyplot as plt


def extract_election_vote_counts(filename, column_names):
    '''
    Takes a filename and a list of column names
    Returns a list of integers that contains the values in those columns from
    every row (the order of the integers does not matter).
    '''
    election_csv = open(filename)
    input_file = csv.DictReader(election_csv)
    election_csv.close()
    vote_counts = []
    for row in input_file:  # skips first row
        for name in column_names:
            clean = row[name].replace(',', '')  # remove commas in numbers
            if clean != '':  # ignore any empty entries
                vote_counts.append(int(clean))  # strings of numbers to int
    return vote_counts


def ones_and_tens_digit_histogram(numbers):
    '''
    Takes as input a list of numbers
    Produces as output a list of 10 numbers
    In the returned list, the value at index i is the frequency with which
    digit i appeared in the ones place OR the tens place in the input list.
    '''
    ones = []
    tens = []
    for num in numbers:  # separate ones and tens digits
        one = num % 10
        ones.append(one)
        ten = (num // 10) % 10
        tens.append(ten)

    ones_and_tens = []
    for i in range(10):  # get average frequency of digits
        ones_and_tens.append((ones.count(i) + tens.count(i)) / (2 * len(ones)))
    return ones_and_tens


def plot_iranian_least_digits_histogram(histogram):
    '''
    Graph the frequencies of the ones and tens digits for the election data.
    '''
    xvalues = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    yvalues1 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    plt.plot(xvalues, yvalues1, label='Ideal')  # plot horizontal line

    yvalues2 = histogram
    plt.plot(xvalues, yvalues2, label='Iran')

    plt.xlabel('Digit')
    plt.ylabel('Frequency')
    plt.legend(loc='upper right')
    plt.savefig('iran-digits.png')
    # plt.show()
    plt.clf()


def random_values(size, xvalues):
    '''
    Takes in sample size and x values
    Returns random y values
    '''
    random_list = []
    for i in range(size):
        random_num = random.randint(0, len(xvalues))
        random_list.append(random_num)

    yvalues = []
    for j in xvalues:  # count the number of each number, then normalize
        if j not in yvalues:
            yvalues.append(random_list.count(j)/size)
        else:
            yvalues.append(0)
    return yvalues


def plot_distribution_by_sample_size():
    '''
    Create five different collections (one of size 10, another of size 50,
    then 100, 1000, and 10,000) of random numbers where every element in
    the collection is a different random number x such that 0 <= x < 100
    Plots the digit histograms for each of those collections on one graph.
    '''
    xvalues = [x for x in range(100)]  # x axis is numbers from 0 to 99
    size_list = [10, 50, 100, 1000, 10000]
    for size in size_list:  # make list of 10/50/100/1000/10000 random numbers
        plt.plot(xvalues, random_values(size, xvalues),
                 label=str(size) + ' random numbers')

    plt.plot([0, 99], [0.01, 0.01], label='Ideal')  # plot horizontal line
    plt.title('Distribution by sample size')
    plt.xlabel('Digit')
    plt.ylabel('Frequency')
    plt.legend(loc='best')
    plt.savefig('random-digits.png')
    # plt.show()
    plt.clf()


def mean_squared_error(numbers1, numbers2):
    '''
    Takes two lists of numbers
    Returns the mean squared error between the lists.
    '''
    sum = 0
    for i in range(len(numbers1)):
        sum += (numbers1[i] - numbers2[i]) ** 2
    return sum / len(numbers1)


def calculate_mse_with_uniform(histogram):
    '''
    Takes a histogram (as created by ones_and_tens_digit_histogram)
    Returns the mean squared error of the histogram with uniform distribution.
    '''
    uniform_distribution = [0.1 for i in range(len(histogram))]
    return mean_squared_error(histogram, uniform_distribution)


def comparison(mse, number_of_samples):
    '''
    Used for comparing mse to samples (see 2 functions below)
    '''
    larger_or_equal = 0
    smaller = 0
    xvals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(10000):  # loop 10,000 times
        yvals = (random_values(number_of_samples, xvals))
        random_mse = calculate_mse_with_uniform(yvals)
        if random_mse >= mse:
            larger_or_equal += 1
        else:
            smaller += 1
    p_value = larger_or_equal / 10000
    return larger_or_equal, smaller, p_value


def compare_iranian_mse_to_samples(iranian_mse, number_of_iranian_samples):
    '''
    Takes 2 inputs: the Iranian MSE (as computed by calculate_mse_with_uniform)
    and the number of data points in the Iranian dataset.
    Builds 10,000 groups of random numbers, where each group is the same size
    as the Iranian election data (120 numbers)
    Computes the MSE with the uniform distribution for each of these groups.
    Compares each of these 10,000 MSEs to the Iranian MSE that was passed into
    the function as a parameter.
    '''
    l_or_e, small, p = comparison(iranian_mse, number_of_iranian_samples)
    print('2009 Iranian election MSE: ' + str(iranian_mse))
    print('Quantity of MSEs larger than or equal to the 2009 Iranian election '
          + 'MSE: ' + str(l_or_e))
    print('Quantity of MSEs smaller than the 2009 Iranian election MSE: '
          + str(small))
    print('2009 Iranian election null hypothesis rejection level p: '
          + str(p))


def compare_us_mse_to_samples(us_mse, number_of_us_samples):
    '''
    Same as compare_iranian_mse_to_samples but with us election data
    '''
    l_or_e, small, p = comparison(us_mse, number_of_us_samples)
    print('2008 United States election MSE: ' + str(us_mse))
    print('Quantity of MSEs larger than or equal to the 2008 United States '
          + 'election MSE: ' + str(l_or_e))
    print('Quantity of MSEs smaller than the 2008 United States election MSE: '
          + str(small))
    print('2008 United States election null hypothesis rejection level p: '
          + str(p))


def main():
    # Iranian Election
    numbers_iran = extract_election_vote_counts(
        "election-iran-2009.csv",
        ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])
    histogram_iran = ones_and_tens_digit_histogram(numbers_iran)
    plot_iranian_least_digits_histogram(histogram_iran)
    plot_distribution_by_sample_size()
    mse_iran = calculate_mse_with_uniform(histogram_iran)
    compare_iranian_mse_to_samples(mse_iran, len(numbers_iran))
    print('\n')  # Print new line

    # US Election
    numbers_us = extract_election_vote_counts(
        "election-us-2008.csv",
        ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"])
    histogram_us = ones_and_tens_digit_histogram(numbers_us)
    mse_us = calculate_mse_with_uniform(histogram_us)
    compare_us_mse_to_samples(mse_us, len(numbers_us))


if __name__ == "__main__":
    main()
