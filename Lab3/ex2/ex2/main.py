from stack import Stack, ExpandedStack


def main():
    stack = ExpandedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.min_value()

    while not stack.is_empty():
        print(stack.top())
        stack.pop()


if '__main__' == __name__:
    main()
