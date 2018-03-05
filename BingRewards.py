import webbrowser
import time, os
from random import choice,randint

finished = "BingFinishedPopup.exe"
word_file = "words.txt"
WORDS = open(word_file).read().splitlines()
finalSearch = []
definitions = 0
killChrome = 'killChrome.cmd'

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

