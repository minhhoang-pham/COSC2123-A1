from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import re
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
        self.array_dictionary = sorted(self.array_dictionary, key=lambda a: a.word)


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """

        # perform binary search
        left = 0
        right = len(self.array_dictionary) - 1
        while left <= right:
            mid = left + (right - left) // 2

            # search for the word then return its frequency
            if self.array_dictionary[mid].word == word:
                return self.array_dictionary[mid].frequency

            elif self.array_dictionary[mid].word < word:
                left = mid + 1

            else:
                right = mid - 1

        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        index = len(self.array_dictionary)
        # Searching for the position
        for i in range(len(self.array_dictionary)):
            if self.array_dictionary[i].word == word_frequency.word:
                return False
            if self.array_dictionary[i].word > word_frequency.word:
                index = i
                break

        # Inserting n in the list
        if index == len(self.array_dictionary):
            self.array_dictionary = self.array_dictionary[:index] + [word_frequency]
        else:
            self.array_dictionary = self.array_dictionary[:index] + [word_frequency] + self.array_dictionary[index:]

        return True



    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # find the position of 'word' in the list, if exists, will be at idx-1

        # perform binary search
        left = 0
        right = len(self.array_dictionary) - 1
        while left <= right:
            mid = left + (right - left) // 2

            # look for the word to delete
            if self.array_dictionary[mid].word == word:
                # delete word from list
                del self.array_dictionary[mid]
                return True

            elif self.array_dictionary[mid].word < word:
                left = mid + 1

            else:
                right = mid - 1
        return False


    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """

        # list to store the autocompleted words
        autocomplete_list = list()
        # pattern for regex matching
        pattern = '^'+prefix_word

        # traverse the array then find the prefix matches and append them to the new list
        for i in range(len(self.array_dictionary)):
            if re.match(pattern, self.array_dictionary[i].word):
                autocomplete_list.append((self.array_dictionary[i]))

        # sort the autocomplete list
        sorted_autocomplete_list = sorted(autocomplete_list, key=lambda word: word.frequency, reverse=True)
        # delete everything except the top 3 values
        del sorted_autocomplete_list[3:]

        return sorted_autocomplete_list
