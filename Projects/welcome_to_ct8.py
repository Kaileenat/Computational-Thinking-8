###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("spring")
mySprite = codesters.Sprite("Lily")
mySprite.say("Hello its a Thursday")



print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")
mySprite2 = codesters.Sprite("kitten",-200,200)