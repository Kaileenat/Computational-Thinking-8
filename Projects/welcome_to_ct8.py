###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("summer")
mySprite = codesters.Sprite("potato.png")
mySprite.say("we all live together in a shed!")



print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")
mySprite2 = codesters.Sprite("potato chip.png",-200,200)
mySprite2 = codesters.Sprite("chip",200,-200)