from string import Template

'''
This code plays with some important capabilities
of the Template sting class
'''

def main() ->  None:
    templ_1 = Template('$person is $years old')
    templ_1.substitute(person='I', years=13)
    print(templ_1)
main()
