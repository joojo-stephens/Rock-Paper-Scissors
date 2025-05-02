# Rock–Paper–Scissors

A simple, console-based Python game where the computer randomly chooses rock, paper, or scissors each round, and you have three rounds to try to beat it.

## Description

This script implements a “Rock–Paper–Scissors” game:

1. The `options` list holds the valid moves: `"rock"`, `"paper"`, `"scissors"`.  
2. It loops for three rounds (`for round_num in range(1, 4)`), displaying the current round number.  
3. Each round:
   - The computer picks a random move:  
     ```python
     my_move = random.choice(options)
     ```
   - The player is prompted:  
     ```
     Choose one (rock, paper, scissors):
     ```  
     and their input is normalized with `.strip().lower()`.  
   - If the input isn’t one of the options, it prints an error and uses `continue` to skip to the next round.  
   - If moves match, it prints a tie message.  
   - Otherwise, it prints a win or loss message based on the rules:
     - Rock beats scissors  
     - Paper beats rock  
     - Scissors beats paper  
4. After three rounds, it prints a “Game over!” message.

No external dependencies beyond Python’s standard library.

## Features

- Three rounds of play  
- Random computer move each round  
- Input validation with retries  
- Clear tie/win/lose feedback  

## Requirements

- Python 3.x

## Usage

1. **Clone** the repository:  
   ```bash
   git clone https://github.com/yourusername/rock-paper-scissors.git
   cd rock-paper-scissors
