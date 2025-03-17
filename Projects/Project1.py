###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("summer")


codesters.Square(100, 100, 200, 'black')
codesters.Square(-100, 100, 200, 'red')
codesters.Square(-100, -100, 200, 'black')
codesters.Square(100, -100, 200, 'red')

mySprite1 = codesters.Sprite("basketball123",100,100)
mySprite1.set_size(0.3)
mySprite2 = codesters.Sprite("brawlstars",-100,-100)
mySprite2.set_size(0.1)
mySprite3 = codesters.Sprite("cardinal",100,-100)
mySprite3.set_size(0.5)
mySprite4 = codesters.Sprite("images",-100,100)
mySprite4.set_size(0.8)


codesters.Text(" My name is Mercer",0,220,"black")
codesters.Text(" I Like these things",0,-220,"black")