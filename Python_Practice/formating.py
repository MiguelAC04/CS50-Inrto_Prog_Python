def main() -> None:
    str1 = '{1} is greater than {0}'.format('ONE', 'ZERO')
    str2 = '{} is placed in {point}'.format('Origin', point='0,0')
    print(str1)
    print(str2)
    names = {'John': 10.0, 'David': 40, 'Alex': 50}
    str3 = '{John:5.2f} | {David:5.2f} | {Alex:5.2f}, are ages'.format(**names)
    print(str3)

    class Person():
        age = 100
        bank = 'Amererican_Express', 'Citibank', 'Capital_One'
        origin = 'China'

    str4 = f'{Person.bank[-1]}'
    print(str4)
    str5 = f'{"CENTERED":.^16}'
    print(str5);

    print()

    print(f'|{12341:+}{1234: }{-1234: }|')
    print(f'{-0.023:z.1f}')
    print(f'{1000.0001:_}')
    print(f'{bin(516)}')
    print(f'{12345:6}{54321:6} {-101:06}')
    print(f'{100.1234:1}')
    print(f'{555:#x} or {555:#X}\n')
    print(f'{1_234_234.99:e} or {1_234_234.99:E}')
main()
