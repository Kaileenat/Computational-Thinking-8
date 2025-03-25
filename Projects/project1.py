###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")

q1 = codesters.Square(100, 100, 200, 'black')
q2 = codesters.Square(-100, 100, 200, 'PaleGreen')
q3 = codesters.Square(-100, -100, 200, 'MediumSlateBlue')
q4 = codesters.Square(100, -100, 200, 'PaleTurquoise')

s1 = codesters.Sprite("cardinal", 100, 100)

s2 = codesters.Sprite("peppapigisaprincess2", -100, -100)
s2.set_size(0.5)

s3 = codesters.Sprite("bluey", 100, -100)
s3.set_size(0.7)

s4 = codesters.Sprite("bubbleguppies", -100, 100)
s4.set_size(0.7)

message1 = codesters.Text("Alex Sumner", 0, 220,"black")
message2 = codesters.Text("im amazing", 0,-220, "black")