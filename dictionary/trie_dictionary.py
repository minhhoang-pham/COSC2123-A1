from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED
# Trie-based dictionary implementation
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


# Class representing a node in the Trie
class TrieNode:

    def __init__(self, letter=None, frequency=None, is_last=False):
        self.letter = letter            # letter stored at this node
        self.frequency = frequency      # frequency of the word if this letter is the end of a word
        self.is_last = is_last          # True if this letter is the end of a word
        self.children: dict[str, TrieNode] = {}     # a hashtable containing children nodes, key = letter, value = child node


class TrieDictionary(BaseDictionary):

    def __init__(self):
        self.root = None
        pass

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        self.root = TrieNode(None, None, False)
        current_node = self.root

        # check each word in words frequencies
        for word_frequency in words_frequencies:
            # check each letter in the word
            for index, letter in enumerate(word_frequency.word):
                # check if the letter doesn't exist in children
                if letter not in current_node.children.keys():
                    # check if the letter is the last letter in the word for the boolean value
                    if index == len(word_frequency.word)-1:
                        # if it is the last letter then add that letter and TrieNode to the children dict with
                        # a frequency and is_last = True
                        current_node.children[letter] = TrieNode(letter, word_frequency.frequency, True)
                    else:
                        # if not the last letter then add that letter and TrieNode to the children dict with
                        # none frequency and is_last = False
                        current_node.children[letter] = TrieNode(letter, None, False)
                # the letter exists in children
                else:
                    # the letter is the last letter then add the word frequency and change is_last to True
                    if index == len(word_frequency.word)-1:
                        current_node.children[letter].frequency = word_frequency.frequency
                        current_node.children[letter].is_last = True

                current_node = current_node.children[letter]

            current_node = self.root

        # for i in self.root.children:
        #     print(self.root.children[i].letter)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """

        end_node = self.node_search(word)
        # print(end_node.letter, end_node.is_last)
        if end_node.is_last and end_node.frequency is not None:
            return end_node.frequency

        return 0


    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """

        # if search returns a frequency then the word is already added
        if self.search(word_frequency.word) > 0:
            return False

        current_node = self.root

        # traverse through each letter of the word
        for index, letter in enumerate(word_frequency.word):
            # check if the letter already exists
            if letter in current_node.children:
                # if it is the last letter then set the frequency and is last to indicate a new word
                if index == len(word_frequency.word)-1:
                    current_node.children[letter].frequency = word_frequency.frequency
                    current_node.children[letter].is_last = True
                    return True
                current_node = current_node.children[letter]

            else:
                # if the letter doesn't exist and isn't the last letter then add a node and go to it
                if index != len(word_frequency.word)-1:
                    current_node.children[letter] = TrieNode(letter, None, False)
                    current_node = current_node.children[letter]
                else:
                    current_node.children[letter] = TrieNode(letter, word_frequency.frequency, True)
                    return True

        return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """

        end_node = self.node_search(word)

        if end_node.is_last and end_node.frequency is not None:
            end_node.frequency = None
            end_node.is_last = False
            return True

        return False


    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """

        autocomplete_list = list()

        node = self.root

        for a in word:
            # no string in the Trie has this prefix
            if not node.children.get(a):
                return autocomplete_list
            node = node.children[a]

        # If prefix is present as a word, but
        # there is no subtree below the last
        # matching node.
        if not node.children:
            return autocomplete_list

        self.suggestions_rec(node, word, autocomplete_list)

        # sort the list by frequency
        sorted_autocomplete_list = sorted(autocomplete_list, key=lambda w: w.frequency, reverse=True)

        # # only trim off objects when there are more than 3
        if len(sorted_autocomplete_list) > 3:
            # delete from 3 beyond
            del sorted_autocomplete_list[3:]

        return sorted_autocomplete_list

    def suggestions_rec(self, node, word, ac_list):

        # Method to recursively traverse the trie
        # and return a whole word.
        if node.is_last:
            # print(word, self.search(word))
            ac_list.append(WordFrequency(word, self.search(word)))

        for a, n in node.children.items():
            self.suggestions_rec(n, word + a, ac_list)

        return ac_list

    def node_search(self, word: str) -> TrieNode:
        """
        return the node which holds the last letter of the word
        @param word: word to search for
        @return: a TrieNode which holds the last letter of the word, empty node if the word can't be found
        """

        current_node = self.root

        for letter in word:
            if letter in current_node.children:
                print(current_node.children[letter].letter, current_node.children[letter].is_last)
                current_node = current_node.children[letter]
            else:
                return TrieNode()

        return current_node
