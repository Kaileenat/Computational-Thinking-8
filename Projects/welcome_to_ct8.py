###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")
mySprite = codesters.Sprite("download.webp")
mySprite2 = codesters.Sprite("baseball", -200, 200)
mySprite2 = codesters.Sprite("basketball", 0, 200)
mySprite.say("How did you find me??")
mySprite = codesters.Sprite("flower2.gif" 0, -250)

print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")
print("This is the new last instruction")