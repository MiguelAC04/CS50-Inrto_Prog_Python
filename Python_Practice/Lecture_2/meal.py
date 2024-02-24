'''
This program is supposed to recieve some hour by the user,
and and cathegorize it into: 7:00 to 8:00 for breakfast,
12:00-13:00 lunch and 18:00-19:00 for dinner, inclusive. It
also allows the user to enter 12-hour formats.
'''

def main():
    time=input('\nHour: ')
    
    def get_Mili_Time(time):
        match (time).split():
            case [hour]:
                if valid_Hour(hour, '24-hour'): return convert(hour)

            case [hour, format] if format:
                if valid_Hour(hour, '12-hour'):
                    hour=convert(hour)
                    match format:
                        case 'am' | 'a.m':
                            return hour if not hour>=12 else hour-12
                        case 'pm' | 'p.m':
                            return hour+12 if not hour>=12 else hour
        return None
    
    def get_Meal(n_Hours): 
        if   7 <=n_Hours<= 8: print('breakfast time', end='\n\n')
        elif 12<=n_Hours<=13: print('lunch time', end='\n\n')
        elif 18<=n_Hours<=19: print('dinner time', end='\n\n')
    
    military_Time=get_Mili_Time(time)

    if military_Time:
        get_Meal(military_Time)
    else: 
        print('Invalid hour format')       
    
        
def valid_Hour(t, format):
            hour, min=t.split(':')
            if 0<=int(min)<=59:
                match format:
                    case '12-hour':
                        if 1<=int(hour)<=12: return True
                    case '24-hour':
                        if 0<=int(hour)<=23: return True
            return False

            
def convert(time):
    hour, min=time.split(':')
    return float(hour)+float(min)/60
    

if __name__ == "__main__":
    main()