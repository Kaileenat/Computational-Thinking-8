###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("summer")

q1 = codesters.Square(100, 100, 200, 'DarkRed')
q2 = codesters.Square(-100, 100, 200, 'ForestGreen')
q3 = codesters.Square(-100, -100, 200, 'SaddleBrown')
q4 = codesters.Square(100, -100, 200, 'Goldenrod')

s1 = codesters.Sprite("Fire", 100, 100)
s1.set_size(0.20)

s2 = codesters.Sprite("Pig", -100, -100)
s2.set_size(0.20)

s3 = codesters.Sprite("Glasses", 100, -100)
s3.set_size(0.20)

s4 = codesters.Sprite("Conch", -100, 100)
s4.set_size(0.20)

message1 = codesters.Text ("Lucy Bui",0,220,"red")
message2 = codesters.Text (" Kill the pig! Cut his throat! Spill his blood! ",0,-220,"black")