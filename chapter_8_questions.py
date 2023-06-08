# Chapter 8 - Input Validation Questions
"""
1. Does PyInputPlus come with the Python Standard Library?

No

2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?

So you don't have to write out pyinputplus everytime

3. What is the difference between inputInt() and inputFloat()?

The inputInt() function returns an int value, while the inputFloat() function returns a float value. This is the difference between returning 4 and 4.0

4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?

Call pyip.inputint(min=0, max=99)

5. What is passed to the allowRegexes and blockRegexes keyword arguments?

Regex strings

6. What does inputStr(limit=3) do if blank input is entered three times?

RetryLimitException error

7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?

returns the string 'Hello'

"""