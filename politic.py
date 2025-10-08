import tkinter as tk

# יצירת חלון ראשי
window = tk.Tk()
window.title("בחירת מפלגה")
window.geometry("600x400")
window.config(bg="#f0f0f0")

def show_menu():
    # ניקוי המסך
    for widget in window.winfo_children():
        widget.destroy()

    # כפתור ליכוד
    likud_btn = tk.Button(window, text="הליכוד", font=("Arial", 20, "bold"),
                          bg="#1a1aff", fg="white", width=15, height=2,
                          command=lambda: show_text("בנימין נתניהו", "#1a1aff"))
    likud_btn.pack(pady=30)

    # כפתור יש עתיד
    yesh_atid_btn = tk.Button(window, text="יש עתיד", font=("Arial", 20, "bold"),
                              bg="#ffcc00", fg="black", width=15, height=2,
                              command=lambda: show_text("בוגד", "#ffcc00"))
    yesh_atid_btn.pack(pady=10)

def show_text(text, color):
    # ניקוי המסך
    for widget in window.winfo_children():
        widget.destroy()
    label = tk.Label(window, text=text, font=("Arial", 60, "bold"), fg=color, bg="#f0f0f0")
    label.pack(expand=True)
    # אחרי 3 שניות חוזר לתפריט
    window.after(3000, show_menu)

# הפעלת המסך הראשי
show_menu()
window.mainloop()