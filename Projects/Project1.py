###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("castle")

q1 = codesters.Square(100,100,200, 'black')
q1 = codesters.Square(-100,100,200, 'crimson')
q1 = codesters.Square(100,-100,200, 'aqua')
q1 = codesters.Square(-100,-100,200, 'darkmagenta')

s1=codesters.Sprite("rugby", 100, -100)
s1.set_size(.8)
s2=codesters.Sprite("cookie", -100, -100)
s2.set_size(.4)
s3=codesters.Sprite("magic", 100, 100)
s3.set_size(.18)
s4=codesters.Sprite("pc", -100, 100)
s4.set_size(.4)

message1 = codesters.Text("My Name is Jack", 0, 220, "black")
message2 = codesters.Text("If It Doesn't Hurt, Your Not Doing It Right", 0, -220, "black")