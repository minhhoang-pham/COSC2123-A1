import re

from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


class ListNode:
    '''
    Define a node in the linked list
    '''

    def __init__(self, word_frequency: WordFrequency):
        self.word_frequency = word_frequency
        self.next = None

# ------------------------------------------------------------------------
# This class  is required TO BE IMPLEMENTED
# Linked-List-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class LinkedListDictionary(BaseDictionary):

    def __init__(self):
        self.head = None
        pass


    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        current_node = ListNode(words_frequencies[0])
        self.head = current_node

        for i in words_frequencies[1:]:
            temp = ListNode(i)
            current_node.next = temp
            current_node = temp


    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        current_node = self.head

        while current_node is not None:
            if current_node.word_frequency.word == word:
                return current_node.word_frequency.frequency

            current_node = current_node.next

        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        # check if the word appears in the linked list
        if self.search(word_frequency.word) > 0:
            return False
        else:
            # create new node, set the new node's next to the head
            # point the head to the new node
            new_node = ListNode(word_frequency)
            new_node.next = self.head
            self.head = new_node
            return True


    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_node.word_frequency.word == word:
                # when the deleted node is the head
                if current_node == self.head:
                    self.head = current_node.next
                    return True

                # when the deleted node is the last node
                if current_node.next is None:
                    previous_node.next = None
                    return True

                # when the deleted node is in the middle
                else:
                    previous_node.next = current_node.next
                    return True

            previous_node = current_node
            current_node = current_node.next

        return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        # set the head as the current node
        current_node = self.head
        # create a list to store the autocomplete words
        autocomplete_list = list()
        # regex to match the prefix word
        pattern = "^" + word

        # traverse the linked list and match the regex
        while current_node is not None:
            if re.match(pattern, current_node.word_frequency.word):
                # if matched then add the word frequency object to the list
                autocomplete_list.append(current_node.word_frequency)

            current_node = current_node.next

        # sort the list by frequency
        sorted_autocomplete_list = sorted(autocomplete_list, key=lambda word: word.frequency, reverse=True)

        # only trim off objects when there are more than 3
        if len(sorted_autocomplete_list) > 3:
            # delete from 3 beyond
            del sorted_autocomplete_list[3:]

        return sorted_autocomplete_list


#         Code for testing
#         print(self.head.word_frequency.word)
#         current_node = self.head
#
#         while True:
#             if current_node.next is not None:
#                 print(current_node.word_frequency.word + " Next: " + current_node.next.word_frequency.word)
#                 current_node = current_node.next
#             else:
#                 break
#         print(current_node.word_frequency.word)

