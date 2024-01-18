from random import randint, seed
import time
from PIL import Image, ImageTk
import tkinter as tk

delay = 100


def gen_photo():
    width, height = 500, 500
    image = Image.new('RGB', (width, height), 'white')
    pixels = image.load()
    for i in range(width):
        for j in range(height):
            pixels[i, j] = (randint(0, 255), randint(0, 255), randint(0, 255))
    image.save('images/img.jpg')
    return 'images/img.jpg'


def repeat():
    global canvas, mimage
    canvas.delete("all")
    mimage = ImageTk.PhotoImage(Image.open(gen_photo()))
    canvas.create_rectangle(0, 0, win.winfo_screenwidth(), win.winfo_screenheight(), fill="gray")
    canvas.create_image((win.winfo_screenwidth() - mimage.width()) // 2,
                        (win.winfo_screenheight() - mimage.height()) // 2,
                        anchor=tk.NW,
                        image=mimage)
    win.after(delay, repeat)

win = tk.Tk()
win.title("Mona Lisa")
win.attributes('-fullscreen', True)
canvas = tk.Canvas(win, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
canvas.pack()

win.after(delay, repeat)
win.mainloop()
