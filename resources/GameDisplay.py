try:
    import Tkinter, random, time, sys
except:
    import tkinter as Tkinter, random, time, sys

class GameDisplay:

    def __init__(self, canvas):
        self.canvas = canvas
        self.widthlimit = canvas.winfo_screenwidth()
        self.heightlimit = canvas.winfo_screenheight()

        # Where to create the bat
        y2 = canvas.winfo_screenheight() - 70
        y1 = y2 - 15

        self.bat = Tkinter.Canvas.create_rectangle(canvas, 0, y1, 200, y2, fill="steelblue")
        self.ball = Tkinter.Canvas.create_oval(canvas, 0, 0, 50, 50, fill="lightgreen")

        self.xvelocity = 10
        self.yvelocity = 10

    def update(self, event=None):
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        a, b, c, d = self.canvas.coords(self.bat)
        k = len(self.canvas.find_overlapping(a, b, c, d))

        if x1 < 0:
            self.xvelocity = 2
            self.canvas.move(self.ball, self.xvelocity, 0)
            pass
        elif y2 >= self.heightlimit:
            x = self.widthlimit / 2
            y = self.heightlimit / 2

            self.canvas.create_text(x, y, text='Game Over', font='arial 50 bold', fill='red')

            self.canvas.master.update()
            self.canvas.master.update_idletasks()

            time.sleep(2)
            self.canvas.master.destroy()
            sys.exit(0)
        elif x2 >= self.widthlimit:
            self.xvelocity = -2
            self.canvas.move(self.ball, self.xvelocity, 0)
        elif y1 <= 0:
            self.yvelocity = 2
            self.canvas.move(self.ball, 0, self.yvelocity)
        elif k == 2:
            self.yvelocity = -2
            self.canvas.move(self.ball, 0, self.yvelocity)
        else:
            self.canvas.move(self.ball, self.xvelocity, self.yvelocity)
        pass

    def update_bat(self, event=None):
        direction = event.keysym
        x1, y1, x2, y2 = self.canvas.coords(self.bat)
        if x2 > self.widthlimit:
            if direction == 'Left':
                self.canvas.move(self.bat, -20, 0)
                pass
        elif x1 < 0:
            if direction == 'Right':
                self.canvas.move(self.bat, 20, 0)
                pass
        elif direction == 'Right':
            self.canvas.move(self.bat, 20, 0)
        elif direction == 'Left':
            self.canvas.move(self.bat, -20, 0)
        else:
            pass
