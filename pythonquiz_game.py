print(" Welcome to my python quiz game! ")
print(" Answer the following questions to test your python knowledge. ")
print(" It should be noted that the object of this quiz is to illustrate my basic understanding of python, and my ability to make a working application however rudimentary.")
print(" Good luck! and have fun :)")

while True: 
    playing = input(" Are you sure you want to play? type 'yes' ").lower()

    if playing != "yes":
        quit()

    print("Perfect, let's get this party started")

    answer = input("What is python? A) A snake B) A programming language C) A type of food D) A type of car ").lower()
    if answer == "b":
        print(" Correct! you're the best!!")
    else:
        print(" BOO! INCORRECT. YOU'RE WRONG BUDDY!")

    answer = input("Who created python? A) Guido van Rossum B) Elon Musk C) Bill Gates D) Mark Zuckerberg ").lower()
    if answer == "a":
        print(" Correct! you're the best!!")
    else:
        print(" BOO! INCORRECT. YOU'RE WRONG BUDDY!")

    answer = input("What is the capital of France? A) Paris B) London C) New York D) Berlin ").lower()
    if answer == "a":
        print(" Correct! you're the best!!")
    else:
        print(" BOO! INCORRECT. YOU'RE WRONG BUDDY!")

    answer = input("What is RAM? A) A type of food B) A type of computer memory C) A type of car D) A type of animal ").lower()
    if answer == "b":
        print(" Correct! you're the best!!")
    else:
        print(" BOO! INCORRECT. YOU'RE WRONG BUDDY!")

    answer = input("What is a CPU? A) A type of food B) A type of part C) A type of car D) A type of animal ").lower()
    if answer == "b":
        print(" Correct! you're the best!!")
    else:
        print(" BOO! INCORRECT. YOU'RE WRONG BUDDY!")

    print(" Thank you for playing my python quiz game! ")
    print(" I hope you had fun! ")

    decision = input(" Do you want to play again? type 'yes' ").lower()
    if decision != "yes":
        print("Thank you for playing my python quiz game!")
        break