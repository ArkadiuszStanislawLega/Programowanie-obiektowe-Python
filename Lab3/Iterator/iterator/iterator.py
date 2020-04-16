class Counter:
    def __init__(self, func):
        self.__func = func
        self.__counter = 0

    def __call__(self, *args, **qwargs):
        self.__counter += 1
        print(f'{self.__counter}. ', end="")
        return self.__func(self, *args, **qwargs)


@Counter
def printing(self):
    print("Fibbonacci: ", end="")


class FibonacciIterator():
    def __init__(self, max_val):
        self.__a = 0
        self.__b = 1
        self.__counter_to_2 = 0
        self.__max_val = max_val

    def __iter__(self):
        return self

    def __next__(self):
        printing()
        if self.__counter_to_2 >= 0 and self.__counter_to_2 < 2:
            self.__counter_to_2 += 1
            return self.__counter_to_2 - 1
        else:
            self.__b = self.__a + self.__b
            self.__a = self.__b - self.__a

        if self.__b >= self.__max_val:
            print("Koniec")
            raise StopIteration
        return self.__b


def main():
    fib = FibonacciIterator(200000000)
    it = iter(fib)
    for f in it:
        print(f)


if __name__ == "__main__":
    main()
