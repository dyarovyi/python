# DEC 3, 2021 - dyarovyi
# This is the roshambo app

# README

import random 

class Program:
    def get_user():
        while True:
            choice = input("Enter R, P or S: ").capitalize()
            if choice == 'R':
                return "Rock"
            elif choice == "P":
                return "Paper"
            elif choice == "S":
                return "Scissors"
            else:
                print("ERROR: invalid value was entered.")

    def get_machine():
        return random.choice(("Rock", "Paper", "Scissors"))

    def play(self):
        user = self.get_user()
        machine = self.get_machine()

        if user == machine:
            print("It's a tie!")
        else:
            print("Machine chose {}".format(machine))

P = Program
P.play(P)