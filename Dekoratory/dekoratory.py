from functools import wraps
import datetime

meesages_list = []


def add_message_to_list(func):
    @wraps(func)
    def add_message(message: str):
        time = datetime.datetime.now()
        add_message.counter += 1
        meesages_list.append(f'{time.strftime("%d-%m-%Y %X")} - {message}')
        print(f'Użyto dekorator {add_message.counter} raz')
        return func(message)

    add_message.counter = 0
    return add_message


@add_message_to_list
def message(message: str):
    print(meesages_list[-1::][0])


def main():
    message("Pierwsza wiadomość.")
    message("Druga wiadomość.")
    message("Trzecia wiadomość.")
    print(f'Ilość wpisów w logu: {len(meesages_list)}')


if __name__ == '__main__':
    main()
