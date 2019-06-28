print("Welcome to number guessor!")
print("Select your range in which you want the computer to guess your number.") 
low = float(input("Enter the lower range number: "))
high = float(input("Enter the higher range number: "))

print("Please think of a number between " + str(low) + " and " + str(high) + "!")

guessed = False

while not guessed:
    ans = (high + low)//2
    print("Is your secret number " + str(ans)+ "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if response == 'c':
        guessed = True
        
    elif response == 'h':
        high = ans
        
    elif response == 'l':
        low = ans
        
    else:
        print("Sorry, I did not understand your input.")
print('Game over. Your secret number was: ' + str(ans))
print("Thank You for using this program")
