###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("flowers")
mySprite = codesters.Sprite("flowers")
mySprite.say("hooray you found me!")


print("\n\n\nWhen you have found the CARDINAl, click here, then use CTRL C to end the program \n\n")
print("This is the new last instruction")
mySprite2 = codesters.Sprite("baseball",-200,200)