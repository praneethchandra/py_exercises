from collections import defaultdict
from collections import OrderedDict
import json

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

dset = defaultdict(set)
dset['a'].add(1)
dset['a'].add(2)
dset['b'].add(4)

print(dset)

d = {}
for key,value in dset.items():
    if key not in d:
        d[key] = []
    d[key].append(value)

print(d)

dict_default = defaultdict(list)
for key, value in dset.items():
    dict_default[key].append(value)

print(dict_default)

dord = OrderedDict()
dord['foo'] = 101
dord['bar'] = 200
dord['spam'] = 300
dord['grok'] = 4

for key in dord:
    print(key, dord[key])

print(json.dumps(dord))

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

'''
zip iteration can be used only once, if used more than once it throws ValueError
'''
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
try:
    print(max(prices_and_names))
except Exception as e:
    print(e)

'''
This will sort key names by default
'''
print(min(prices))
print(max(prices))

'''
for sorting based on prices in above example
'''
print(min(prices.values()))
print(max(prices.values()))


print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))

print(prices[min(prices, key=lambda k: prices[k])])


sim_prices = {'AAA': 45.23, 'ZZZ': 45.23}
min(zip(sim_prices.values(), sim_prices.keys()))

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print(f'a: {a}, b: {b}')

print(f'a.keys() & b.keys(): {a.keys() & b.keys()}')

print(f'a.keys() - b.keys(): {a.keys() - b.keys()}')

print(f'a.items() & b.items(): {a.items() & b.items()}')

c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(f'a.keys() - z, w: {c}')


