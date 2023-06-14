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
