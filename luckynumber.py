import random

lucky_number = random.randint(1,50)

print(f'Your lucky number is {lucky_number}') 

fortune_number = random.randint(1,3)

fortune_text = ""

if fortune_number == 1:
    fortune_text = "You are gonna get married this year."
elif fortune_number == 2:
    fortune_text = "You will win a car today"
else:
    fortune_text = "You will win a lottery worth 1 million this year"
print(f'{fortune_text} and your fortune number is {fortune_number}')