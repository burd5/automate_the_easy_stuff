# Date Detection Project - Chapter 7
import re
"""
Assume that the days range from 01 to 31, the months range from 01 to 12, and 
the years range from 1000 to 2999. Note that if the day or month is a single 
digit, it’ll have a leading zero.

"""
# Create regex expressions to identify correct date format DD/MM/YYYY

def isFormat():
    date = input('Enter a date in the following format - DD/MM/YYYY: ')

    date_regex = re.compile(r'^(\d{2})/(\d{2})/(\d{4})$')
    string = re.search(date_regex, date)
    try:
        month = string.group(1)
        day = int(string.group(2))
        year = int(string.group(3))
        return isValidDate(month,day,year)
    except:
        print('Incorrect format.Try again.')
        return isFormat()


# Check to see if the variables are valid - return True/False. 
"""

April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400.

"""
_30_months = ['04', '06', '09', '11']

other_months = ['01', '02', '03', '05', '07', '08', '10', '12']

def isValidDate(month,day,year):
    if year >= 1000 and year <= 2999:
        if month == '02':
            if year % 400 == 0:
                if day > 29:
                    return 'Not a valid date.'
            elif day > 28:
                return 'Not a valid date.'
        elif month in _30_months:
            if day > 30:
                return 'Not a valid date.'
        elif month in other_months:
            if day > 31: return 'Not a valid date.'
        elif month not in other_months or month not in _30_months: return 'Not a valid date.'
    elif year > 2999: return 'Not a valid date.'
    return 'Valid date.'

print(isFormat())