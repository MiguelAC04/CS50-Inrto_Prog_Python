def main():
    input_Str=input('Enter some faces: ')
    
    def faces(input):
        faces.smiley='🙂' ; faces.sad='🙁'
        input=input.replace(':)', faces.smiley)
        return input.replace(':(', faces.sad)
    
    print('Result:', faces(input_Str))
    
main()
