from random import randint, choice


'''
    This programs ask the user for the degree
of difficutly he desires to perform a series
of 10 arithmetic operations and evaluates how
many answers he got right.
'''

def main() -> None:
    sum = '{x} + {y}'
    minus = '{x} - {y}'
    div = '{x} / {y}'
    multi = '{x} * {y}'
        
    correct_ans = 0

    L = get_level()
    
    for i in range(10):
        print('\tProblem ', i+1)
        correct_ans += ask_Q(L, sum, minus, div, multi)
    
    print(f'Correct {correct_ans}/10')


def generate_integer(level: int) -> int:
    '''Returns integer for operation'''
    max = 10**level-1
    return randint(0, max)


def get_ans() -> float:
    '''Gets the answer from the user'''
    clean = lambda n: n.replace('.', '', 1).replace('-','',1)
    while True:
        if clean(ans:=input()).isdigit():
            return float(ans)
        
        
def get_level() -> int:
    '''Gets amount of digits for values in the operation'''
    while True:
        if (level:=input('Level: ')).isdigit():
            level = int(level)
            if 0 < level < 4:
                return level
  

def ask_Q(L=1, *oprs: tuple[str]) -> int:
    '''Constructs the question to ask the user
    
    and prompts it to him, before checking if 
    
    the answer is correct or not.
    '''
    get_opr = lambda opr_: choice(opr_)
    while True:
        x, y = generate_integer(L), generate_integer(L)
        opr = get_opr(oprs).format(x=x, y=y)
        try:
            ans = round(eval(opr), 2)
        except ZeroDivisionError:
            pass
        else: break
        
    for _ in range(3):
        print(opr+' =', end=' ')
        if get_ans() == ans:
            return 1
    else:
        print('EEE', ans)
        return 0


if __name__ == "__main__":
    main()