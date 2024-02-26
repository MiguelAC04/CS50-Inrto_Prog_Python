def main() -> None:
    operation = input('Opperation>> ')
    operators = ('+', '-', '*', '/', 'x')
    op_parts = operation.split()

    intersection = lambda l1, l2: list(set(l1).intersection(l2))

    for part in op_parts:
        if (op := intersection(part, operators)):
            valid_values(part, op)
        print(set(part))


def check_decimal(num):
    return num.replace('.', '', 1).isdigit()


def get_values(action: list[str], operators: list[str]) -> list[str]:
    for op in operator:
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
