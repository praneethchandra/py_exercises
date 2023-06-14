items = [1, 10, 7, 4, 5, 9]

head, *tail = items
print(f'head: {head}. tail: {tail}')

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))