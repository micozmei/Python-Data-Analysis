def total(n):
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def count_divisible_digits(n, m):
    """
    Returns number of digits of n that are divisible
    by m. Assumes 0 <= m < 10
    """

    count = 0

    # ensures n is positive
    n = abs(n)

    # return 0 if m = 0, or 1 if n = 0, or
    # performs computation of divisible digits
    if m == 0:
        return count
    elif n == 0:
        return 1
    else:
        while n != 0:
            digit = n % 10
            if digit % m == 0:
                count += 1
            n = n // 10
        return count


def is_relatively_prime(n, m):
    """
    Returns True or False on if n and m are relatively prime.
    Relatively prime numbers have no shared common factors aside from 1
    """

    # performs calculation depending on whether n or m is larger.
    if n < m:
        for i in range(2, m + 1):
            if m % i == 0:
                if n % i == 0:
                    return False
            return True
    if n >= m:
        for i in range(2, n + 1):
            if n % i == 0:
                if m % i == 0:
                    return False
            return True


def travel(string, x, y):
    """
    Moves a point on coordinates (x, y) by directions given by North
    (N or n) South (S or s) East (E or e) and West (W or w)in a string.
    If a character in the string is not a direction,
    it will be ignored. Note directions are not case sensitive
    """

    # performs translation depending on character name
    for char in string:
        if char == 'N' or char == 'n':
            y = y + 1
        elif char == 'S' or char == 's':
            y = y - 1
        elif char == 'W' or char == 'w':
            x = x - 1
        elif char == 'E' or char == 'e':
            x = x + 1
    return str((x, y))


def swip_swap(source, c1, c2):
    """
    Swaps locations of characters c1 and c2 in input string source.
    If one character does not exist, it will replace the existing one.
    If neither exist in source, source will be unaltered.
    """
    index_c1 = []
    index_c2 = []
    # conversion to list necessary to be able to determine indices
    source_as_list = [i for i in source]

    # determines locations of occurences of c1 and c2 in source
    for i in range(len(source_as_list)):
        if source_as_list[i] == c1:
            index_c1.append(i)

        elif source_as_list[i] == c2:
            index_c2.append(i)
    # scenario if both c1 & c2 are in source,
    # and accounts for cases where there are more
    # than one case of either.

    if c1 in source_as_list and c2 in source_as_list:
        if len(index_c2) > 1:
            for i in index_c2:
                source_as_list[i] = c1
            source_as_list[index_c1[0]] = c2

        elif len(index_c1) > 1:
            for i in index_c1:
                source_as_list[i] = c2
            source_as_list[index_c2[0]] = c1

        else:
            source_as_list[index_c2] = c1
            source_as_list[index_c1] = c2

    # cases where there is only c1 or c2 in source

    elif c1 in source_as_list:
        for i in index_c1:
            source_as_list[i] = c2

    elif c2 in source_as_list:
        for i in index_c2:
            source_as_list[i] = c2

    return "".join(source_as_list)


def compress(string):
    """
    takes string and returns a new string
    that each character is followed by its
    consecutive count, with adjacent duplicate
    characters removed.
    """

    new_string_as_list = []
    count = 1
    # compares index i to index i + 1 to find
    # conseq duplicates, then stores in a counter
    # if no duplicates, count = 1, if at end of string,
    # stops count

    for i in range(len(string)):
        if i == len(string) - 1:
            new_string_as_list.append(string[i])
            new_string_as_list.append(str(count))

        elif string[i+1] == string[i]:
            count += 1
        else:
            new_string_as_list.append(string[i])
            new_string_as_list.append(str(count))
            count = 1

    return "".join(new_string_as_list)


def longest_line_length(file_name):
    """
    Determines length of longest line in .txt file
    """
    with open(file_name) as file:
        lines = file.readlines()

        max_count = 0
        # checks if file is empty
        if len(lines) == 0:
            return None

        # performs count of each line and saves max count
        for line in lines:

            count = len(line)

            if count > max_count:
                max_count = count

        return max_count


def longest_word(file_name):
    """
    Finds longest word and its associated line number in file_name.
    """

    with open(file_name) as file:
        lines = file.readlines()
        line_num = 1
        max_word_len = 0
        # return None if file is empty
        if len(lines) == 0:
            return None
        # checks each word through each line
        for line in lines:

            line = line.split()

            for word in line:
                # checks if word is longer than max
                # recorded length, and updates max if it does
                if len(word) > max_word_len:
                    max_word_len = len(word)
                    max_word = word
                    max_line_num = line_num

            line_num += 1

        return str(max_line_num) + ":" + " " + str(max_word)


def mode_digit(n):
    """
    For a number n, determines most common digit
    """
    count_list = [0] * 10

    digit_list = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # ensures no negative sign in processing
    n = abs(n)
    # conversion to string
    num_as_list = [i for i in str(n)]

    # in the event that there is a tie, we want to return the larger value.
    # Therefore, we will index
    # from ascending digits so we can use s.index

    # counts each occurence of digit i and stores in count list going backwards
    for i in range(10):
        for num in num_as_list:
            if str(i) == num:
                count_list[9 - i] += 1

    # finds index of max value of count
    max_idx = count_list.index(max(count_list))

    return digit_list[max_idx]
