###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("Kitties.jpeg")
mySprite = codesters.Sprite("Cute cat.jpeg")
mySprite = codesters.Sprite("Doggy.jpeg", -150,50)
mySprite.say("I love pets")
mySprite = codesters.Sprite("Bunny.jpeg", 50,200)

print("/n/nWhen you have found the CARDINAL, click here, then suse CTRL C to end the program/n/n")
print("This is the new last instruction")
