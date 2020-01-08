class User:

    def __init__(self, userName, userAge, userSex, userHeight, userWeight, userActivity):
        self.userName = userName
        self.userAge = userAge
        self.userSex = userSex
        self.userHeight = userHeight
        self.userWeight = userWeight
        self.userActivity = userActivity
      
class Counter:

    def __init__(self, user, looseSpeed):
        self.user = user
        self.looseSpeed = looseSpeed

        if (self.user.userSex == 'male'):
            self.bmr = round((9.99*self.user.userWeight + 6.25*self.user.userHeight - 4.92*self.user.userAge + 5)*self.user.userActivity)
        if (self.user.userSex == 'female'):
            self.bmr = round((9.99*self.user.userWeight + 6.25*self.user.userHeight - 4.92*self.user.userAge - 161)*self.user.userActivity
        )    

        self.bmi = round(self.user.userWeight / ((self.user.userHeight / 100) ** 2))

        if (looseSpeed == 10):

            self.prots = round(((self.bmr/100) * 30)/4)
            self.fats = round(((self.bmr/100) * 15)/9)
            self.carbs = round(((self.bmr/100) * 45)/4)

            self.bmr = round(self.bmr * 0.9)

        if (looseSpeed == 15):

            self.prots = round(((self.bmr/100) * 30)/4)
            self.fats = round(((self.bmr/100) * 15)/9)
            self.carbs = round(((self.bmr/100) * 40)/4)

            self.bmr = round(self.bmr * 0.85)

        if (looseSpeed == 20):

            self.prots =round(((self.bmr/100) * 30)/4)
            self.fats = round(((self.bmr/100) * 15)/9)
            self.carbs = round(((self.bmr/100) * 35)/4)
            self.bmr = round(self.bmr * 0.8)

        self.breakfastBmr = round(((self.bmr/100)*40) - 100)
        self.lunchBmr = round(((self.bmr/100)*35) - 150)
        self.dinnerBmr = round(self.bmr - (self.breakfastBmr + 100) - (self.lunchBmr + 150))



    







    









