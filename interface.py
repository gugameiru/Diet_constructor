import sys
from user_constructor import *
from menu_generator import *
from prettytable import PrettyTable
from db_getData import addFood
import textwrap

def mainMenu():
    print('''1 - Расчет меню\n2 - Добавление нового блюда\n3 - Средство объяснения\n4 - Выход\n''')
    choose = input('Введите значение: ')
    print('')
    if (choose == '1'):
        menuCounter()
    elif (choose == '2'):
        print('''Типы блюд:\n1 - Завтрак\n2 - Салат\n3 - Суп\n4 - Второе\n5 - Ужин\n6 - Напиток\n7 - Перекус на 100 калорий\n8 - Перекус на 150 калорий\n9 - Главное меню''')
        table = input('Введите значение: ')
        print('')
        if (table == '1'):
            table = 'breakfasts'
        if (table == '2'):
            table = 'Salads'
        if (table == '3'):
            table = 'Soups'
        if (table == '4'):
            table = 'Second_dishes'
        if (table == '5'):
            table = 'Dinners'
        if (table == '6'):
            table = 'Drinks'
        if (table == '7'):
            table = 'Snacks_100'
        if (table == '8'):
            table = 'Snacks_150'
        if (table == '9'):
            mainMenu()
                
        dish = input('Введите описание блюда в формате: Название, состав, вес порции, калорийность порции, белки, жиры, углеводы через запятую. Если не знаете параметр - оставьте пустое место между очередными запятыми.\n' )
        print('')
        dish = dish.split(',')
        for key in dish:
            key.strip()
        dish[2] = float(dish[2])
        dish[3] = float(dish[3])
        dish[4] = float(dish[4])
        dish[5] = float(dish[5])
        dish[6] = float(dish[6])

        addFood('food.db', table, dish)
        print('Данные добавлены')
        mainMenu()
    elif (choose == '3'):
        f = open('manual.txt', mode = 'r',encoding = 'utf-8')
        for string in f:
            print(textwrap.fill(string, 80))
        f.close()
        print('')
        mainMenu()
    elif (choose == '4'):
        sys.exit()
    else:
        pass

def menuCounter():
    userdataStr = input('Введите своё имя, возраст, пол (м или ж), рост в см., вес в кг., активность (от 1.2 до 1.9) через запятую: \n')
    userdataSpeed = input('Введите желаемую скорость похудения (низкая - 1, средняя - 2, высокая - 3 ): \n')
    # userdataStr = 'Дмитрий, 44, м, 187, 109, 1.3'
    # userdataSpeed = '2'
    userdata = userdataStr.split(',')
    if(userdata[2].strip() == 'м'):
        userdata[2] = 'male'
    if(userdata[2].strip() == 'ж'):
        userdata[2] = 'female'
    if(userdataSpeed == '1'):
        userdataSpeed = 10
    if(userdataSpeed == '2'):
        userdataSpeed = 15
    if(userdataSpeed == '3'):
        userdataSpeed = 20
    user1 = User(userdata[0], int(userdata[1]), userdata[2], int(userdata[3]), int(userdata[4]), float(userdata[5].replace(',','.')))
    counter1 = Counter(user1, userdataSpeed)

    if (counter1.bmi <= 25):
        print('%s, ваш индекс массы тела = %i. Он меньше или равен 25 (норма). Значит вам не нужно худеть' % (user1.userName, counter1.bmi)) 
        sys.exit()
    else: 
        print('%s, ваш индекс массы тела = %i. Он больше нормы.' % (user1.userName, counter1.bmi)) 
        print('По нашим расчетам, вам надо употреблять в день %i калорий, %i граммов белков, %i граммов жиров и %i граммов углеводов.' % (counter1.bmr, counter1.prots, counter1.fats, counter1.carbs))
        print('Предлагаем вам меню для похудения:')
        

    breakfast = breakfastSelection(Breakfasts.copy(deep=True), counter1.breakfastBmr)

    lunch = lunchSelection(Salads.copy(deep=True), Soups.copy(deep=True), Second_dishes.copy(deep=True), counter1.lunchBmr)

    dinner = breakfastSelection(Dinners.copy(deep=True), counter1.dinnerBmr)

    weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

    tablestrings = []

    for i in range (len(weekdays)):
        dayDishesTotal = []
        tablestrings.append(['', weekdays[i], '','','','',''])
        tablestrings.append(['Завтрак', '', '',counter1.breakfastBmr,'','',''])
        tablestrings.append(['', '', '','','','',''])
        for key in breakfast[i]:
            tablestrings.append([textwrap.fill(key[2], 45), textwrap.fill(key[3], 45), key[5], key[6], key[7], key[8], key[9]])
            dayDishesTotal.append(key)
        drink = snackSelection(Drinks).values.tolist()
        tablestrings.append([textwrap.fill(drink[0][2], 45), textwrap.fill(drink[0][3], 45), drink[0][5], drink[0][6], drink[0][7], drink[0][8], drink[0][9]])
        dayDishesTotal.append(drink[0])
        tablestrings.append(['', '', '','','','',''])
        tablestrings.append(['Перекус, 100 калорий', '', '','100','','',''])
        tablestrings.append(['', '', '','','','',''])
        snack = snackSelection(Snacks_100).values.tolist()
        tablestrings.append([textwrap.fill(snack[0][2], 45), textwrap.fill(snack[0][3], 45), snack[0][5], snack[0][6], snack[0][7], snack[0][8], snack[0][9]])
        dayDishesTotal.append(snack[0])
        tablestrings.append(['', '', '','','','',''])

        tablestrings.append(['Обед', '', '', counter1.lunchBmr,'','',''])
        tablestrings.append(['', '', '','','','',''])

        for key in lunch[0][i]:
            tablestrings.append([textwrap.fill(key[2], 45), textwrap.fill(key[3], 45), key[5], key[6], key[7], key[8], key[9]])
            dayDishesTotal.append(key)
        for key in lunch[1][i]:
            tablestrings.append([textwrap.fill(key[2], 45), textwrap.fill(key[3], 45), key[5], key[6], key[7], key[8], key[9]])
            dayDishesTotal.append(key)
        for key in lunch[2][i]:
            tablestrings.append([textwrap.fill(key[2], 45), textwrap.fill(key[3], 45), key[5], key[6], key[7], key[8], key[9]])
            dayDishesTotal.append(key)
        drink = snackSelection(Drinks).values.tolist()
        tablestrings.append([textwrap.fill(drink[0][2], 45), textwrap.fill(drink[0][3], 45), drink[0][5], drink[0][6], drink[0][7], drink[0][8], drink[0][9]])
        tablestrings.append(['', '', '','','','',''])
        dayDishesTotal.append(drink[0])
        tablestrings.append(['Перекус, 150 калорий', '', '','150','','',''])
        tablestrings.append(['', '', '','','','',''])
        snack = snackSelection(Snacks_150).values.tolist()
        tablestrings.append([textwrap.fill(snack[0][2], 45), textwrap.fill(snack[0][3], 45), snack[0][5], snack[0][6], snack[0][7], snack[0][8], snack[0][9]])
        tablestrings.append(['', '', '','','','',''])
        dayDishesTotal.append(snack[0])
        tablestrings.append(['Ужин', '', '',counter1.dinnerBmr,'','',''])
        tablestrings.append(['', '', '','','','',''])
        for key in dinner[i]:
            tablestrings.append([textwrap.fill(key[2], 45), textwrap.fill(key[3], 45), key[5], key[6], key[7], key[8], key[9]])
            dayDishesTotal.append(key)
        drink = snackSelection(Drinks).values.tolist()
        tablestrings.append([textwrap.fill(drink[0][2], 45), textwrap.fill(drink[0][3], 45), drink[0][5], drink[0][6], drink[0][7], drink[0][8], drink[0][9]])
        dayDishesTotal.append(drink[0])
        tablestrings.append(['Всего за день', '------------------------------', '%i г.' % choosenDishesSum(dayDishesTotal,5),'%i к.' % choosenDishesSum(dayDishesTotal,6),'%i б.' % choosenDishesSum(dayDishesTotal,7),'%i ж.' % choosenDishesSum(dayDishesTotal,8),'%i у.' % choosenDishesSum(dayDishesTotal,9)])
        tablestrings.append(['------------------------------', '------------------------------', '-----','-----','-----','-----','-----'])

    fullMenu = PrettyTable()
    fullMenu.field_names = ['Название','Состав','Вес','К','Б','Ж','У']
    fullMenu.align['Название'] = 'l'
    fullMenu.align['Состав'] = 'l'
    fullMenu.align['Вес'] = 'r'
    fullMenu.align['К'] = 'r'
    fullMenu.align['Б'] = 'r'
    fullMenu.align['Ж'] = 'r'
    fullMenu.align['У'] = 'r'
    for key in tablestrings:
        fullMenu.add_row(key)

    print(fullMenu)
    mainMenu()

mainMenu()




    





