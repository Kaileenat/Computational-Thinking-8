###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")

q1 = codesters.Square(100, 100, 200, 'CornflowerBlue')
q2 = codesters.Square(-100, 100, 200, 'LightGoldenrodYellow')
q3 = codesters.Square(-100, -100, 200, 'Turquoise')
q4 = codesters.Square(100, -100, 200, 'RosyBrown')


s1 = codesters.Sprite("Shiba", 100, 100)
s1.set_size(0.05)
s2 = codesters.Sprite("writing", -100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite("cardinal", 100, -100)
s4 = codesters.Sprite("cat", -100, 100)
s4.set_size(0.25)

message1 = codesters.Text("Ezra/ El Sobotka", 0,220, 'blue')

message2 = codesters.Text("Kill the pig, cut his throat, spill his blood!", 0,-220, 'red')