###
# Translates words from English to Polish
#
translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

word = input('Enter a word in English: ').lower()
if word in translations:
    print(f'{word} - {translations[word]}')
else:
    print('Translation is unavailable')
