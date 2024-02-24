def main():
    ls=list(i for i in range(3))
    print('State 1: ', ls)
    ls.extend((j,j//3) for j in range(30,38,2))
    print('State 2: ', ls, '(after extend)')
    removed=ls.pop(1)
    print(f'State 3: {ls} (after pop index 1: {removed} value)')
    ls.reverse() #Returns None
    ls.insert(len(ls)-1, 'one')
    print(f'State 4: {ls} (->reverse and insert "one")')

    ls2=ls
    print(True) if ls == ls2 and ls is ls2 else print(False)     
    del ls
    print(f'ls[:] = ls2[:]: {ls2[:]}')
    
    ls3=ls2.copy()
    print(True) if ls3 is ls2 else print(False)
    print(True) if ls3 == ls2 else print(False)
    def sort_Ls2(item):
        if type(item) == tuple:
            return item [0]
        elif type(item) == str:
            return 0
        return item
    ls2.sort(key=sort_Ls2)
    print(f'State 5: {ls2} (after sort)')
    
    for x  in {'a' : 0, 'b' : 1, 'c' : 3}:
        pass
    print('X:',x)
    
    m = [
        ( 1,  2,  3),
        ('a','b','c'),
        ('A','B','C')
    ]  
    m_traspose=[[m[i][j] for i in range(len(m)) if str(m[i][j]).isdigit()] for j in range(len(m[0]))]
    print(m_traspose)
    
main()