import numpy as np
p = (4,5)
x, y = p
print('p: ', p, 'x: ', x, 'y: ', y)


data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(f'data: {data}, name: {name}, shares: {shares}, price: {price}, date: {date}')

name, shares, price, (year, mon, day) = data
print(f'data: {data}, name: {name}, shares: {shares}, price: {price}, year: {year}, mon: {mon}, day: {day}')

s = 'Hello'
a, b, c, d, e = s
print(f's: {s}, a: {a}, b: {b}, c: {c}, d: {d}, e: {e}')

_, shares, price, _ = data
print(f"data: {data}, shares: {shares}, price: {price}")

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