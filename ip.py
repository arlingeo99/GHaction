quest1 = input("What is your name? ")

quest2 = int(
    input(
        "Do you want to uppercase it? If so, enter 1. If you want to lowercase it then enter 2 "
    )
)


if quest2 == 1:
    print(quest1.upper())
elif quest2 == 2:
    print(quest1.lower())
else:
    print("Invalid input")
