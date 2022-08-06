import tkinter as T

# Required:
# Change the greeting everytime, something like "Hi John" and then "Hello John"
# Once in a while "S'up John"
# Challenge:
# A custom text option for when they type a certain name
# AND also if they press the click me button 10 times
# it displays a special message

def display_phrase():
    name = ent.get()
    greetLabel.config(text= "Hi " + name)

window = T.Tk()

window.title("My Good App")

# Set window size to 400x400
window.geometry("400x400")

greetLabel = T.Label(master=window, font=("Consolas", 20))
greetLabel.grid(columnspan=2, row=0)

lbl = T.Label(text="What's your name? ", font=("Consolas"))
lbl.grid(column=0, row=1)

ent = T.Entry(font=("Consolas"))
ent.grid(column=1, row=1)

btn = T.Button(text="Click Me", bg="#FFAB00", command=display_phrase)
btn.grid(columnspan=2)

# Big entry box
# txt = T.Text(master=window, height=10, width=30)
# txt.grid()

# Should be the last line for your app
window.mainloop()