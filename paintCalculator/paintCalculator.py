# Functions Challenge

"""
Create a program that calculates the amount of paint needed to
paint a wall. The user must provide the following information: Performance, height and width.
The program should display the message 'You need x cans of paint' on the screen.
"""

performance = float(input('Insert the performance of the bucket (m²): '))
height = float(input('Insert the height of the wall (m): '))
width = float(input('Insert the width of the wall (m): '))


def calc_amount_of_paint():
    return (height * width) / performance


print(f'You need {calc_amount_of_paint()} cans of paint')
