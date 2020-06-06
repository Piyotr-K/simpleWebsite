from tkinter import *
import time
from GameDisplay import GameDisplay

root = Tk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()

canvas = Canvas(root, background="grey", width=w, height=h)
canvas.pack()

game = GameDisplay(canvas)
for seq in ['<Any-KeyPress>']:
    root.bind_all(seq, game.update_bat)

root.title("Bouncing Game")
root.wait_visibility(canvas)
root.wm_attributes('-alpha', 1.0)
root.resizable(0, 0)

# Custom mainloop
while 1:
    root.update_idletasks()
    root.update()
    game.update()
    time.sleep(0.01)
