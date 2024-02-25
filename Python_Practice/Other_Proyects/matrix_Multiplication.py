def main():
    
    def constructor(self):
        self.name = list_.objs
        list_.objs+=1
        print('\tMatrix', self.name)
        
        def get_Size():
            while True:
                size=input('Size of matrix (i x j): ')
                match size.split('x'):
                    case i, j:
                        if i.isdigit() and j.isdigit():
                            i, j = int(i), int(j)
                            if i and j: return i, j 
                    case _:       
                        print('NOTE: Size sintax [rows!=0]x[columns!=0]')
        
        def get_Matrix():
            rows, columns = get_Size()
            print('Enter row values:')
            
            self.rows = rows ; self.columns = columns
            self.square = True if rows == columns else False
 
            for i in range(rows):
                while True:
                    row = input(f'row[{i}]: ').split(',')
                    if len(row) == columns:
                        if all(row[j].isdigit() for j in range(columns)):
                            self.append(list(map(int, row)))
                            print(type(self[0][0]))
                            break
                        else:
                            print('Enter only numbers')
                    else:
                        print('NOTE: Row Syntax [x],[y],[z]')
        
        get_Matrix()
                
    global list_  
    list_ = type('list_', (list, ), {
                    '__init__':constructor,
                    
                    'objs':0,
                    
                    'traspose':traspose,
        })  
       
    matrix=list_()   
    
    match input('Find traspose or mutiply? ').title():
        case 'Traspose':
            matrix.traspose()
            print(matrix)
        case 'Multiply':
            matrix_2=list_()
            print(matrix.name, matrix_2.name)
            while True:
                mtr = input('Operation: ').split('*')
                print(mtr)
                print(str(matrix.name)==mtr[0], str(matrix_2.name)==mtr[1])
                m1_Name, m2_Name = str(matrix.name), str(matrix_2.name)
                match mtr:
                    case [m1_Name, m2_Name]:
                        print('case 1')
                        print_Matrix(multiply(matrix, matrix_2))
                    case [m2_Name, m1_Name]:
                        print_Matrix(multiply(matrix_2, matrix))
                    case _:
                        print('Operation Syntax [matrix_X]*[matrix_Y]')
                        continue
                break

def multiply(m1, m2):
    if m1.columns == m2.rows:
        result=list()
        row=list()
        
        for i in range(m1.rows):
            for j in range(m2.columns):
                item=0
                for k in range(m1.columns):
                    item+=m1[i][k]*m2[k][j]
                row.append(item)
            result.append([*row])
            del row[:]
        return result

def traspose(self):
    size=len(self)
    # Method 1: 
    #  [[matrix[i][j] for i in range(size)] for j in range(size)]
    
    #Method 2:
    # self=list(zip(*self))
    
    #Method 3:
    for i in range(size):
        for j in range(i+1,size):
            self[i][j], self[j][i] =  self[j][i], self[i][j]
    return self
 
def print_Matrix(matrix):
    # [print(item) for subitem in matrix for item in subitem]
    # [[print(row) for row in item] for item in matrix]
    if matrix:  
        [print(*item) for item in matrix]

main()
    
    
    
    