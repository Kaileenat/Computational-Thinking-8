###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("fall")
mySprite = codesters.Sprite("baldactors.webp")
mySprite.say("I hate mondays!")


mySprite2 = codesters.Sprite ("baseball" ,-200 , 200)