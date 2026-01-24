
'''Rock paper scisors'''

#input value: rock paper or scissors
#output will be rock paper or scissors
#relationship: if user input rock, computer outputs rock draw,
#if computer outputs scissors, user win,
# if computer outputs paper, computer wins

#Note any option that says (s c i s s Ors), bassically if it spells out scissors it's
# okay wether its captial or not, likewise with any other option 

# x = input("Pick an option, Rock, Paper or Scissors :")
# x = str(x)
# if x != "rock" or "scissors" or "rock":
#     print("There are no options like that")
# else:
#     print("Yes")

a = input("what would you like to play, rock paper of scissors.: " )

# def import_random():
#     import random
#     x = ["0","1"]
#     random.shuffle(x)
#     return x
    
def calc():
    import random
    x = ["0","1"]
    random.shuffle(x)
    
    x_ = ["0","1"]
    if x_ == x:
        # Hard mode
        if a == "rock":
            print("paper")
            
        elif a == "paper":
            print("scissors")
            
        else:
            print("rock")
            
    else:
        # Easy mode ["1","0"]
        if a == "rock":
            print("scissors")
             
        elif a == "paper":
            print("rock")
        
        else:
            print("paper")
        
calc()
