number = 23
guess = int(input('Enter a number: '))

if guess == number:
    print("Good")
elif guess < number:
    print('number is greater')
else:
    print('number is lower')