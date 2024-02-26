def main() -> None:
    operation = input('Opperation>> ')
    operators = ('+', '-', '*', '/', 'x')

    intersection = lambda L1, L2: list(set(L1).intersection(L2))

    if (op := intersection(operation, operators)):
        if valid_values(operation, op):
            evaluate(operation)
    else:
        exit('Not a operation')


def evaluate(operation: str) -> None:
    try:
        eval('123*1a')
        

def check_decimal(num: str) -> bool:
    '''Checks whether numbers with decimal point or commas are valid'''
    match num.split('.', 1):
        case int_part, decimal_part:
            if int_part > 3:
                i = 0
                for _ in int_part.count(','):
                    if not (j := int_part.find(',', i))%3:
                        return False
                    i = j + 1
            return int_part.isdigit() and decimal_part.isdigit()
        case decimal:
            return decimal.isdigit()


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
