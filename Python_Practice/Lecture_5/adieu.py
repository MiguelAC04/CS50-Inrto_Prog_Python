def main() -> None:
    names = list()
    while True:
        if name := input('Name>> '):
            names.append(name.title())
        else:
            adieu(names)
            break


def adieu(names: list) -> None:
    print('Adieu, adieu, to', end=' ')
    n = len(names)
    if n == 1:
        print(*names)
    else:
        for i, name in enumerate(names):
            print(name+',', end=' ') if not i==n-1 else print('and '+name)
    
    
main()