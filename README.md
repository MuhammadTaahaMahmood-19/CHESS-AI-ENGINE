# ♟️ AI Chess Engine with Pygame GUI

This project is a simple chess engine built in Python that allows you to play as **White** against an AI opponent playing as **Black**. The AI uses the **Minimax algorithm** with alpha-beta pruning and a material-based evaluation function. The interface is built using **Pygame**.

---

## 🎮 Features

- Play chess with a graphical board (Pygame)
- Human vs AI (you play as White)
- AI uses Minimax (depth-limited search)
- Loads clean SVG-to-PNG Wikipedia-style chess piece graphics
- Legal moves enforced

---

## 🖥️ Requirements

- Python 3.7+
- `pygame`
- `python-chess`

Install dependencies:

```bash
python3 -m pip install pygame python-chess
```

---

## 🚀 How to Run

```bash
python3 chess_gui.py
```

Click a white piece, then click a valid square. The AI will automatically reply.

---

## 📁 File Structure

```
CHESS_ENGINE_AI/
├── chess_ai.py        # Minimax engine logic
├── chess_gui.py       # Pygame board + input
├── assets/            # Folder with 12 PNG chess piece images
│   ├── white_pawn.png
│   ├── black_pawn.png
│   └── ...
├── README.md
├── .gitignore
```

---

## 🧠 AI Logic

- Based on **Minimax** algorithm with **alpha-beta pruning**
- Evaluation function considers only **material balance**
- Adjustable search depth (currently set to 2)

---

## 📸 Screenshot of the board


<img width="638" alt="Screenshot 2025-07-03 at 16 01 02" src="https://github.com/user-attachments/assets/59405a24-d8b4-4fcd-abf8-f090fc92f286" />



## 🙋‍♂️ Author

Made with ❤️ by Muhammad Taaha Mahmood




---

## 🚧 More updates on the way!

Planned enhancements:
- ✅ Move highlighting
- 🔁 Undo/redo support
- ⏱️ Timer/clock system
- 🌐 Multiplayer mode
- 🧠 Stronger AI with positional evaluation

Stay tuned and star the repo to follow updates!
