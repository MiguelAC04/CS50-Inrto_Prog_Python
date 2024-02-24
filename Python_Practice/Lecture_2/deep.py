'''
The supposed purpose of everything is 42, or the
aplhabetical representation of this magnitud
("forty two", "forty-two"). The program must
take the answer from the user and promt if he
was right or not.
'''

def main():
    answer=input("""What is the Answer to the Great Question of Life, the Universe, and Everything? """)
    
    def purpose_Everything(answer):
        match answer.lower():
            case '42' | 'forty two' | 'forty-two':
                return 'Yes'
            case _:
                return 'No'
    
    print(purpose_Everything(answer))


main()

