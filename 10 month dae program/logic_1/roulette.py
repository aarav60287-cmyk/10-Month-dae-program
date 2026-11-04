import random

red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

money = 100
print("ROULETTE - you start with $100")
print("Good luck!")
print("Place your bets!")
print("The minimum bet is $1")
print("Zero is green!")
print("Red and black pay 1 to 1")
print("A correct number pays 35 to 1")

while money > 0:
    print("\nMoney:", money)
    bet = int(input("How much do you bet? "))

    if bet > money or bet < 1:
        print("Invalid bet")
        continue

    choice = input("Bet on red, black, or a number (0-36): ")

    number = random.randint(0, 36)

    if number == 0:
        color = "green"
    elif number in red_numbers:
        color = "red"
    else:
        color = "black"

    print("The ball landed on", number, color)

    if choice == color:
        money = money + bet
        print("You win!")
    elif choice == str(number):
        money = money + bet * 35
        print("JACKPOT!")
    else:
        money = money - bet
        print("You lose.")

print("Game over. You have $" + str(money))
print("Thanks for playing roulette!")
print("You can always try again!")