from string import Template

'''
This code plays with some important capabilities
of the Template sting class
'''

def main() ->  None:
    templ_1 = Template('$person is $yzears old')
    print(templ_1.substitute(person='He', years=13))
    

main()
