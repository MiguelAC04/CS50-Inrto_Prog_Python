'''
This program changes the format of a variable form a Camel
form, to snake.
3 methods were used to achieve the same purpose, but it seems
that the first one is the fastest one
'''
import time

def main():
    camel_Var=input('Camelcase Name: ')
    methods=[method1, method2, method3]
    
    def print_Results(camel_Var):
        for n, method in enumerate(methods):
            t0=time.time()
            method(camel_Var)
            tF=time.time()
            print(f'{n}: {tF-t0:.10f}')
    
    print_Results(camel_Var)
    with open('text.txt', 'r') as file:
        t0=time.time()
        method1(file.read())
        method1(file.read())
        tf=time.time()
        print(f'{tf-t0:.20f}')
        # print_Results(file.read())

def method1(snake_Var):
    print('m1')
    '''Fastest'''
    for i in range(len(snake_Var)):
        char=snake_Var[i]
        if char.isupper():
            snake_Var=('_'+char.lower()).join(snake_Var.split(char))
    return snake_Var       

def method2(snake_Var):
    print('m2')

    for char in snake_Var:
        if char.isupper():
            snake_Var=('_'+char.lower()).join(snake_Var.split(char))
    return snake_Var

def method3(camel_Var):
    print('m3')

    snake_Var=str()
    for char in camel_Var:
        snake_Var+=('_'+char.lower()) if char.isupper() else char
    return snake_Var

main()