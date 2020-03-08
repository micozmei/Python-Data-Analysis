# Test File
from fraud_detection import extract_election_vote_counts, \
    ones_and_tens_digit_histogram, mean_squared_error, \
    calculate_mse_with_uniform


# Problem 1 Tests
def test_extract_election_vote_counts():
    assert extract_election_vote_counts("election-iran-2009.csv",
                                        ["Ahmadinejad", "Rezai", "Karrubi",
                                         "Mousavi"])[0:8] == \
                                         [1131111, 16920, 7246, 837858,
                                          623946, 12199, 21609, 656508]
    assert extract_election_vote_counts("election-us-2008.csv",
                                        ["Obama", "McCain", "Nader", "Barr",
                                         "Baldwin", "McKinney"])[0:8] == \
        [813479, 1266546, 6788, 4991, 4310, 123594, 193841, 3783]
    print("test_extract_election_vote_counts passed!")


# Problem 2 Tests
def test_ones_and_tens_digit_histogram():
    assert ones_and_tens_digit_histogram([127, 426, 28, 9, 90]) == \
        [0.2, 0.0, 0.3, 0.0, 0.0, 0.0, 0.1, 0.1, 0.1, 0.2]

    assert ones_and_tens_digit_histogram([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
                                         89, 144, 233, 377, 610, 987, 1597,
                                         2584, 4181, 6765]) == \
        [0.21428571428571427, 0.14285714285714285, 0.047619047619047616,
         0.11904761904761904, 0.09523809523809523, 0.09523809523809523,
         0.023809523809523808, 0.09523809523809523, 0.11904761904761904,
         0.047619047619047616]
    print('test_ones_and_tens_digit_histogram passed!')


# Problem 5 Tests
def test_mean_squared_error():
    assert mean_squared_error([1, 4, 9], [6, 5, 4]) == 17.0
    assert mean_squared_error([-1, -1, 0, 0], [-1, 1, -1, 1]) == 1.5
    print('test_mean_squared_error passed!')


# Problem 6 Tests
def test_calculate_mse_with_uniform():
    value = calculate_mse_with_uniform(ones_and_tens_digit_histogram(
        extract_election_vote_counts("election-iran-2009.csv", ["Ahmadinejad",
                                     "Rezai", "Karrubi", "Mousavi"])))
    assert value <= 0.000739583333333 + 0.00001 and value >= \
        0.000739583333333 - 0.00001  # allow some room for rounding error
    print('test_calculate_mse_with_uniform passed!')


if __name__ == '__main__':
    test_extract_election_vote_counts()
    test_ones_and_tens_digit_histogram()
    test_mean_squared_error()
    test_calculate_mse_with_uniform()
    print("All tests passed!")
