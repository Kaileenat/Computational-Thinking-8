###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("wintertrees")

q1 = codesters.Square(100,100, 200, 'red')
q2 = codesters.Square(-100,100, 200, 'black')
q3 = codesters.Square(-100,-100, 200, 'green')
q4 = codesters.Square(100,-100, 200, 'gray')

s1 = codesters.Sprite("cardinal", 100, 100)
s1.set_size(0.60)

s2 = codesters.Sprite("basketball", -100, 100)
s2.set_size(2.00)

s3 = codesters.Sprite("soccerball", -100, -100)
s3.set_size(1.50)

s4 = codesters.Sprite("chesspawn", 100, -100)
s4.set_size(0.015)

message1 = codesters.Text("Emmett Robison", 0, 220, "black")
message2 = codesters.Text("I don't know", 0, -220, "black")