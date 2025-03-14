###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("summer.png")
q1 = codesters.Square(100, 100, 200, 'blue')
q3 = codesters.Square(-100, 100, 200, 'black')
q3 = codesters.Square(-100, -100, 200, 'blue')
q4 = codesters.Square(100, -100, 200, 'black')
s1 = codesters.Sprite("cardinal", 100, 100)
s1.set_size(0.5)
s2 = codesters.Sprite("soccergood", -100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite("spot (1)", 100, -100)
s3.set_size(0.3)
s4 = codesters.Sprite("french", -100, 100)
s4.set_size(0.2)

message1 = codesters.Text("Gray Johnston",0,220,"black")
message2 = codesters.Text("I like food",0,-220,"blue")