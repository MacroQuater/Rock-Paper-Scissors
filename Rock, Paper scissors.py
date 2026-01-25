
'''Rock paper scissors'''

#input value: rock paper or scissors
#output will be rock paper or scissors
#relationship: if user input rock, computer outputs rock draw,
#if computer outputs scissors, user win,
# if computer outputs paper, computer wins

def user_input():
    
    u_in = input("Pick one option, rock, paper or scissors: " )
    u_in =''.join(u_in.split()).lower()
    if  u_in == "rock" or u_in == "paper" or  u_in =="scissors":
        return u_in
    else:
        return f"Input value {u_in} is not specified as an option in the program,\nPlease try again."
        
def gen_random():
    import random
    return random.choice(["0","1"])
    
def calc1(u_in,gen_random):
    
    
    if gen_random == ["0"]:
        # Ai wins
        if u_in == "rock":
            a = "paper"
            return a
        elif u_in == "paper":
            b = "scissors"
            return b
        else:
            c = "rock"
            return c
    else:
        # User wins ["1"]
        if u_in == "rock":
            b = "scissors"
            return b
        elif u_in == "paper":
            c = "rock"
            return c
        else:
            a = "paper"
            return a


# def calc2(u_in, ai,gen_random):
#     
#     if gen_random == ["0"]:
#         # Ai wins
#         if 
        
def main():
    
    calc1(user_input(),gen_random())
    
print(main())
