import datetime

name = input("Give name now!")
age = input("Give age now!")
year = int(datetime.datetime.now().year) + (100 - int(age))

oneHundredYear = "You will be 100 in the year " + str(year)

num = input("How many copies!")

for i in range(0,int(num)):
    print(oneHundredYear + '\n')
