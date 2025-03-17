###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")
q1=codesters.Square(100, 100, 200,'blue')
q2=codesters.Square(-100, 100, 200,'yellow')
q3=codesters.Square(-100, -100, 200,'blue')
q4=codesters.Square(100, -100, 200,'yellow')
s1=codesters.Sprite("bbb" ,100,100)
s2=codesters.Sprite("cal" ,-100,100)
s3=codesters.Sprite("cardinal" ,-100,-100)
s4=codesters.Sprite("basketball" ,100,-100)
s1.set_size(0.7)
s4.set_size(2.0)
message1=codesters.Text("my name is michael",0,220,"red")
message12=codesters.Text("baseball is cool",0,-220,"black")