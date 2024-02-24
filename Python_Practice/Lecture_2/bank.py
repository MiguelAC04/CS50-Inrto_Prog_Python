'''
The purpose of this code is t model a program that
gives the used $0 if he greets with a "hello", $20
if the greeting begins with an "h" and $100 otherwise.
The evaluation must be case-insensitive.
'''

def main():
    greeting=input("Greeting: ").lower()
    
    def ev_Greeting(greeting):
        
        def get_First_Word(str):
            return str.split()[0]
        
        greeting=get_First_Word(greeting)
        
        '''Fastest way to do it is though re library'''
        #if re.search(greeting, 'hello', 'ignorecase')
        
        if greeting.__contains__('hello'):
            '''
            This evaluation can also be done through:
            1. 'hello' in greeing:
            2. greeting.find('hello'): Returns index of fining, else -1
            3. greeting.index('hello'): If nothing is found, raises error
            4. greeting.count('hello'): Returns 0 if none was found.
            '''
            return 0
        elif 'h'==greeting[0]:
            return 20
        else:
            return 100  

    earned_Money=ev_Greeting(greeting)
    print(f'You earned ${earned_Money}')
    
main()