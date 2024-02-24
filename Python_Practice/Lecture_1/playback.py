def main():
    input_Str=input('Enter something: ')
    
    def replace(input):
        return input.strip().replace(' ', '...')
    #NOTE: Or:
    # replace=lambda input: input.strip().replace(' ', '...')
    print(replace(input_Str))
    
main()