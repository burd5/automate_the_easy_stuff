# Regex version of the strip() method
import re
"""
Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.

"""

stripRegex = re.compile(r'(^\s*)|(\s*$)')

print(re.sub(stripRegex, '', '   sjsjs js  sjsjd      '))