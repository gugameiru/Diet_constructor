import sqlite3
import numpy as np
import pandas as pd

pd.options.display.max_rows = 100

def getDataFrames(cursor, sql):
    cursor.execute(sql)
    foods = (cursor.fetchall())
    foodsLst = []
    for i in foods:
        lst = list(i)
        foodsLst.append(lst)

    return foodsLst

def getFood(db, meal):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    sql = "SELECT *  FROM '%s'" % meal

    meal = pd.DataFrame(getDataFrames(cursor, sql))
    meal.columns = list(map(lambda x: x[0], cursor.description))
    meal = meal.sort_values(by=['Calories'], ascending=False).reset_index()

    conn.close()

    return meal

def addFood(db, table, recipe):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO '%s'([Name],[Consist_of],[Weight], [Calories], [Prots], [Fats], [Carbs]) VALUES (?, ?, ?, ?, ?, ?, ?)" %table, (recipe))

    conn.commit()
    conn.close()

   

# newRecipe = ['Свежевыжатый сок', 'морковь, яблоки, лимон', None, 200, 80, 1.8, 0.5, 16]

# addFood('food.db', 'Drinks', newRecipe)













