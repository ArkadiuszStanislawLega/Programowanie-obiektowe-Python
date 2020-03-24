def main():
    try:
        with open("lorem_ipsum.txt", "r", encoding='UTF-8') as file:
            print(f'Ilość wyrazów w pliku: {len(file.readlines()[0].split())}')
    except FileNotFoundError:
        print("Nie znaleziono pliku.")


if __name__ == "__main__":
    main()
