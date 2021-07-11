import random
import re

def loadWords():
    return open('english-nouns.txt','r').readlines()

def hideWord(word):
    for chr in word:
        word = word.replace(chr, '*')
    return word

def replaceHiddenChar(myguess, hidden_word, myword):
    indexes = [x.start() for x in re.finditer(myguess,myword)]
    for ind in indexes:
        hidden_word = hidden_word[:ind]+myguess+hidden_word[ind+1:]
    return hidden_word

def isInputValid(guess):
    return len(guess)<=1

def isCharValid(guess,word):
    return guess in word

def printStatus(fails,accerts,hidden_word):
    print(f'=============\nWord: {hidden_word}\nAccerts: {accerts}\nFails: {fails}')

def main():
    lines = loadWords()
    secret_word = random.choice(lines).strip()
    hidden_word = hideWord(secret_word)
    letters = len(secret_word)
    print('============\nThe selected word has '+str(letters)+' letters\n'+hideWord(secret_word))
    fails, accerts = 0, 0
    while(hidden_word!=secret_word):
        myguess = input('Insert your guess: ')
        if(isInputValid(myguess) and isCharValid(myguess,secret_word)):
            hidden_word = replaceHiddenChar(myguess,hidden_word,secret_word)
            accerts+=1
        else:
            print('Too bad.. try again')
            fails+=1
        printStatus(fails,accerts,hidden_word)

if __name__ == "__main__":
    main()



