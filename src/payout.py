def calculate_payout(bet, s1, s2, s3):
    if s1 == s2 == s3:
        return bet * 5, "JACKPOT! 🎉"
    elif s1 == s2 or s2 == s3 or s1 == s3:
        return bet * 2, "Nice! You got a pair!"
    else:
        return 0, "No match. Try again!"
