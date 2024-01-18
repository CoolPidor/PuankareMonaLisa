import tkinter as tk
from tkinter import scrolledtext
import random, string

class InfinitePInsertionApp:
    def __init__(self, win):
        self.win = win
        self.win.title("GenShekspir")
        
        self.entry_text = tk.StringVar()
        self.entry_text.trace_add('write', self.on_entry_change)

        self.entry = scrolledtext.ScrolledText(win, wrap=tk.WORD, font=('Arial', 12), height=10)
        self.entry.pack(fill=tk.BOTH, expand=True)

        self.start_button = tk.Button(win, text="Start", command=self.start_insertion)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(win, text="Stop", command=self.stop_insertion, state=tk.DISABLED)
        self.stop_button.pack(side=tk.RIGHT, padx=10)

        self.is_inserting = False
        self.infinite_insertion()

    def on_entry_change(self, *args):
        if len(self.entry.get('1.0', tk.END)) > 1:
            self.entry.delete('1.0', tk.END)

    def infinite_insertion(self):
        if self.is_inserting:
            self.entry.insert(tk.END, random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ.,!?;1234567890 \n'))
            self.win.after(5, self.infinite_insertion)

    def start_insertion(self):
        self.is_inserting = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.infinite_insertion()

    def stop_insertion(self):
        self.is_inserting = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

win = tk.Tk()
app = InfinitePInsertionApp(win)
win.geometry("500x400")
win.mainloop()
