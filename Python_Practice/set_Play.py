def main():
    colors={"red", "blue", "red", "white", "black"}
    
    def display(colors=colors, __n__=[0,]):
        __n__[0]+=1
        print(f'State {__n__}:', end=' ')
        [print(color, end=', ') for color in colors]
        print()
        
    display()
    colors.update(("orange", "yellow"), ("purpule", "pink"))
    display()
    rgb={"red", "green", "blue"}
    colors_1=colors & rgb
    display(colors_1)
    colors_2 = {"brown", "dark blue"}
    colors |= colors_2
    # colors_1.intersection_update(rgb)
    display()
    colors.pop() , colors.pop()
    display()
    
    print(float('NaN'))
    
    '''LOOPING TECHNIQUES'''
    for i, elem in enumerate({"one", "two", "three"}):
        print(i, elem)
    
    print()
    
    ingredients={"Sugar", "Flour", "Eggs", "Chocolate"}
    grams=["20 grams", "500 grams", 2]
    order=(3, 1, 2, 4)
    
    for item in zip(ingredients, grams, order):
        print(item)
    
    print()
        
    for item in sorted({"CYK 883", "RNT 772", "HJL 672"},
                       key=lambda elem: elem[-1]):
        print(item)
    
    print()    
    
    def loop():
        for i in range(3):
            print('in loop')
            yield i
    
    for j in loop():
        print('iteration number', j+1)

    print()
    
    '''Assignement in Expression'''
    if (m:=input('n>> ')).isdigit():
        n=int(m)
    else:
        n=m    
    print(type(n), n)
    
    def get_Residue(n, div):
        return n%div
    
    if (h:=n%3):
        print(h,n,m)
        

main()