# Slot Machine Game (Python Console Project)

## Introduction
The **Slot Machine Game** is a simple yet engaging Python console-based project that simulates a real slot machine experience.  
This project demonstrates the use of **functions, randomness, loops, modular programming, and basic game logic**.  
It is perfect for beginners who want to understand how games work behind the scenes without any frontend or GUI.

---

## Features
-  Random symbol generation using Python’s `random` module  
-  Virtual balance system to manage bets and winnings  
-  Jackpot detection when all symbols match  
-  Continuous gameplay until the balance becomes zero or the player quits  
-  Clean modular structure with separate files for game logic, payouts, and symbols  
-  Easy to expand with more symbols, difficulty levels, or advanced animations

---

## How It Works
1. The player starts with a **default balance** (e.g., 100 credits).  
2. The player enters a **bet amount** before each spin.  
3. Three symbols are randomly selected from a predefined list.  
4. The payout is calculated based on:
   - **3 symbols match → Jackpot (x5 payout)**
   - **2 symbols match → Small Win (x2 payout)**
   - **No match → Bet lost**
5. The balance updates after each round.  
6. The player may continue, place new bets, or quit the game.

---

## Game Rules
- Minimum bet must be **greater than 0**.
- Player cannot bet more than their current balance.
- Payout Rules:
  - **Three matching symbols → Win 5× your bet**
  - **Two matching symbols → Win 2× your bet**
  - **No match → Lose your bet**
- The game ends when:
  - The player enters **0** to quit, or  
  - Balance reaches **0**

---

## Project Structure
```bash

slot_machine_project/
│
├── src/
│   ├── main.py        # Entry point of the program
│   ├── game.py        # Game loop and user interaction
│   ├── payout.py      # Payout calculations and logic
│   └── symbols.py     # List of available symbols
│
└── README.md          # Project documentation
```

---

## Technology Used
- Python 3.x
- VS Code (for development)
- Random module (built-in)
- Terminal / Command-line execution

---
## Author 

| Field        | Details                                                                                                    |
| ------------ | ---------------------------------------------------------------------------------------------------------- |
| **Name**     | Sneha Sharma                                                                                               |
| **LinkedIn** | [www.linkedin.com/in/sneha-sharma-90012b296]                                                              |
| **Email**    | [snehasnehasharma0918@gmail.com](mailto:snehasnehasharma0918@gmail.com)                                                              |
