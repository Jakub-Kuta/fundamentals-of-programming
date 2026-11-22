###
# Functions to operate on a text
#
def count_words(text):
    return len(text.split())

def words_longest_first(text):
    return sorted(text.split(), key=len, reverse=True)

def words_alphabetical(text):
    return sorted(text.split(), key=str.lower)
