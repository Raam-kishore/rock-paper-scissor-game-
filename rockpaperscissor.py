
import random
game_choices =["scissor","rock","paper"]
user_point=0
computer_point=0
for i in range(0,6) :
 print("Enter your choice")
 user_choice=input()
 computer_choice=random.choice(game_choices)
 print("the computer choice is :",computer_choice)
 if computer_choice=="rock" and user_choice=="paper":
    print("you win as paper cover rocks")
    user_point=user_point+1
 elif computer_choice=="paper" and user_choice=="rock":
    print("you lose as paper cover rocks")
    computer_point=computer_point+1
 elif computer_choice=="scissor" and user_choice=="paper":
    print("you lose as scissor cuts paper")
    computer_point=computer_point+1
 elif computer_choice=="paper" and user_choice=="scissor":
    print("you win as scissor cuts paper")
    user_point=user_point+1
 elif computer_choice=="scissor" and user_choice=="rock":
    print("you lose as rock broke scissor")
    user_point=user_point+1
 elif computer_choice=="rock" and user_choice=="scissor":
    print("you lose as rock broke scissor")
    computer_point=computer_point+1
 elif computer_choice=="scissor" and user_choice=="rock":
    print("you win as rock broke scissor")
    user_point=user_point+1


print("you point is",user_point)
print("computer point is ",computer_point)
if user_point==computer_point :
    print("the game is tied")
elif user_point>computer_point :
    print("you won the game")
elif user_point<computer_point :
    print("you lose the game")




