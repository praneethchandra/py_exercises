import sys

num_squared_lc = [num**2 for num in range(10000)]
num_squared_gc = (num**2 for num in range(10000))

print(f"num_squared_lc: {num_squared_lc}, size: {sys.getsizeof(num_squared_lc)}")
print(f"num_squared_gc: {num_squared_gc}, size: {sys.getsizeof(num_squared_gc)}")

for i in num_squared_gc:
    print(i, end=" ")


'''
If speed is an issue and memory isn't then a list comprehension is likely better tool for the job.
'''
import cProfile

cProfile.run('sum([i*2 for i in range(10000)])')
cProfile.run('sum((i*2 for i in range(10000)))')