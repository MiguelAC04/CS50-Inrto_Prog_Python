''''
This program checks if the promted vanity plate from the
user is valid or not, knowing that they should begin with
two letters, have a length of 2-6 characters numbers 
must be at the en of the plate and 0 cannot be the first
number. Also, no punctuation is allowed.
'''
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s[:2].isalpha():
        if len(s)==2:
            return True
        elif 2<len(s)<=6:
            return check_Mid_Chars(s[2:])
    return False

def check_Mid_Chars(s):
    if s.isalnum():
        for i, c in enumerate(s):
            if c.isdigit():
                return True if s[i+1:].isdigit() and c!='0' else False      
        return True
    return False


main()