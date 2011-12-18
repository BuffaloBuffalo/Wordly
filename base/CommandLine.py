from base.WordFinder import WordFinder
from base.ResultsManipulator import ResultsManipulator
print "Welcome to Wordly"
print "Valid entry methods are space or comma delimited, or none at all, for example: 'aartgfd', 'a a r t g f d', or 'a,a,r,t,g,f,d' "
print "Enter your tiles:"

stringTiles = raw_input( )

STRIPPED_CHARACTERS=[","," ", ";",":","!","@","#","$","%","^","&","*","(",")","-","_","[","]","{","}","\\","|", "\"","'",".","/","?"]
STRIPPED_NUMS =["1","2","3","4","5","6","7","8","9","0"]

badCharacters = list(STRIPPED_NUMS)
badCharacters.extend(STRIPPED_CHARACTERS)
print badCharacters
sanitizedTiles = stringTiles.lower()
for character in badCharacters:
    sanitizedTiles=sanitizedTiles.replace(character,"")
    
print "Interpreted your tiles as: ",sanitizedTiles

wordFinder =  WordFinder()
words = wordFinder.execute(list(sanitizedTiles))

manip = ResultsManipulator(words)
sortedWords = manip.sortByLengthDesc()
for word in sortedWords:
    print word