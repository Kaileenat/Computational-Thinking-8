###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("summer")
q1 = codesters.Square (100, 100, 200, 'green')
q2 = codesters.Square (-100, 100, 200, 'blue')
q3 = codesters.Square (-100, -100, 200, 'black')
q4 = codesters.Square (100, -100, 200, 'red')
s1 = codesters.Sprite("cardinal", 100, 100)
s2 = codesters.Sprite("basketball",-100, -100)
s2.set_size(3.0)
s3 = codesters.Sprite("Snowboard.png", 100, -100)
s3.set_size(0.4)
s4 = codesters.Sprite("Spotify.png", -100, 100)
s4.set_size(0.2)
message1 = codesters.Text("levi Kaufman",0,220, "red")
message2 = codesters.Text("team work makes the dream work",0,-220,"pink")