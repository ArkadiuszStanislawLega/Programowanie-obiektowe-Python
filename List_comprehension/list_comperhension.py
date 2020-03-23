def is_prime(n):
    """
    Algorytm przerobiony z https://maturka.it/algorytmy/python-sprawdzanie-czy-liczba-jest-liczba-pierwsza/

    Arguments:
        n {int} -- liczba która jest sprawdzana

    Returns:
        boolean -- True - jeżeli podana cyfra w argumencie jest pierwsza
    """
    # jeśli to dwójka, to liczba jest pierwsza.
    if n == 2:
        return True

    # jeśli liczba jest parzysta lub mniejsza bądź równa 1, to na pewno nie jest pierwsza.
    if n % 2 == 0 or n <= 1:
        return False
    # sprawdzam czy ma pdzielniki zaokrąglone w dół
    square_root = int(n**0.5) + 1
    for divider in range(3, square_root, 2):
        if n % divider == 0:
            return False
    return True


def main():
    lista = list(range(20))
    print([liczba**2 for liczba in lista if is_prime(liczba)])


if __name__ == "__main__":
    main()
