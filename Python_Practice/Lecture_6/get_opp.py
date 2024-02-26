def main() -> None:
    operation = input('Opperation>> ')
    global operators
    operators = ('+', '-', '*', '/', 'x')
    op_parts = operation.split()

    intersection = lambda L1, L2: list(set(L1).intersection(L2))

    for part in op_parts:
        if (op := intersection(part, operators)):
            valid_values(part, op)

        print(set(part))


def check_decimal(num):
    return num.replace('.', '', 1).replace(',', '').replace(',', '').isdigit()


def get_values(action: str, operators: list[str]) -> list[str]:
    for op in operators:
        action = ' '.join(action.split(op))
    return action.split()


def valid_values(action: str, operator: list[str]) -> bool:
    values = get_values(action, operator)

    for i, valid_n in enumerate(map(check_decimal, values)):
        if not valid_n:
            print('Non valid:', values[i])
            return False
    else: return True


if __name__ == "__main__":
    main()
