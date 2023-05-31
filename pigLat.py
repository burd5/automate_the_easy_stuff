# English to Pig Latin

print('Enter a message to be converted into Pig Latin: ')
# receives user message to be translated
message = input()

# list of vowels
VOWELS = 'aeiouy'

# variable to store converted words
pigLatin = []

for word in message.split():
    # separate non-letters at beginning of word
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # separate non-letters at end of the word
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters = word[-1] + suffixNonLetters
        word = word[:-1]
    if len(word) == 0:
        pigLatin.append(suffixNonLetters)
        continue

    # store case of original word
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()

    # separate the consonants
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # return word back to original case
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # final step - Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

# Join all the words back together into a single string:
print(' '.join(pigLatin))

