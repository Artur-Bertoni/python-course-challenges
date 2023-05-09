# BMI Calculation - Body Mass Index

"""
What is your height in cm:
What is your weight in kg:
"""

# LESS THAN 18.5        THINNESS
# BETWEEN 18.5 AND 24.9 NORMAL
# BETWEEN 25.0 AND 29.9 OVERWEIGHT
# BETWEEN 30.0 E 39.9   OBESITY
# GREATER THAN 40.0     SEVERE OBESITY

from math import pow

height = float(input('What is your height in cm: '))
weight = float(input('What is your weight in kg: '))

bmi = weight / pow((height / 100), 2)
status = ''

if bmi < 18.5:
    status = 'thinness'
elif 18.5 <= bmi <= 24.9:
    status = 'normal'
elif 25 <= bmi <= 29.9:
    status = 'overweight'
elif 30 <= bmi <= 39.9:
    status = 'obesity'
else:
    status = 'severe obesity'

print(f'You\'re with {status}')
