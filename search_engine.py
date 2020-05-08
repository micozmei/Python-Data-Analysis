from document import Document
import os
import math


class SearchEngine:
    """
    SearchEngine class, or rather, store-brand Google.
    Utilizes tf-idf to calculate relevancy of files
    to a certain search parameter.
    """

    def __init__(self, dirname):
        """
        Initializes SearchEngine with the name of directory and checks
        for / at end of string.
        Additionaly, creates a list of files in the directory,
        counts the number, and produces an inverted index.
        Also produces a list called listDoc which contains
        a Document object for each filename.
        """

        if dirname[-1] == "/":
            self._dirname = dirname
        else:
            self._dirname = dirname + "/"

        inv_idx = {}

        self._listdir = os.listdir(dirname)
        self._doc_count = len(self._listdir)
        self._listDoc = []

        for file_name in self._listdir:

            # initializes Document under
            # object name file and appends it to listDoc
            File = Document(self._dirname + file_name)  # path
            self._listDoc.append(File)

            # acquires all words in File and generates inverted index
            # inverted index is a dictionary which maps from a term
            # (string) to a list of Documents which contain that term
            words = File.get_words()

            for word in words:
                word = word.lower()
                if word in inv_idx.keys():
                    inv_idx[word].append(file_name)
                else:
                    inv_idx[word] = [file_name]

        self._invidx = inv_idx

    def _calculate_idf(self, term):
        """
        Calculates IDF for a term through this directory.
        If the term is not in the inverted index, returns 0.
        """

        if term not in self._invidx:
            return 0

        return math.log(self._doc_count / len(self._invidx[term]))

    def search(self, terms):
        """
        Performs search of term(s) specified in str terms and then
        provides list of documents that had a non-zero
        tf-idf value in descending order.
        If the term wasn't found, then returns None.
        """

        # Ensures lower casing and splits the words into a list.
        terms = terms.lower()
        terms = terms.split()

        tup_dict = {}
        # Iterates through each term to calculate idf
        # and tf, calls term_frequency from Document.
        for term in terms:

            idf = self._calculate_idf(term)

            # Iteration through listDoc so we can use term_frequency.
            idx = 0
            for doc in self._listDoc:
                file_name = self._listdir[idx]
                tf = doc.term_frequency(term)
                tf_idf = tf * idf

                # first stores list of tuples as a dictionary so we
                # can add tf_idf terms to values
                # I decided to have this switch to a tuple later
                # so I can actually sort them in a list.
                if file_name not in tup_dict:
                    tup_dict[file_name] = tf_idf
                else:
                    tup_dict[file_name] += tf_idf
                idx += 1

        # Converts dictionary to a list of tuples, then
        # sorts in descending order of second value.
        sort_tup = sorted(list(tup_dict.items()),
                          key=lambda x: x[1], reverse=True)

        sorted_list = []

        # Checks for non-zero values and stores associated file name.
        for tup in sort_tup:
            if tup[1] != 0:
                sorted_list.append(self._dirname + tup[0])

        if len(sorted_list) == 0:
            return None

        return sorted_list
