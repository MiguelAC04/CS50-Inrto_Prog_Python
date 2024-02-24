'''
This program takes out all vowls from
a user's input
'''
def main():
    sentence=input('Input: ')
    print(delete_Vowls(sentence))


def delete_Vowls(promt):
    vowls=['a','e','i','o','u']
    for letter in promt:
        if not letter.isspace() and vowls:
            if letter.lower() in vowls:
                promt=promt.replace(letter, '')
                vowls.pop(vowls.index(letter.lower()))
    return promt


main()