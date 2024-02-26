def main() -> None:
    operation = input('Opperation>> ')
    operators = ('+', '-', '*', '/', 'x')

    intersection = lambda L1, L2: list(set(L1).intersection(L2))

    if (op := intersection(operation, operators)):
        valid_values(operation, op)
    else:
        exit('Not a operation')


def check_decimal(num: str) -> bool:
    '''Checks whether numbers with decimal point or commas are valid'''
    int_part, decimal_part = num.split('.', 1)
    if int_part < 3:
        return num.replace('.', '', 1).isdigit()




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
