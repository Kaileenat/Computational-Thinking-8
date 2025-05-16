# Beginning: Create variables
giraffe_points = 0
dog_points = 0

# Middle: Ask questions 
answer = input ("Which one you like better A) zoos, or B) pet stores?")
if answer == "A":
    giraffe_points += 1
elif answer == "B" :
    dog_points += 1


answer = input ("do you like A) outdoor pets, or B) indoor pets?")
if answer == "A":
    giraffe_points += 1
elif answer == "B" :
    dog_points += 1

    
answer = input ("would you rather have A) tall, or B) short?")
if answer == "A":
    giraffe_points += 1
elif answer == "B" :
    dog_points += 1
   
   

answer = input ("would you want A) spots, or B) one color?")
if answer == "A":
        giraffe_points += 1
elif answer == "B" :
    dog_points += 1


answer = input ("Are you A) quiet , or B) loud ?")
if answer == "A":
        giraffe_points += 1
elif answer == "B" :
    dog_points += 1

#End: determine results
if giraffe_points > dog_points:
     print("You are a giraffe person")
elif dog_points > giraffe_points:
     print("You are a dog person")
elif giraffe_points == dog_points:
     print("You like giraffe and dogs the same")
    
