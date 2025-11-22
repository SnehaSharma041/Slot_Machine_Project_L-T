import random
from symbols import symbols
from payout import calculate_payout

def spin():
    return random.choice(symbols), random.choice(symbols), random.choice(symbols)

def play():
    balance = 100
    print("🎰 Slot Machine Game 🎰")
    print("Starting Balance:", balance)

    while balance > 0:
        print("\nYour Balance:", balance)

        bet = int(input("Enter bet amount (0 to quit): "))

        if bet == 0:
            print("Exiting the game. Final Balance:", balance)
            break

        if bet > balance:
            print("You don't have enough money!")
            continue

        s1, s2, s3 = spin()
        print(f"\nSpinning...  {s1} | {s2} | {s3}")

        payout, message = calculate_payout(bet, s1, s2, s3)
        balance = balance - bet + payout

        print(message)
        print("You won:", payout)
