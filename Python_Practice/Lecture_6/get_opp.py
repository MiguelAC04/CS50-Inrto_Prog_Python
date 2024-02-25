def main() -> None:
    operation = input('Opperation>> ')
    operators = ('+', '-', '*', '/', 'x')
    op_parts = operation.split()

    intersection = lambda l1, l2: list(set(l1).intersection(l2))

    for part in op_parts:
        if (op := intersection(part, operators)):
            check_values(part, op)
        print(set(part))


def check_decimal(num):
    return num.replace('.', '', 1).isdigit()


def check_values(action, operator):
    values = action.split(operator[0])
    for x in list(map(check_decimal, values)):
        print(x)

    # if x:=):
    #     pass
    # print(x[0])
    # return values.replace('.', 1)
if __name__ == "__main__":
    main()
