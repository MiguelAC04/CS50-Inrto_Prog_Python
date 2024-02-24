def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    def get_Total(menu):
        total_Price = 0.00
        while True: 
            if item := input('Item: '):
                if price := menu.get(item.title()):
                    total_Price+=price
                    print(f'Total: ${total_Price:.2f}')
            else:
                break
    # get_Total(menu)
    
    def get_Total2(menu):
        
        def get_Price(item):
            try:
                return menu[item.title()]
            except KeyError:
                return
        
        total_Price = 0.00
        
        while True:
            try:
                if item := input("Item: "):
                    if price := get_Price(item):
                        yield (total_Price := total_Price+price) 
                else: 
                    return
            except EOFError:
                return
            
    [print(f'Total: ${price:.2f}') for price in get_Total2(menu)]
        
                

main()