def main() -> None:
    mall_List = dict()
    
    terminate = lambda:[print(f'{amount} {item}') for item, amount in mall_List.items()]
    while True:
        try:
            if not (new_Item := input().upper()):
                raise EOFError
        except EOFError:
            terminate()
            break
        else:
            mall_List.setdefault(new_Item, 0)
            mall_List[new_Item]+=1

def main_2() -> None:
    mall_List = dict()
    
    terminate = lambda:[print(f'{amount} {item}') for item, amount in mall_List.items()]
    while True:
        try:
            if not (new_Item := input().upper()):
                raise EOFError
        except EOFError:
            terminate()
            break
        else:
            if new_Item in mall_List:
                mall_List.update({new_Item: 0})
            mall_List[new_Item]+=1
                
main_2()