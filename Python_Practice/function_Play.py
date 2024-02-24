def main():
    '''Changing default values during run time'''
    x='Str'
    def f(a=[x,], b=0):
        a.append(x)
        b+=1
        return [a,b]
    
    print('\tDefaul value for mutable objects\n'
           '\tcan change in run time')
    print(f())
    print(f())
    
    def f2(a,/):
        return(a)
    print(f2(2))
    
    nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat_list = [item for sublist in nested_lists for item in sublist]
    print(*flat_list, end='\n\n')
    
    
    '''Using the * operator to unpack tuples in parameters'''
    print('\Tuple Packing and Unpacking:')
    ## NOTE: To avoid 'name' having it's value assign twice,
    ##       the '/' can be used, to specify that the first 'name',
    ##       can only be recieved positoinally, unlike the one in
    ##       the ditionary
    def present_Artist(name='Museum Louvre',/, *contributors, **kwargs):
        print('Contributors: ', *contributors, sep='/')
        for item in kwargs:
            print(f'{item.title()}:{kwargs[item]}')

    present_Artist('Alexander', 'Leonardo da Vinci',
                   name='Pablo Picasso', age=3, hobbies=['reading','painting'])
    
    # def present_Artist(date, contributors, kwargs):
    #     print('Contributors: ', *contributors, sep='/')
    #     for item in kwargs:
    #         print(f'{item.title()}:{kwargs[item]}')
    
    # present_Artist('13/13/13', ('Alexander', 'Leonardo da Vinci'),
    #         {'name':'Pablo Picasso', 'age':3, 'hobbies':['reading','painting']})


    def paint(pencil, *colors, style):
        print('Painting with: ',pencil)
        print(f'{style},  {colors}', end='\n\n')
    
    paint('Faber-Castell', 
          'red', 'white', ' organe', 'black', 
          style='Abstract')
    # def paint(pencil, colors, style):
    #     print('Painting with: ',pencil)
    #     print(f'{style},  {colors}')
    # paint('Faber-Castell', ('red', 'white', ' organe', 'black'), 'Abstract')


    '''Using ** operator to unpack dictoinaries in parameters'''
    print('\tDictionary Packing and Unpacking: ')
    car={'brand':'Audi', 
         'year':'2012', 
         'color':'black',
         'plate':'CS500',
         'rim_Size':23,
         'crashed':False,
    }
    
    def f(*prev_Owners,
          plate, brand='BMW', year='2023',
          color='white', miles=1000, 
          **rest):
        print(brand, year, color, prev_Owners)
        print(plate, miles, 'miles')
        print(rest, end='\n\n')
        
    f('A','B','C', miles=90_000, **car)

    
    print('''\tSpecial parameters''')
    # def display(a,/,b,*,c):
    #     print(a,b,c, sep='')
    # display('a', 'b', c='c') # display('a', b='b', c='c')
    display=lambda a, /, b, *, c: print(a, b, c, sep='')
    display('a', 'b', c='C')
    
    print('''\tLambda Expressions''')
    def find_Sums(n):
        # combinations=list()
        # for i in range(n):
        #     j=n-i
        #     combinations.append((i,j))
        # return combinations
    #OR
        for i in range(n):
            yield (i, n-i)
    sums=lambda n: (*find_Sums(n), print('Res:', end=' '))
    print(sums(3), end='\n\n')
    
    
    print('''\tGiving atributes to Functions''')
    class Point():
        origin=(0,0)
        def __init__(self) -> None:
            pass
        def m1(self, a:str, b:(int, int))->'int or None':
            pass
    
    def display(c:str, 
                default:Point=Point.origin) -> 'str or None':
        display.used=0
        display.uses=[1,]
        if c.isalpha():
            display.used+=1
            display.uses.append(1)
            return c.swapcase()
        else:
            return None
    print(f'Return Val: {display("aBcDe")}, UsedAttr: {display.used}, UsesList= {display.uses}')
    print(f'Return Val: {display("AbCdE")}, UsedAttr: {display.used}, UsesList= {display.uses}')
    print(f'Return Val: {display("00000")}, UsedAttr: {display.used}, UsesList= {display.uses}')
    print(display.__annotations__, end='\n\n') 
        
main()