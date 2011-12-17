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
#        children = self.spellingDictionary.dictionary.children(stem)
#        nextLetters = children.keys();
        print "stem = ", stem, " unused letters = ", unusedLetters
        #apparent children/keys is worthless and only gets immediate children with results ie dict.children('to') 
        #doesn't give us the 'a' becuase 'toa' isn't a word
        for nextLetter in unusedLetters:
            #is stem+nextLetter a word?
            try:
                newWord = self.spellingDictionary.dictionary[stem + nextLetter]
                words.append(newWord)
            except KeyError:
                #nop
                print()
            except NeedMore:
                #nop
                print()
        
            #brute force!
            #create new stem, remove letter from unused letter, infinite recursion!
            newUnusedLetters = list(unusedLetters)
            newUnusedLetters.remove(nextLetter)
            newStem = stem + nextLetter
            if newUnusedLetters != None:
                #recursion!
                print "recursion"
                words.extend(self.findWords(newStem, newUnusedLetters))    
        return words;

    def execute(self, tiles):
        wordList = []
        print "tiles = ", tiles
        for letter in tiles:
            unusedLetters = list(tiles)
            unusedLetters.remove(letter)
            print"calling findWords with ", letter, " ", unusedLetters
            foundWords = self.findWords(letter, unusedLetters)
            wordList.extend(foundWords)
        return wordList
    
def testToad():
    wordFinder = WordFinder()
    words = wordFinder.execute(["t", "o", "a", "d"])
    print "words: "
    for word in words:
        print word
        
def testLettersT():
    wordFinder = WordFinder()
    words = wordFinder.findWords('t', ['o','a','d'])
    print "words: "
    for word in words:
        print word

def printTOAD():
    wordFinder = WordFinder()
    print wordFinder.spellingDictionary.dictionary['t']
    print wordFinder.spellingDictionary.dictionary['to']
    print wordFinder.spellingDictionary.dictionary['toa']    
    print wordFinder.spellingDictionary.dictionary['toad']

def printTOADChildren():
    wordFinder = WordFinder()
    print wordFinder.spellingDictionary.dictionary.children('t')
    print wordFinder.spellingDictionary.dictionary.children('to')
    print wordFinder.spellingDictionary.dictionary.children('toa')    
    print wordFinder.spellingDictionary.dictionary.children('toad')
    
    
testToad()