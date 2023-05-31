# bullet point adder - adds Wikipidea bullet points to the start of each line of
# text on the clipboard

# use in tandem with mclip.py

import pyperclip
text = pyperclip.paste()
text = 'Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'

# separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
print(text)
pyperclip.copy(text)


