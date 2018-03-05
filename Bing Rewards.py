import webbrowser
import time, os
from random import choice,randint

finished = "BingFinishedPopup.exe"
word_file = "words.txt"
WORDS = open(word_file).read().splitlines()
finalSearch = []
definitions = 0
browser = input("""What browser do you use?
                [1] Chrome
                [2] Explorer""")
if browser == '1' or browser.lower() == 'chrome':
    killChrome = "killChrome.cmd"
elif browser == '2' or browser.lower() == 'explorer':
    killChrome = "killExplore.cmd"

postRewardCommand = input("""After the program finishd would you like to:
                            [1] Shutdown
                            [2] Restart
                            [3] Hibernate
                            [4] Do Nothing""")
if postRewardCommand == "1":
    command = "shutdown.lnk"
if postRewardCommand == "2":
    command = "restart.lnk"
if postRewardCommand == "3":
    command = "hibernate.lnk"
else:
    command = "nothing"


def append(num,initialNum,word):
    global finalSearch
    global definitions
    plus = "+"
    if initialNum == 1:
        finalSearch.append(word)
        finalSearch.append(plus)
        finalSearch.append("definition")
        definitions += 1
    else:
        if num != 1:
            finalSearch.append(word)
            finalSearch.append(plus)
        if num == 1:
            finalSearch.append(word)

def browser():
    global WORDS
    global listOfWords
    global finalSearch
    beginning = "http://www.bing.com/search?q="
    end = "&src=ie9tr&adlt=strict"
    plus = "+"
    finalSearch.append(beginning)
    x = randint(1,5)
    initial = x
    for i in range(x):
        SEARCH = choice(WORDS)
        append(x,initial,SEARCH)
        x -= 1
    finalSearch.append(end)
    SEARCH = ''.join(finalSearch)
    webbrowser.open_new_tab(SEARCH)
    finalSearch.remove(beginning)
    finalSearch.remove(end)
    print(finalSearch)
    finalSearch = []
count = 0
for i in range(3):
    for i in range(30):
        count+=1
        print(count)
        print()
        browser()
        print()
        if count % 6 == 0:
            time.sleep(2)
            os.startfile(killChrome)
        time.sleep(2)

os.startfile(finished)
os.startfile(command)
