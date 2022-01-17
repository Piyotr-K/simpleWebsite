def e1(name):
    # Given a string name, eg. "Bob", return a greeting of the form "Hello Bob!"
    # return the final string
    return f"Hello {name}!"

def e2(tag, word):
    # Create an html tag thing
    # Given a tag and a word return in the format <tag>word</tag>
    # eg. e2("h4", "Massive") -> <h4>Massive</h4>
    return f"<{tag}>{word}</{tag}>"

def e3(word):
    # Given a word
    # Return the first half of the word
    # Round down 9 / 2 -> 4
    # eg. HugeMeme -> Huge
    # eg. HugeLarge -> Huge
    return word[0:len(word)//2]

def e4(word):
    return word[0:2]

def e5(word):
    # Given a word, rotate the first 2 letters to the end
    # Last 2 letters to the front
    # return final string
    # eg. Elephantine -> neephantiEl
    # eg. Bigfunny -> nygfunBi
    tmp = word[0:2]
    tmp2 = word[-2:] # Get last 2 characters
    tmp3 = word[2:-2]
    return f"{word[-2:]}{word[2:-2]}{word[0:2]}"

def e6(s):
    # Given a string of 2 numbers
    # Get the sum
    # 3 35 -> 38
    # 6 45 -> 51
    tmp = s.split(" ")
    sum = 0
    for x in range(len(tmp)):
        sum += int(tmp[x])
    return sum

def e7():
    # Eg of telemarketer numbers:
    # 8229, 8338, 9008
    # print ignore or answer depending on if it is a telemarketer
    digit = input()
    digit2 = input()
    digit3 = input()
    digit4 = input()
e7()