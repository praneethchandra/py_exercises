import cProfile
import timeit

def csv_reader_using_return(file_name):
    file = open(file_name, "r")
    result = file.read().split("\n")
    return result

def csv_reader_using_yield(file_name):
    for row in open(file_name, "r"):
        yield row

def read_using_return():
    csv_gen = csv_reader_using_return("/home/pkgone/py_exercises/files/gender_statistics.csv")
    row_count = 0

    for row in csv_gen:
        row_count += 1

    print(f"Row count is {row_count}")

def read_using_yield():
    csv_gen = csv_reader_using_yield("/home/pkgone/py_exercises/files/gender_statistics.csv")
    row_count = 0

    for row in csv_gen:
        row_count += 1

    print(f"Row count is {row_count}")


def main():
    timeit.timeit("read_using_return()", number=1, setup="from __main__ import read_using_return")
    timeit.timeit("read_using_yield()", number=1, setup="from __main__ import read_using_yield")


if __name__ == '__main__':
    cProfile.run('main()')
    # main()








