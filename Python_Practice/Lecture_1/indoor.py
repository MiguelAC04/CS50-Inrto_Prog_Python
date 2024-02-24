def main():
    input_Str=input('Enter something: ')
    
    # def process_Str(input):
    #     return input.lower()
    
    # print(process_Str(input_Str))
    #NOTE:Or:
    process_Str=lambda input:input.lower()
    print(process_Str(input_Str))
    

main()