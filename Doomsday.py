import shelve
import random
import calendar
import os

#Creating the high score file if it does not already exist
filename = ('score.db')
if not os.path.exists(filename):
    s = shelve.open()
    s['score'] = 0
    s.close()

os.system('cls||clear')
count = 0

while(True):

#Generating random dates

    year = random.randint(1583, 3000)
    month = random.randint(1, 12)

    if month == 1:
        day = random.randint(1, 31)
    if month == 2:
        day = random.randint(1, 28)
    if month == 3:
        day = random.randint(1, 31)
    if month == 4:
        day = random.randint(1, 30)
    if month == 5:
        day = random.randint(1, 31)
    if month == 6:
        day = random.randint(1, 30)
    if month == 7:
        day = random.randint(1, 30)
    if month == 8:
        day = random.randint(1, 31)
    if month == 9:
        day = random.randint(1, 30)
    if month == 10:
        day = random.randint(1, 31)
    if month == 11:
        day = random.randint(1, 30)
    if month == 12:
        day = random.randint(1, 31)
# ^ If someone knows of a more efficient way to handle this section, please inform me.


    weekday = (calendar.weekday(year, month, day) + 1)
    print(str(month) + "/" +  str(day) + "/" + str(year))
    attempt = input("Calculate the day of the week of this date:")
    # 0 = Sunday
    # 1 = Monday
    # 2 = Tuesday
    # 3 = Wednesday
    # 4 = Thursday
    # 5 = Friday
    # 6 = Saturday

    if int(attempt) == weekday:
        print("Success!")

#keeping track of a high score

    count = count + 1

    if int(attempt) != weekday:
        break

count = count - 1


s = shelve.open(filename)
current = s['score']


if current >= count:
    print("Your high score is: " + str(current))

if current < count:
    highscore = count
    print("Your new high score is: " + str(highscore))
    s['score'] = count


s.close()
