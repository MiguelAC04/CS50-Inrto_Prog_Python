def main() -> None:
    operation = input('Opperation>> ')
    operators = ('+', '-', '*', '/')
    op_parts = operation.split()
    intersection = lambda l1, l2: list(set(l1).intersection(l2))
    for part in op_parts:
        if (op := intersection(part, operators)):
            check_values(part, op)


def check_decimal(num):
    return num.replace('.', '', 1).isdigit()


def check_values(action, operator):
    values = action.split(operator)
    if x:=map(check_decimal, values):
        pass
    print(x)
    # return values.replace('.', 1)
if __name__ == "__main__":
    main()
