# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 18:17:00 2020

@author: Sara
"""

questions = ["\n🎶I believe I can ___🎶\n",
             "\n🎶All I ____ for Christmas is you🎶\n",
             "\n🎶If you liked it, then you should have put a ____ on it🎶\n",
             "\n🎶Somewhere over the _______🎶\n",
             "\n🎶I knew you were _______ when you walked in🎶\n"]

answers = ["fly", "want", "ring", "rainbow", "trouble"]

positive_comments = ["Wow! You are good!",
                     "Nice! Keep it up!",
                     "Correct!",
                     "Amazing! Almost there!",
                     "PERFECT!!"]
other_comments = ["Wrong!",
                  "Incorrect!",
                  "Try harder next time!",
                  "Oops! You're wrong.",
                  "Too bad."]
correct = 0
user_ans = []
i = 0
score = 0
# print(len(questions))

print("Music Quiz")
print("Take this quiz and guess the missing lyrics!")

name = input("Please enter your name:\t")
print("\nHi" + "," + " " + name.title() + "!")


def final_part(answers, score):
    score = len(user_ans)
    print("\nYou got", score, "out of", len(questions))
    if score == len(questions):
        print("\nPerfect! You did a really great job!")
    elif score >= 3:
        print("\nNice score! Well done.")
    else:
        print("\nTry harder next time.")


def start_game(correct):
    print("\nYay! Here's the first question.")
    while correct < 5:
        print("\n" + str(questions[correct]))
        player_answers = input("Your answer:")
        if player_answers.title() == answers[correct].title():
          print(positive_comments[correct].title())
          user_ans.append(1)
          correct = correct + 1
        else: 
          print(other_comments[correct].title())
          correct = correct + 1


choice = ''

while choice != 'Bye':
    print("\nPlease type Go to start,")
    print("or Bye to quit.")

    choice = input("\nPlease choose.. ")
    if choice == 'Go':
        start_game(correct)
    elif choice == 'Bye':
        print("\nSee you next time!\n")
    else:
        print("\nI don't understand that choice, please try again.\n")
    break

final_part(answers, score)
