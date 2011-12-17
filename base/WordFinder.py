from base.SpellingDictionary import SpellingDictionary
from datastructure.trie import NeedMore
class WordFinder:
    def __init__(self):
        self.spellingDictionary = SpellingDictionary()
        #self.dictionary.add(["toad", "to", "do", "dot"])
        self.spellingDictionary.populateDictionary()
        print"Done building dictionary"

    def findWords(self, stem, unusedLetters):
        words = []
        children = self.spellingDictionary.dictionary.children(stem)
        nextLetters = children.keys();
        print "stem = ",stem," unused letters = ",unusedLetters," nextLetters = ",nextLetters
        for nextLetter in nextLetters:
            if nextLetter in unusedLetters:
                #remove nextLetter from unusedLetters (and make a copy)
                newUnusedLetters = list(unusedLetters)
                print newUnusedLetters
                newUnusedLetters.remove(nextLetter)
                newStem = stem + nextLetter
                
                print newUnusedLetters
                print newStem
                if newUnusedLetters !=None:
                    #recursion!
                    print "recursion"
                    words.extend(self.findWords(newStem, newUnusedLetters))    
                try:
                    newWord = self.spellingDictionary.dictionary[stem+nextLetter]
                    words.append(newWord)
                except KeyError:
                    #nop
                    print()
                except NeedMore:
                    #nop
                    print()
                    #how to handle case where the given stem is an actual word
        return words;


    def execute(self, tiles):
        wordList = []
        print "tiles = ",tiles
        for letter in tiles:
            unusedLetters = list(tiles)
            unusedLetters.remove(letter)
            print"calling findWords with ",letter," ",unusedLetters
            foundWords = self.findWords(letter, unusedLetters)
            wordList.extend(foundWords)
        return wordList



#how does the dictionary get bound to the word finding algorithm?
wordFinder = WordFinder()
#print wordFinder.spellingDictionary.dictionary['titte']
#words = wordFinder.execute(["t", "o", "a", "d"])

#words = wordFinder.findWords('t', ['o','a','d'])
#print "words: "
#for word in words:
#    print word
    
#print wordFinder.spellingDictionary.dictionary['t']
#print wordFinder.spellingDictionary.dictionary['to']
#print wordFinder.spellingDictionary.dictionary['toa']    
#print wordFinder.spellingDictionary.dictionary['toad']


print wordFinder.spellingDictionary.dictionary.children('t')
print wordFinder.spellingDictionary.dictionary.children('to')
print wordFinder.spellingDictionary.dictionary.children('toa')    
print wordFinder.spellingDictionary.dictionary.children('toad')
