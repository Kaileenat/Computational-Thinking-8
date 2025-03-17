
###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("fall")
mySprite = codesters.Sprite("llama.jpg")
mySprite.say("hello stella")

mySprite2 = codesters.Sprite ("baseball",-200, 200)