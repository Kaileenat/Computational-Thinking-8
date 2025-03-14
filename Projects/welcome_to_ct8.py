###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("fall")
mySprite = codesters.Sprite("blackcat")
mySprite.say("whats up")
mySprite.set_size(1.5)

mySprite2 = codesters.Sprite("coralinesquid")
mySprite2.set_size(.25)

print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")