ANAGRAM_LIST = ['spas', 'pass', 'saps', 'asps']


def get_rotations(word):
    rotations = []

    if len(word) < 2:
        return word

    tempWord = word
    for char in word:
        tempWord = tempWord[1:len(word)]
        for ana in get_rotations(tempWord):
            rotations.append(char + ana)
            
        tempWord = tempWord + char

    return rotations
    

def compare_list(anaWord, wordList):
    anagrams = []
    
    for anas in get_rotations(anaWord):
        if anas in wordList and anagrams.count(anas) == 0:
            anagrams.append(anas)

    return anagrams
            


print(compare_list('pass',ANAGRAM_LIST))

            
