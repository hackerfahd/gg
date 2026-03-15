import tkinter as tk
from tkinter import messagebox
import datetime
import threading
import winsound

def alarm(time_str):
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == time_str:
            winsound.Beep(2000, 1000)  # تردد 2000 لمدة ثانية
            messagebox.showinfo("المنبّه", f"حان الوقت: {now}")
            break

def set_alarm():
    time_str = entry.get()
    if not time_str:
        messagebox.showwarning("خطأ", "يرجى إدخال الوقت بصيغة HH:MM")
        return
    threading.Thread(target=alarm, args=(time_str,), daemon=True).start()
    status.config(text=f"تم ضبط المنبّه على {time_str}")

root = tk.Tk()
root.title("منبّه بسيط")
root.geometry("300x180")

label = tk.Label(root, text="أدخل الوقت (HH:MM):", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

button = tk.Button(root, text="ضبط المنبّه", font=("Arial", 14), command=set_alarm)
button.pack(pady=5)

status = tk.Label(root, text="", font=("Arial", 12))
status.pack(pady=5)

root.mainloop()
