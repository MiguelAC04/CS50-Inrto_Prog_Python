def main() -> None:
    str1 = '{1} is greater than {0}'.format('ONE', 'ZERO')
    str2 = '{} is placed in {point}'.format('Origin', point='0,0')
    print(str1)
    print(str2)
    names = {'John': 10.0, 'David': 40, 'Alex': 50}
    str3 = '{John:5d}, {David:5d}, {Alex:5d}, are ages'.format(**names)
    print(str3)
    class Person():
        age = 100
        bank = 'Amererican_Express', 'Citibank', 'Capital_One'
        origin = 'China'
    
    str4 = f'{Person.bank[-1]}'
    print(str4)     
main()