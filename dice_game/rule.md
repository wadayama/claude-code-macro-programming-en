# Game Rules: Dice Game

## 1. Overview
A strategic simulation game where the player (AI agent) autonomously manages risk within limited assets and rounds, dynamically changing strategies according to situations while aiming to achieve the ultimate goal.

## 2. Game Objective
- **Initial Assets**: 20 chips
- **Total Rounds**: 10 rounds
- **Victory Condition**: Total assets of 30 chips or more at the end of the final round (10th game).

## 3. Game Termination Conditions
One set of the game ends when any of the following conditions are met:
- All 10 rounds are completed.
- Total assets reach 0 during any round (bankruptcy).

## 4. Game Flow (One Round Process)
Each round proceeds with the following steps:

1. **Situation Check**: The player is informed of the "current round number" and "current total assets".

2. **Strategic Decision**: The player analyzes the situation and chooses one of the following three options:
   - A) Even Bet: Decide bet amount and place bet.
   - B) Specific Number Bet: Decide the number to bet on (1-6) and bet amount.
   - C) Pass: No betting is performed in this round.
   
   ※Bet amounts can be freely decided as integers ranging from 1 chip to the current total assets.

3. **Dice Roll**: One fair dice with faces 1-6 is rolled.

4. **Result Determination**: Win/loss is determined based on the dice outcome and player's choice.

5. **Asset Update**: Player's total assets are updated based on win/loss, bet amount, and payout multiplier.

## 5. Betting Types and Payouts
Payouts differ between normal rounds and the final bonus round. Payout refers to the total amount returned including the bet amount.

### Normal Rounds (Rounds 1-9)

| Bet Type | Win Condition | Win Rate | Payout (Return) | Expected Profit |
|----------|---------------|----------|-----------------|-----------------|
| Even Bet | Roll {2, 4, 6} | 50.0% | 2x | 1x bet amount | 0% |
| Specific Number Bet | Roll specified number | 16.7% | 5x | 4x bet amount | -16.7% |

### Final Bonus Round (Round 10)
Only in the final round, all payouts are doubled.

| Bet Type | Win Condition | Win Rate | Payout (Return) | Expected Profit |
|----------|---------------|----------|-----------------|-----------------|
| Even Bet | Roll {2, 4, 6} | 50.0% | 4x | 3x bet amount | +100% |
| Specific Number Bet | Roll specified number | 16.7% | 10x | 9x bet amount | +66.7% |

## 6. Instructions for Player (Agent)
Your objective is to achieve 30 chips or more in total assets at the end of 10 rounds.

Variable descriptions:
- At the start of each round, information is provided in the format `{"round": current_round_number, "assets": current_total_assets}`.
- You should decide your action in the format `{"action": "choice", "bet_amount": bet_amount, "target_number": number}`.
  - `action` is one of `"even_bet"`, `"specific_number_bet"`, `"pass"`.
  - `bet_amount` is the number of chips to bet (0 for pass).
  - `target_number` is the number 1-6 to specify for specific number bets.