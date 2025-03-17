###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")


q1 = codesters.Square (100, 100, 200, 'pink')
q2 = codesters.Square (-100, 100, 200, 'AliceBlue')
q3 = codesters.Square (-100, -100, 200, 'LightCyan')
q4 = codesters. Square (100, -100, 200, 'MintCream')


s1 = codesters.Sprite ("cardinal", 100, 100)
s2 = codesters.Sprite ("cardinal", -100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite("cardinal", 100, -100)
s3.set_size(0.5)
s4 = codesters.Sprite ("nova", -100, 100)
s4.set_size(0.5)
