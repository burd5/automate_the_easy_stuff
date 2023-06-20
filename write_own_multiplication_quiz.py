# Write Your Own Multiplication Quiz
import random, time
"""
To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project on your own without importing it. This program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9. You’ll need to implement the following features:

If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
The user gets three tries to enter the correct answer before the program moves on to the next question.
Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the correct answer after the 8-second limit.
"""

numberOfQuestions = 10
correctAnswers = 0

for i in range(numberOfQuestions):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)

    product = num1 * num2

    print(f'{i}. {num1} X {num2}')
    