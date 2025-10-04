import tkinter as tk
import time

# --- יצירת חלון ---
root = tk.Tk()
root.title("Hala Madrid!")
root.geometry("800x400")
root.configure(bg="black")

canvas = tk.Canvas(root, width=800, height=400, bg="black", highlightthickness=0)
canvas.pack()

title = "HALA MADRID"
letters = []

# צבעים בסגנון ריאל מדריד (זהב ולבן)
colors = ["#FFD700", "white"]

# מחשבים מיקום התחלתי כדי למרכז את הכיתוב
letter_spacing = 60
text_width = letter_spacing * len(title)
x_start = (800 - text_width) // 2 + 30
y_pos = 200

# יצירת האותיות
for i, char in enumerate(title):
    letter = canvas.create_text(x_start + i * letter_spacing, y_pos, text=char,
                                font=("Helvetica", 60, "bold"), fill="black")
    letters.append(letter)

# --- אפקט הופעה הדרגתית ---
for i, letter in enumerate(letters):
    root.update()
    time.sleep(0.2)
    canvas.itemconfig(letter, fill=colors[i % 2])
    canvas.scale(letter, 400, 200, 1.3, 1.3)
    root.update()
    time.sleep(0.1)
    canvas.scale(letter, 400, 200, 1/1.3, 1/1.3)
    root.update()

# --- אפקט סיום נוצץ ---
for i in range(3):
    for color in colors:
        canvas.config(bg=color)
        root.update()
        time.sleep(0.1)
    canvas.config(bg="black")

# טקסט סיום
canvas.create_text(400, 350, text="¡Vamos Real Madrid!", font=("Helvetica", 22, "italic"), fill="white")

root.mainloop()