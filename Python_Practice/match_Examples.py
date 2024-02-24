def main():
    actions={
        'sound':'beep',
        'a':'b',

        'format':'ogg'
    }
    match actions:
        case {"text": message, "color": c} as d:
            print(message, c)
        case {"sleep": duration} as d:
            print(duration)
        case {"sound": url, "format": "ogg"} as d:
            print(url)
        case {"sound": _, "format": _}:
            print("Unsupported audio format")
    
    for i in range(3):
        print('a', end=' ')
    else: print('b')
    
    def example_function(**kwargs):
        print(kwargs)

    options = {'option1': 'value1', 'option2': 'value2'}
    example_function(**options)
    
    '''Match statements capabilities'''
    point=(0,0)
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")
        
    class Point:
        def __init__(self, x, y, z):
            self.x_comp = x
            self.y_comp = y
            self.z_comp = z

    def where_is(point):
        print(f"x:{point.x_comp},y:{point.y_comp}")
        match point:
            case Point(x_comp=0, y_comp=0):
                print("Origin")
            case Point(x_comp=0, y_comp=a) as p:
                print(f"Y={a}, {p.x_comp, p.y_comp}")
            case Point(x=x, y=0) as p if point.y_comp==2:
                print(f"X={x}")
            case Point():
                print("Somewhere else")
            case _:
                print("Not a point")
    
    def IF_where_is(point):
        #Same as case Point(x=0, y=0)
        if not point.x and not point.y:
            print("Origin")
        else: print('No Origin')

    def triple_If(a,b,c,/):
        if a.isdigit() and b.isdigit() and c.isdigit():
            a,b,c = int(a),int(b),int(c)
        if a < b < c:
            print('b in the middle')
        elif a == b < c:
            print('a=b, less than c')
        elif a < b == c:
            print('b=c, greater than a')
        elif a == b == c == 0:
            print('all 0')
    triple_If(*input('>> ').split(','))
    
    where_is(Point(x=0,y=1, z=0))    
    
    def matching(command):
        match command.split():
            #The [] are necessary, to assign the values of the given
            #list to the pruposed variables
            case [part_1, part_2, *rest]:
                print('More than 2 args:', *rest, rest)
            case [part_1, part_2]:
                print('2 args')
            case [comm]:
                print('1 arg')
    
    matching(input('Command: '))
    
main()