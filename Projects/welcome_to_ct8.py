###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")

mySprite = codesters.Sprite("Gentleman", -150, -100)
mySprite.set_size(0.3)
mySprite.say("Hello My Good Sir")

mySprite2 = codesters.Sprite("Typical Gentleman", 150, -100)
mySprite2.set_size(0.4)
mySprite2.say("Hello Good Sir, Would You Like Some Tea")

mySprite3 = codesters.Sprite("Tea Stuff", 0, -100)
mySprite3.set_size(0.1)