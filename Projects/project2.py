###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

morningperson_points = 0
nightperson_points = 0

answer = input("If you could choose your ideal sleep schedule, would you prefer to A) Wake up early and go to bed early, or B) Wake up later and go to bed later?")
if answer == "A":
    morningperson_points += 1
elif answer == "B":
    nightperson_points += 1

answer = input("When do you generally feel most alert and energetic A) In the morning, or B) In the evening")
if answer == "A":
    morningperson_points += 1
elif answer == "B":
    nightperson_points += 1

answer = input("If you had a free day, would you rather A)Spend the morning doing activities,or B) Spend the evening doing activities")
if answer == "A":
    morningperson_points += 1
elif answer == "B":
    nightperson_points += 1

answer = input("How do you typically feel when you have to wake up early A) Refreshed and ready, or B) Groggy and tired" )
if answer == "A":
    morningperson_points += 1
elif answer == "B":
    nightperson_points += 1

answer = input ("Do you find it easier to A) Get out of bed in the morning, or B) Stay up late at night")
if answer == "A":
    morningperson_points += 1
elif answer == "B":
    nightperson_points += 1

# end of quiz:
if morningperson_points > nightperson_points:
    print ("you are a morning person")
elif nightperson_points > morningperson_points:
    print ("you are a night person")
