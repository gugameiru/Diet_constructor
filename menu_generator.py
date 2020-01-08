from db_getData import getDataFrames
from db_getData import getFood

Breakfasts = getFood('food.db', 'breakfasts')
Dinners = getFood('food.db', 'Dinners')
Drinks = getFood('food.db', 'Drinks')
Salads = getFood('food.db', 'Salads')
Second_dishes = getFood('food.db', 'Second_dishes')
Snacks_100 = getFood('food.db', 'Snacks_100')
Snacks_150 = getFood('food.db', 'Snacks_150')
Soups = getFood('food.db', 'Soups')

def choosenDishesSum(choosenDishes, index):
    sum = 0
    for key in choosenDishes:
        if (key[index] == None):
            continue
        sum += key[index]
    return sum

def dishesSelection(dishes, calories):    
    
    choosenDishes = []  
    for key in dishes.iterrows():
        if ((key[1][6] >= (calories - 30)) and (key[1][6] <= (calories + 30))):
            choosenDishes.append(dishes.loc[key[0]])
            dishes.drop([key[0]], inplace=True)
            return choosenDishes
    
    if (choosenDishes == []):
        tmp = dishes.head(n=15)
        dishSample = tmp.sample(n=1)
        dishIndex = int(dishSample.index[0])
        dishSample = dishSample.iloc[0]
        choosenDishes.append(dishSample)
        dishes.drop([dishIndex], inplace=True)
        sum = 0
        for key in dishes.iterrows():
            sum = key[1][6] + choosenDishes[0][6]
            if ((sum >= calories - 30) and (sum) <= (calories + 30)):
                choosenDishes.append(dishes.loc[key[0]])
                dishes.drop([key[0]], inplace=True)
                return choosenDishes   
    
    if (choosenDishesSum(choosenDishes, 6) < calories):
        tmp = dishes.head(n=15)
        dishSample = tmp.sample(n=1)
        dishIndex = int(dishSample.index[0])
        dishSample = dishSample.iloc[0]
        choosenDishes.append(dishSample)
        dishes.drop([dishIndex], inplace=True)

        sum = choosenDishesSum(choosenDishes, 6)
        for key in dishes.iterrows():
            prevSum = sum
            sum += key[1][6]  
            if ((sum >= (calories - 30)) and (sum <= (calories + 30))):
                choosenDishes.append(dishes.loc[key[0]])
                dishes.drop([key[0]], inplace=True)
                return choosenDishes
            else:
                sum = prevSum
    
    choosenDishes = []
    tmp = dishes[20:80]
    dishSample = tmp.sample(n=1)
    dishIndex = int(dishSample.index[0])
    dishSample = dishSample.iloc[0]
    choosenDishes.append(dishSample)
    dishes.drop([dishIndex], inplace=True)
    return choosenDishes

def snackSelection(snack):
    return snack.sample(n=1)

def breakfastSelection(dishes, calories):
    breakfasts = []

    for i in range(7):
        breakfasts.append(dishesSelection(dishes, calories))

    return breakfasts

def lunchSelection(salads, soups, secondDishes, calories):

    lunchDishes = []
    
    lunchDishes1 = []
    lunchDishes2 = []
    lunchDishes3 = []

    caloriesSample = calories / 4

    saladCalories = caloriesSample * 0.75
    soupCalories = caloriesSample
    secondDishCalories = caloriesSample * 2

    for i in range(7):
        lunchDishes1.append(dishesSelection(salads, saladCalories))
        lunchDishes2.append(dishesSelection(soups, soupCalories))
        lunchDishes3.append(dishesSelection(secondDishes, secondDishCalories))
    
    lunchDishes = [lunchDishes1, lunchDishes2, lunchDishes3]
    return lunchDishes



