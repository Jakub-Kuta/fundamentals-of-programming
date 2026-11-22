###
# Uses the functions from the MyText module
#
import MyText

text = 'An apple a day keeps the doctor away'

print('Text:', text)
print('Number of words:', MyText.count_words(text))
print('Words from the longest:', ','.join(MyText.words_longest_first(text)))
print('Words ordered alphabetically:', ','.join(MyText.words_alphabetical(text)))
