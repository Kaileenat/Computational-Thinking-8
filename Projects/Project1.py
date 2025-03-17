###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background ("summer")

q1 = codesters . Square(100,100, 200, 'pink')
q2 = codesters . Square (-100,100,200, 'navy')
q3 = codesters . Square (-100, -100, 200, 'violet')
q4 = codesters . Square (100,-100,200, 'lavenderblush')

s1 = codesters.Sprite ("Ballet Shoes ", 100, 100)
s1.set_size(0.7)
s2 = codesters.Sprite ("Shopping!", -100,-100)
s2.set_size(0.8)
s3 = codesters.Sprite ("Starbucks", 100, -100)
s3.set_size(0.5)
s4 = codesters.Sprite ("Palm Tree", -100,100)
s4.set_size(0.7)

message1 = codesters.Text ("Sadie Person",0,220,"hotpink")
message2 = codesters.Text ("Have an Amazing day!",0,-220,"navy")