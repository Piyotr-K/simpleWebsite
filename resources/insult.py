import random
from guizero import App, Text, PushButton

def insult_me():
    # Adjectives
    list_a = []
    list_b = []

    # Nouns
    list_c = []

    with open("insults/insults.csv", 'r') as f:
        contents = f.readlines()

        # Go through the contents line by line, row by row
        for line in contents:
            # Split the line into a list of 3 items
            words = line.split(",")
            list_a.append(words[0])
            list_b.append(words[1])
            list_c.append(words[2].strip())

    word1 = random.choice(list_a)
    word2 = random.choice(list_b)
    word3 = random.choice(list_c)

    # Concatenation
    #print("You are a " + word1 + " " + word2 + " " + word3 + "!")

    # Format
    #print("You are a {} {} {}!".format(word1, word2, word3))

    # Format short hand
    #print(f"You are a {word1} {word2} {word3}!")
    return (f"You are a {word1} {word2} {word3}!")

def new_insult():
    new_insult = insult_me()
    message.value = new_insult

# Create the app
app = App("Shakespearean insult generator")
message = Text(app, insult_me())
btn = PushButton(app, new_insult, text="Insult me again :(")
app.display()