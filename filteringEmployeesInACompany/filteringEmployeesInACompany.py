# 'Sets' Challenge

"""
Create a program that generates 3 lists according to the need below:

List1 = Employees who have a car and work at night
List2 = Employees who have a car and work during the day
List3 = Employees who do not have a car
"""

employees = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
dayWorkers = ['Ana', 'Marcos', 'Alice', 'Melissa']
nightWorkers = ['Pedro', 'Sophia', 'Bruno']
haveCar = ['Marcos', 'Alice', 'Bruno', 'Melissa']

list1 = set(haveCar).intersection(nightWorkers)
list2 = set(haveCar).intersection(dayWorkers)
list3 = set(employees).difference(haveCar)

print(f'Employees with a car that works at the nighttime: {list1}\n'
      f'Employees with a car that works at the daytime: {list2}\n'
      f'Employees without a car: {list3}')
