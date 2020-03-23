from functools import wraps
import datetime

log = []


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time = datetime.datetime.now()
        for i in args:
            log.append(f'{time.strftime("%d-%m-%Y %X")} - {i}')
        return func(*args, **kwargs)
    return wrapper


@my_decorator
def message(message):
    print(log[-1::][0])


def main():
    message("First message.")
    message("Second messaage.")
    message("Third message.")
    print(f'Ilość wpisów w logu: {len(log)}')


if __name__ == '__main__':
    main()
