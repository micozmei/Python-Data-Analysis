import re


class Document:
    """
    Represenation of a file inside a directory to be processed by SearchEngine.
    Calculates the term frequency for a given term,
    and allows to acquire path name and a list of words in the document.
    """

    def __init__(self, filename):
        """
        Initializes document class with specified filename.
        Generates dictionary of each word in file as key and
        its frequency as value
        """
        self._filename = filename

        freq_dict = {}
        word_dict = {}
        word_count = 0
        # Stores each word in word dictionary and counts occurences.
        with open(self._filename) as doc:
            lines = doc.readlines()
            for line in lines:
                line = line.split()
                for word in line:
                    word = re.sub(r'\W+', '', word)  # removes punctuation
                    word = word.lower()  # lowercase
                    word_count += 1
                    if word in word_dict.keys():
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1

            freq_dict = dict.fromkeys(word_dict.keys())
            # iterates through freq_dict's keys
            # (same as word_dict) and calculates frequency of each word
            for key in freq_dict.keys():
                freq_dict[key] = word_dict[key] / word_count

        self._TF = freq_dict

    def get_path(self):
        """
        Returns path name of filename.
        """
        split_list = self._filename.split('/')
        dir_str = str('')
        for i in range(len(split_list) - 1):
            dir_str += split_list[i] + '/'

        return dir_str

    def term_frequency(self, term):
        """
        Returns term frequency of given term (string).
        If the term is not in the file, returns 0
        """
        term = term.lower()

        if term not in self._TF:
            return 0
        return self._TF[term]

    def get_words(self):
        """
        Returns a list of all words in the document
        """
        return self._TF.keys()
