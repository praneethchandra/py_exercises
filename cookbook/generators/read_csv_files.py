import cProfile
import timeit

FILE_NAME = "/home/pgone/py/py_exercises/files/gender_statistics.csv"

def csv_reader_using_return(file_name):
    file = open(file_name, "r")
    result = file.read().split("\n")
    return result

def csv_reader_using_yield(file_name):
    for row in open(file_name, "r"):
        yield row

def read_using_return():
    csv_gen = csv_reader_using_return(FILE_NAME)
    count_rows(csv_gen)

def read_using_yield():
    csv_gen = csv_reader_using_yield(FILE_NAME)
    count_rows(csv_gen)

def read_using_yield_comprehension():
    csv_gen = (row for row in open(FILE_NAME, 'r'))
    count_rows(csv_gen)


def count_rows(csv_gen):
    row_count = 0

    for row in csv_gen:
        row_count += 1

    print(f"Row count is {row_count}")    


def main():
    # timeit.timeit("read_using_return()", number=1, setup="from __main__ import read_using_return")
    # timeit.timeit("read_using_yield()", number=1, setup="from __main__ import read_using_yield")
    # timeit.timeit("read_using_yield_comprehension()", number=1, setup="from __main__ import read_using_yield")
    read_using_return()
    read_using_yield()
    read_using_yield_comprehension()


if __name__ == '__main__':
    cProfile.run('main()')
    # main()








