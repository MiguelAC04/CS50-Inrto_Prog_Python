from string import Template

'''
This code plays with some important capabilities
of the Template sting class
'''

def main() ->  None:
    templ_1 = Template('$person is $years old $Noun')
    mapp = {'Noun' : 10, 'person' : 'She'}
    print(templ_1.substitute(mapp, person='He', years=13))
    templ_2 = Template('$Person plays $piano')
    print(templ_2.safe_substitute())
    print(templ_2.template)

if __name__ == "__main__":
    main()
