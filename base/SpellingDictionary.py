from datastructure.trie import Trie
class SpellingDictionary:
    def __init__(self):
        self.dictionaryFile = "en_US.dic"
        self.dictionary = Trie()
    def populateDictionary(self):
        file = open(self.dictionaryFile);
        rawWords = []
        for line in file:
            rawWords.append(line)
        for rawWord in rawWords:
            word = self.readWord(rawWord)
            self.dictionary[word] = word;
            #print word;
        
    def readWord(self, wordLine):
        index = wordLine.find('/')
        if index <0:
            #print "no /"
            #get rid of the trailing newline
            return wordLine[0:len(wordLine)-1]
        actualWord = wordLine[0:index]
        return actualWord;
        