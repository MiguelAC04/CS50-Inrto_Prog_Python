'''
This program's purpose is dipense a coke
when the used has entered enough 5, 10 or
25 cent coins to pay for the 50 cents value.
Also, gives change
'''
def main():
    denominations=[5,10,25]
    amount_Due=50
    
    while amount_Due>0:
        print('Amount Due:', amount_Due)
        coin=input('Coin: ')
        if coin.isdigit():
            coin=int(coin)
            if coin in denominations: amount_Due-=int(coin)
    print('Change Owed: ', abs(amount_Due))
            
main()