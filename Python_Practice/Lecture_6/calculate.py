'''
This program allows the user to prompt for an operation
in the terminal, and get the value.
Simply, it the same as:
try:
    eval(operation)
except SyntaxError as err:
    exit(err)
'''

def main(focus_oper: str = None) -> list[str, int] | None:
    '''Main method that construct the process of evaluating an expression'''
    operation = input('Opperation>> ') if not focus_oper else focus_oper
    operators = ('+', '-', '*', '/', 'x')

    if (oper := intersection(operation, operators)):
        if operation[-1] not in operators:
            if valid_values(operation, oper):
                return operation, evaluate(operation)
            else:
                raise ValueError('Invalid values for operation')
        else:
            exit('Missing value after operation')
    else:
        raise SyntaxError('No operator present')


intersection = lambda L1, L2: list(set(L1).intersection(L2))


def evaluate(operation: str) -> int | float:
    '''Performs the given operaiton'''
    prep_op = operation.replace(',', '').replace('x', '*')
    return eval(prep_op)


def check_decimal(num: str) -> bool:
    '''Checks whether numbers with decimal point or commas are valid'''
    match num.split('.', 1):
        case [int_part, decimal_part]:
            if len(int_part) > 3:
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
    match main():
        case [operation, result]:
            print(operation+' =', result)
