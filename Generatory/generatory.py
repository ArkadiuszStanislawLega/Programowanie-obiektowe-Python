def fibonacci(n):
    """
    Przerobiony algorytm z http://www.algorytm.edu.pl/algorytmy-maturalne/ciag-fibonacciego.html
    Arguments:
        n {int} -- ilość cyfr do wygenerowania

    Yields:
        int -- kolejne cyfry z ciągu fobbinacciego
    """
    a = 0
    b = 1
    for i in range(n):
        b = a + b
        a = b-a
        yield a


def main():
    for item in fibonacci(11):
        print(item)


if __name__ == "__main__":
    main()
