# Mad Libs 

"""
Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.

The program would find these occurrences and prompt the user to replace them.

Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck

The following text file would then be created:

The silly panda walked to the chandelier and then screamed. A nearby pickup
truck was unaffected by these events.

The results should be printed to the screen and saved to a new text file.

"""
import re
mad_text = open('mad_text.txt', 'r')
mad_libs = mad_text.read()
print(mad_libs)

def madLibs(text):
    speech = 'ADJECTIVE|NOUN|ADVERB|VERB'
    inputs = list(re.findall(speech, text))
    for word in inputs:
        filler = input(f'Enter a {word.lower()}:\n')
        text = text.replace(word, filler, 1)
    file_name = input('Please name the new file for your completed mad libs: \n')
    mad_libs_translated_file = open(f'{file_name}.txt', 'w')
    mad_libs_translated_file.write(mad_libs)
    mad_libs_translated_file.close()
    mad_text.close()
    return text

print(madLibs(mad_libs))

