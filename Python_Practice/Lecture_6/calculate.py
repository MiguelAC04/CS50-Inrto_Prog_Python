'''
This program allows the user to prompt for an operation
in the terminal, and get the value.
Simply, it the same as:
try:
    eval(operation)
except SyntaxError as err:
    exit(err)
'''


def main(focus_oper: str | None = None) -> None:
    operation = input('Opperation>> ') if not focus_oper else focus_oper
    operators = ('+', '-', '*', '/', 'x')

    intersection = lambda L1, L2: list(set(L1).intersection(L2))

    if (oper := intersection(operation, operators)):
        if operation[-1] not in operators:
            if valid_values(operation, oper):
                evaluate(operation)
        else:
            exit('Missing value after operation')
    else:
        exit('Not a operation')


def evaluate(operation: str) -> None:
    '''Performs the given operaiton'''
    prep_op = operation.replace(',', '').replace('x', '*')
    print(operation+' =', eval(prep_op))



def check_decimal(num: str) -> bool:
    '''Checks whether numbers with decimal point or commas are valid'''
    match num.split('.', 1):
        case [int_part, decimal_part]:
            if int_part > 3:
                i = 0
                for _ in int_part.count(','):
                    if not (j := int_part.find(',', i)) % 3:
                        return False
                    i = j + 1
            return int_part.isdigit() and decimal_part.isdigit()
        case [decimal]:
            return decimal.isdigit()


def get_values(action: str, operators: list[str]) -> list[str]:
    '''Gets the numerical values present in an operation'''
    for oper in operators:
        action = ' '.join(action.split(oper))
    return action.split()


def valid_values(action: str, operator: list[str]) -> bool:
    '''Checks whether the numeric values in an operation are valid'''
    values = get_values(action, operator)

    for i, valid_n in enumerate(map(check_decimal, values)):
        if not valid_n:
            print('Non valid:', values[i])
            return False
    else:
        return True


if __name__ == "__main__":
    main()