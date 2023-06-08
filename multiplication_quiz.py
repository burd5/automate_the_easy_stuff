
# Multiplication Quiz

import pyinputplus as pyip
import random, time

numberOfQuestions = 11
correctAnswers = 0

for questionNumber in range(1, numberOfQuestions):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    prompt = f'{questionNumber}: {num1} X {num2} = '
    sum = num1 * num2
    try:
        pyip.inputStr(prompt, allowRegexes=[rf'^{sum}$'],
                      blockRegexes=['.*', 'Incorrect!'],
                      timeout=8,
                      limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)

print(f'Score: {correctAnswers}/{numberOfQuestions - 1}')