###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("underwater")
q1 = codesters.Triangle(-100, 100, 150, 'orange')
q2 = codesters.Square(-100,-100, 150, 'red')
q3 = codesters.Circle(100, 100, 150, 'green')
q4 = codesters.TriangleIso(100,-100, 75,75, 'black')

s1 = codesters.Sprite("racket", 100, 100)
s2 = codesters.Sprite("doggy", -100, -100)
s3 = codesters.Sprite("wailord" , -100, 120)
s4 = codesters.Sprite("fish",100,-110)

message1 = codesters.Text("Eli Scher", 0, 210, "yellow")
message2 = codesters.Text("FISHY FISHY FISHY", 0, -210, "red")