
def read_word_list_backwards(words):
    """
    (str) -> (str)
    Reverse order of words given.
    """
    retWord = ""
    for word in words.split(sep=' '):
        retWord = str(word) + ' ' + retWord 

    return retWord

def reverse_words(words):
    """
    (str) -> (str)
    Reverse order of words given.
    """
    return ' '.join(words.split()[::-1])
