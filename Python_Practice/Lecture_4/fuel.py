def main():
    while True:
        fuel_pct=input("Fuel: ")
        match fuel_pct.split('/'):
            case [x, y]:
                try:
                    x, y = int(x), int(y)
                except ValueError as err:
                    print(err)
                else:
                    if pct:=get_Pct(x,y):
                        print(pct)
                        break
class OverloadError(Exception):
    
    def __init__(self) -> None:
        self.message="Amount of gas can't be greater than 100%"
        super().__init__(self.message)

def get_Pct(x:int, y: int) -> str | None:
    '''Gets percentage of gas'''
    try:
        try:
            pct=x/y*100
        except ZeroDivisionError:
            raise
        else:
            if 100 >= pct >= 99:
                return "F"
            elif 1 >= pct >= 0:
                return "E"
            elif 99 > pct > 1:
                return f"{pct:.1f}%"
            else:
                raise OverloadError
    except ZeroDivisionError:
        return None
    except OverloadError:
        return None

main()