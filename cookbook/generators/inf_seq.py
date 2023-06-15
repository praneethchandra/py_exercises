def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

def main():
    # to get finite sequence you can use range()
    a = range(5)
    print(list(a))

    # this would run until we stop it manually
    # for i in infinite_sequence():
    #     print(i, end=" ")

    gen = infinite_sequence()
    i = 0
    while i < 100:
        i = next(gen)
        print(i, end=" ")


if __name__ == "__main__":
    main()



