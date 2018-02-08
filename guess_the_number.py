
import random
random_number = random.randint(1, 10)

print "I am thinking on a number between 1-10"
number = int(raw_input('What is my number? '))

while number == random_number:
    print "You Win!!!"
    play = raw_input("Do you want to play again (Y or N)?")
    if play == "N" or play == "n":
        print "Bye Bye see you next time!"
        break
    if play == "Y" or play == "y":
        random_number = random.randint(1, 10) 
        number = int(raw_input('What is my number? '))
     
i = 4
while i > -1:
    
    if number != random_number:
        
        if number > random_number:
            print "its too high try again you have " + str(i) + " times more"
            number = int(raw_input('What is my number? '))
            i = i - 1
            
            if i == 0:
                print "You lost!!!"
                play = raw_input("Do you want to play again (Y or N)?")
                
                if play == "N" or play == "n":
                    print "Bye Bye see you next time!"
                    break
                
                if play == "Y" or play == "y":
                    i = 4
                    random_number = random.randint(1, 10) 
                    number = int(raw_input('What is my number? '))  

        elif number < random_number:
            print "its too low try again you have " + str(i) + " times more"
            number = int(raw_input('What is my number? '))
            i = i - 1
            
            if i == 0:
                print "You lost!!!"
                play = raw_input("Do you want to play again (Y or N)?")
                
                if play == "N" or play == "n":
                    print "Bye Bye see you next time!"
                    break
               
                if play == "Y" or play == "y":
                    i = 4
                    random_number = random.randint(1, 10) 
                    number = int(raw_input('What is my number? '))
        
    else:
        print "You Win!!!"   
        play = raw_input("Do you want to play again (Y or N)?")
                
        if play == "N" or play == "n":
            print "Bye Bye see you next time!"
            break
        
        if play == "Y" or play == "y":
            i = 4
            random_number = random.randint(1, 10) 
            number = int(raw_input('What is my number? '))



#test


 