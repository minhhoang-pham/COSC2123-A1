from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import bisect


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Array-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ArrayDictionary(BaseDictionary):

    def __init__(self):
        self.array_dictionary = list()
        pass


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        self.array_dictionary = words_frequencies


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        i = bisect.bisect_left(self.array_dictionary, word)
        if i != len(self.array_dictionary) and self.array_dictionary[i].word == word:
            return self.array_dictionary[i].frequency
        else:
            return 0


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        if self.search(word_frequency.word) == 0:
            bisect.insort(self.array_dictionary, word_frequency)
            return True
        else:
            return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # find the position of 'word' in the list, if exists, will be at idx-1
        i = bisect.bisect_left(self.array_dictionary, word)
        if i != len(self.array_dictionary) and self.array_dictionary[i].word == word:
            self.array_dictionary.remove(i)
            return True
        else:
            return False


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """

        autocomplete_list = list()

        i = 0
        while prefix_word not in self.array_dictionary:
            i += 1

        if i != len(self.array_dictionary):
            while prefix_word in self.array_dictionary:
                autocomplete_list.append(self.array_dictionary[i])
                i += 1

        sorted_autocomplete_list = sorted(autocomplete_list, key=lambda word: word.frequency, reverse=True)

        return sorted_autocomplete_list
