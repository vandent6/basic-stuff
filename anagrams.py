"""
Anagrams are words that can be spelled using the
same letters found in other words.
"""

wordList = ["pass","spas","saps","asps"]

def anagrams(word, duplicates=False):
    """
    (str, bool) -> list(str)
    Given a word, returns all anagrams, by default will not return duplicates.
    """
    retList = []
        if len(word) < 2:
        retList.append(word)
        return retList

    tempWord = word[1:len(word)]
    
    for char in word:
        
        for innerWord in anagrams(tempWord):

            if duplicates == False:
                if retList.count(char + innerWord) == 0:
                    retList.append(char + innerWord)
            else:
                retList.append(char + innerWord)

                
        tempWord = tempWord[1:len(word)]
        tempWord = tempWord + char
        
    return retList


def find_anagrams(word, words, duplicates=False):
    """
    (str, list, bool) -> list(str)
    Given a word and a list of words, will find the anagrams from the list.
    Will not find duplicates by default.
    """
    anasList = []
    for anas in anagrams(word, duplicates):
        if words.count(anas) > 0:
            anasList.append(anas)

    return anasList



print(find_anagrams("pass",wordList,False))
