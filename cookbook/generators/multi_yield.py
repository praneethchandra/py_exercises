def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str

multi_obj = multi_yield()
print(next(multi_obj))
print(next(multi_obj))
'''
unless yield is infinite you can iterate 
throug it one time only. Once all values have 
been evaluated, iteration will stop and the for 
look will exit
'''
try:
    print(next(multi_obj)) 
except StopIteration as e:
    print(f"Caught StopIteration: {e}")


letters = ["a", "b", "c", "d", "e"]
it = iter(letters)

while True:
    try:
        letter = next(it)
    except StopIteration:
        print(f"Caught StopIteration break.")
        break
    print(letter)