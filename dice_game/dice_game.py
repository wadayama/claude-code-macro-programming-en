#!/usr/bin/env python3
"""Simple dice game controller for PoC."""

import random
import subprocess
import sys
from variable_db import VariableDB, save_variable, get_variable


def run_macro(macro_file):
    """Run macro file using Claude CLI."""
    with open(macro_file, 'r', encoding='utf-8') as f:
        subprocess.run(["claude", "-p", "--dangerously-skip-permissions"], stdin=f)


def roll_dice():
    """Roll a fair 6-sided dice."""
    return random.randint(1, 6)


def validate_agent_action():
    """Validate agent's action and return parsed values."""
    action = get_variable("action")
    bet_amount_str = get_variable("bet_amount")
    target_number_str = get_variable("target_number")
    current_assets = int(get_variable("assets"))
    
    # Validate action
    if action not in ["even_bet", "specific_number_bet", "pass"]:
        save_variable("game_status", f"ERROR: Invalid action '{action}'")
        sys.exit(1)
    
    # Parse and validate bet_amount
    try:
        bet_amount = int(bet_amount_str) if bet_amount_str else 0
    except ValueError:
        save_variable("game_status", f"ERROR: Invalid bet_amount '{bet_amount_str}'")
        sys.exit(1)
    
    # Validate bet_amount range
    if action != "pass" and (bet_amount < 1 or bet_amount > current_assets):
        save_variable("game_status", f"ERROR: Invalid bet_amount {bet_amount} (assets: {current_assets})")
        sys.exit(1)
    
    # Parse and validate target_number
    target_number = None
    if action == "specific_number_bet":
        try:
            target_number = int(target_number_str) if target_number_str else 0
        except ValueError:
            save_variable("game_status", f"ERROR: Invalid target_number '{target_number_str}'")
            sys.exit(1)
        
        if target_number < 1 or target_number > 6:
            save_variable("game_status", f"ERROR: Invalid target_number {target_number}")
            sys.exit(1)
    
    return action, bet_amount, target_number


def calculate_payout(action, bet_amount, target_number, dice_result, is_final_round):
    """Calculate payout based on game rules."""
    if action == "pass":
        return 0
    
    if action == "even_bet":
        if dice_result in [2, 4, 6]:  # Win
            if is_final_round:
                return bet_amount * 3  # Final round: 4x payout = 3x profit
            else:
                return bet_amount * 1  # Normal round: 2x payout = 1x profit
        else:  # Loss
            return -bet_amount
    
    if action == "specific_number_bet":
        if dice_result == target_number:  # Win
            if is_final_round:
                return bet_amount * 9  # Final round: 10x payout = 9x profit
            else:
                return bet_amount * 4  # Normal round: 5x payout = 4x profit
        else:  # Loss
            return -bet_amount
    
    return 0


def play_round(round_num):
    """Play one round of the game."""
    current_assets = int(get_variable("assets"))
    save_variable("round", str(round_num))
    
    # Run agent
    run_macro("agent_action.md")
    action, bet_amount, target_number = validate_agent_action()
    
    # Create action description
    if action == "pass":
        action_desc = "PASS"
    elif action == "even_bet":
        action_desc = f"EVEN_BET({bet_amount})"
    else:
        action_desc = f"NUMBER_BET({bet_amount},#{target_number})"
    
    # Roll dice and calculate result
    dice_result = roll_dice()
    is_final = (round_num == 10)
    payout = calculate_payout(action, bet_amount, target_number, dice_result, is_final)
    new_assets = current_assets + payout
    save_variable("assets", str(new_assets))
    
    # Determine result
    if payout > 0:
        result = "WIN"
    elif payout < 0:
        result = "LOSS"
    else:
        result = "NO_CHANGE"
    
    # Save game status
    final_flag = " FINAL" if is_final else ""
    save_variable("game_status", f"R{round_num} | {action_desc} | Dice:{dice_result} | {result} | Assets:{current_assets}→{new_assets}{final_flag}")
    
    # Check bankruptcy
    if new_assets <= 0:
        save_variable("game_status", f"R{round_num} | BANKRUPTCY | Assets: 0 | GAME_OVER")
        return False
    
    return True


def main():
    """Main game controller."""
    # Initialize
    db = VariableDB()
    db.clear_all()
    save_variable("assets", "20")
    save_variable("game_status", "GAME START: 20 chips, Goal: 30+ chips")
    
    # Play 10 rounds
    for round_num in range(1, 11):
        if not play_round(round_num):
            return  # Game ended early due to bankruptcy
    
    # Final result
    final_assets = int(get_variable("assets"))
    
    if final_assets >= 30:
        save_variable("game_status", f"GAME END: VICTORY! Final: {final_assets} chips")
    else:
        save_variable("game_status", f"GAME END: DEFEAT. Final: {final_assets} chips (short by {30 - final_assets})")


if __name__ == "__main__":
    main()