import numpy as np
grades = (10, 20, 45,62, 17,18, 20)

def drop_first_last(grades):
    first, *middle, last = grades
    return np.average(middle)

print(drop_first_last(grades))

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(f'record: {record}, name: {name}, email: {email}, phone_numbers: {phone_numbers}')

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(f'trailing: {trailing}, current: {current}')