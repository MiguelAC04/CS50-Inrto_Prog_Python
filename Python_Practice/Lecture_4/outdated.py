from datetime import date

def main() -> None:
    '''
        Parce middle-edian date to 
        
        the standard ISO 8601 format.
    '''
    # print(date.fromtimestamp(613415314))
    # print(date.fromisocalendar(2023,42,2))
    # print((d:=date.fromisoformat('2023-12-21')), type(d))
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]
    
    def get_ISO(date_: str) -> list:
        '''
            Recieves date in format [m/d/y] or 
            
            [m d, y] and returns the number of each.
        '''
        match date_.split('/'):
            case [month, day, year]:
                integers = year.isdigit() and month.isdigit() and day.isdigit()
                return (int(year), int(month), int(day)) if integers else None
        
        # title = lambda str: str.title()
        # match list(map(title, date_.split())):
        match date_.title().split():
            case [month, day, year]:
                if month in months:
                    day = day.replace(',', '', 1)
                    if day.isdecimal() and year.isdecimal():
                        return int(year), months.index(month)+1, int(day)
    
    while True:
        if date_Parts := get_ISO(input("Date: ")):
            try:
                iso_Date = date(*date_Parts)
            except (ValueError, OverflowError):
                continue
            except Exception as err:
                print('Unexpected:', err)
            else:
                if iso_Date <= date.today():
                    print(iso_Date)
                #Or:
                    #print(f'{year}-{month:02}-{day:02}')
                    break
                
                
if (n:=__name__) == "__main__":
    print(n)
    main()