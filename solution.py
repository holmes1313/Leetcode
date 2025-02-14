"""
A
Aniseed  3
Apple 23,54
Arrowroot 19
B
Banana 24,93,120
Boiling 122
Bread 124,125
Bundt 123
D
Duck 122


"""
import collections

class Solution:
    def __init__(self):
        self.index_to_words = collections.defaultdict(set)
        self.word_to_pages = collections.defaultdict(set)

    def store_index ( self, word: str, page: int ):
        index = word[0].upper()
        self.index_to_words[index].add(word)
        self.word_to_pages[word].add(page)
    
    def print_index( self ):
        for index in sorted(self.index_to_words.keys()):
            print(index)
            for word in sorted(self.index_to_words[index]):
                print(word)
                print(sorted(self.word_to_pages[word]))

                
        
