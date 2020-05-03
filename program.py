import ctypes
import time
from random import randrange
import os
import sys
import urllib.request
import threading
from threading import Timer
from time import sleep




issa=input("Enter password: ")
password = urllib.request.urlopen("https://pastebin.com/raw/mqqb0ipZ").read()
global dis
global incorrect
global secret
global currentPassword

secret = "ile"
incorrect = 0
dis = False

def checkpass():
    #thread = RepeatedTimer(2, checkpass)
    try:
        newpas = urllib.request.urlopen("https://pastebin.com/raw/mqqb0ipZ").read()
        if str(currentPassword) != str(newpas.decode('utf-8')):
            #thread.stop()
            sortprint(f"Password has been changed [{currentPassword}], exiting...\n")
            time.sleep(2)
            exit()
    except:
        sortprint("An error occured, try restarting the program\n")
        #thread.stop()
        exit()

            
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()


    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


# game function
def game():
    #h4x("Guess a number from 1 - 10: ","True")
    checkpass()
    global incorrect
    In = input("Guess a number from 1 - 10: ")
    In = str(In)
    ran = randrange(1,11)
    ran = str(ran)


    # Vibe check start
    if str(In.lower()) == "quit" or str(In.lower()) == "gtfo":
        exit()
    if str(In.lower()) == "fuck":
        global dis
        dis = True
        sortprint("Successfully changed outputting method\n")
    if In == secret:
        sortprint(f"legacy detected; hi there boi, the answer is {ran} k \n")
        In = input("Guess a number from 1 - 10: ")


    # game funcs
    if In == ran:
        sortprint(f"YOU WON! After {str(incorrect)} tries!\n")
        dod = input("Do you want to play again? [Y/n]")
        if dod.lower()=="y":
            incorrect = 0
            game()
        else:
            sortprint("Congrats and see you soon!\n")
            time.sleep(0.04)
            exit()
    

    else:
        incorrect = incorrect + 1
        sortprint(f"{str(In)} is the wrong asnwer, try again or type quit to quit the game.\n")
        game()


def sortprint(string):
    if dis == True:
        print(string)
    if dis == False:
        h4x(string,"True")

# clear output for h4x
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# h4x function
def h4x(string,inline):
        letter = 1
        while letter <= len(string):
            new_string = string[0:letter]
            if inline: sys.stdout.write("\r")
            sys.stdout.write("{0}".format(new_string))
            if inline == False: sys.stdout.write("\n")
            if inline: sys.stdout.flush()
            letter += 1 
            if string[-1+-2]=='e': time.sleep(float(0.04)) 
            else: time.sleep(float(0.06)) 


if issa == str(password.decode('utf-8')):
    sortprint("Welcome to Mansour's first secure game in Pyhton! :) If you don't like this way of outputting type fuck\n")
    global currentPassword
    currentPassword = str(password.decode('utf-8'))
    game()
else:
        # ctypes.windll.user32.MessageBoxW(0,"Enter a correct password","Wrong Password",1)
        sortprint("Wrong password :(")
        exit()
