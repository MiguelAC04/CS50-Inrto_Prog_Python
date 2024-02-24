'''
This program get the number of calories
that the fruit the user promts has.
'''
def main():
    fruit_Calories={
        'Apple':130,         'Avocado':50,
        'Banana':110,        'Cantaloupe':50,
        'Grapefruit':60,     'Grapes':90,
        'Honeydew Melon':50, 'Kiwifruit':90,
        'Lemon':15,          'Lime':20,
        'Nectarine':60,      'Orange':80,
        'Peach':60,          'Pear':100,
        'Pineapple':50,      'Plums':70,
        'Strawberries':100,  'Sweet Cherries':100,
        'Tangerine':50,      'Watermelon':80,
        }
        
    def get_Calories(user_Fruit):
        for fruit in fruit_Calories:
            if fruit == user_Fruit:
                print(f'Calries: {fruit_Calories[fruit]}') 
                break
        else:
            print('No fuit found')
    
    get_Calories(input('Fruit: ').title())
    
   

    


main()