###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")
mySprite = codesters.Sprite("butterfly")
mySprite.set_size(0.25)
mySprite.say("You are fun")


print("Welcome to CT8!")
print("Great job correctly setting up this codespace")
print("We will be using this site for the majority of the projects for this class")
print("Make sure you bookmark this page using the STAR icon in the top right corner of your browser")


print("\n\n")
print("Now, try to view the display screen")
print("To view the display screen:")
print("\t1: click PORTS on the menu bar above this text")
print("\t2: move your mouse over the words in blue that start with https://")
print("\t3: a few icons should appear - click the globe")
print("\t4: a new tab will open - click CONNECT")
print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")
mySprite2 = codesters.Sprite("prettyrainbow",-200,200)
mySprite2.set_size(0.9)
mySprite3 = codesters.Sprite("tropicalflowers",150,-100)
mySprite3.set_size(0.6)