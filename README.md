# ❌⭕ GridX

**A classic two-player Tic-Tac-Toe game, playable right in your terminal.**

GridX is a simple, dependency-free Python implementation of Tic-Tac-Toe for two players sharing the same keyboard. Take turns placing X's and O's on a 3x3 grid, and the game automatically detects wins across all eight possible combinations, or calls a tie when the board fills up.

---

## 🎮 Gameplay

- Two players take turns: **X** goes first, then **O**
- The board is numbered 1 through 9, and you enter a number to claim that cell
- The game checks after every move for a win across all rows, columns, and both diagonals
- If the board fills up with no winner, it's declared a tie
- After each round, you're asked whether you'd like to play again

---

## 🛠️ Tech Stack

- **Python 3** — no external libraries or dependencies required

---

## 📁 Project Structure

```
gridx/
├── code.py          # Full game logic
└── README.md
```

---

## ▶️ Getting Started

### Prerequisites
- Python 3 (nothing else needed — pure standard library)

### Running the Game

```
git clone https://github.com/rhitamcoder/gridx.git
```
```
cd gridx
```
```
python code.py
```

Follow the on-screen prompts: enter a number from 1 to 9 to place your mark on the matching cell.

---

## 🧠 How It Works

- **Board representation:** the board is a list of 9 strings, initially numbered `"1"` through `"9"` so players can see which number maps to which cell
- **Move validation:** `get_player_move()` loops until the player enters a number that's still an open cell on the board
- **Win detection:** `check_winner()` checks the board against 8 predefined winning combinations (3 rows, 3 columns, 2 diagonals)
- **Tie detection:** `is_board_full()` checks whether every cell has been claimed by `X` or `O`
- **Game loop:** an outer `while True` loop lets players restart as many rounds as they like until they choose to stop

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
