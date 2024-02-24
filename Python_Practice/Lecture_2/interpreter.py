'''
This code is able to recieve a basic arithmetic
opertation from the user, and get the answer.

The key element in this code is that the values 
of a function that RETURN MORE THAN ONE value
can be ASSIGNED TO THE SAME NUMBER of VARIABLES ,
in one line, each separated by ','
'''

def main():
    operation=input("Operation: ")
        
    def calculation(x, y , z):
        x=float(x) ; z=float(z)
        match y:
            case '+': return x+z
            case '-': return x-z
            case '*': return x*z
            case '/':
                if z: return x/z
                else:
                    print('Indeterminate')
                    exit(1)
            case _: 
                print(f'Unknown operator: {y}')
                exit(2)
    
    match operation.split(' '):
        case x, y, z:
            print(f'Result: {calculation(x,y,z):.1f}')
        case _:
            print('Bad syntax operation')
   
main()