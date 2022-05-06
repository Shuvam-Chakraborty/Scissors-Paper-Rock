import random
print("Instructions :\nScissors : 'S'\nPaper : 'P'\nRock : 'R'\n")
turn = 0
you = 0
comp = 0
draw = 0
while turn < 10:
    lst = ['S', 'P', 'R']
    choice = random.choice(lst)
    print("Turn", turn + 1, ":")
    your_input = str(input("Enter your choice : ")).capitalize()
    if your_input in lst:
        if choice == your_input:
            if choice == 'S':
                print("You have entered Scissors.\nComputer has entered Scissors.\nDraw this time.")
            elif choice == 'P':
                print("You have entered Paper.\nComputer has entered Paper.\nDraw this time.")
            elif choice == 'R':
                print("You have entered Rock.\nComputer has entered Rock.\nDraw this time.")
            turn += 1
            draw += 1
        if choice == 'S':
            if your_input == 'R':
                print("You have entered Rock.\nComputer has entered Scissors.\nYou won.")
                turn += 1
                you += 1
            elif your_input == 'P':
                print("You have entered Paper.\nComputer has entered Scissors.\nComputer won.")
                turn += 1
                comp += 1
        elif choice == 'R':
            if your_input == 'S':
                print("You have entered Scissors.\nComputer has entered Rock.\nComputer won.")
                turn += 1
                comp += 1
            elif your_input == 'P':
                print("You have entered Paper.\nComputer has entered Rock.\nYou won.")
                turn += 1
                you += 1
        elif choice == 'P':
            if your_input == 'S':
                print("You have entered Scissors.\nComputer has entered Paper.\nYou won.")
                turn += 1
                you += 1
            elif your_input == 'R':
                print("You have entered Rock.\nComputer has entered Paper.\nComputer won.")
                turn += 1
                comp += 1
        print("\n")
    else:
        print("Invalid input.\nTry again.\n")

print("\nScore :\nYou :", you, "\nComputer :", comp, "\nDraw : ", draw, "\n")
print("Final result:")
if you > comp:
    print("You have won. Congratulations!!!")
elif you < comp:
    print("Computer has won. Better luck next time!!!")
elif you == comp:
    print("Oops it's a draw.")
