#!/usr/bin/env python
import time
import platform
from os import system
from subprocess import call

class Birthday(object):
    """
    A class to make your computer 'sing' you happy birthday
    """
    def __init__(self):
        self.os = platform.system()
        self.name = ''
        
    def espeak_checker(self):
        # Check to see if espeak is installed
        cmd = "where" if self.os == "Windows" else "which"
        # 1 if not installed 0 if installed
        rseponse = call([cmd, 'espeak'])
        # Install instructions for Linux and return False
        if rseponse == 1 and self.os == "Linux":
            print("Looks like you don't have espeak installed. You can \
            install it with sudo apt-get install espeak")
            return False
        # Install instructions for Windows and return False
        elif rseponse == 1 and self.os == "Windows":
            print("Looks like you don't have espeak installed. You can download it from http://sourceforge.net/projects/espeak/files/espeak/espeak-1.48/setup_espeakedit-1.48.03.exe but be sure to add it to your path when you're finished intalling it!")
            return False
        # Return True
        elif response == 0:
            return True
    
    def input_string(self):
        # Make sure it gets your name regardless of python version
        try: 
            input = raw_input
        except NameError: 
            pass
        self.name = input("I hear it's your bday. What's your name?")
        print("Could you turn up your volume, please?")
        
    def hbd_string(self):
        # Create the text to be sung.
        text = ''
        for i in range(0,4):
            text += 'Happy birthday '
            if i == 2:
                text += 'dear {} '.format(self.name)
            elif i == 3:
                text += 'to you!'
            else:
                text += 'to you '
        return text
        
    def hbd_mac(self):
        # Sing for Macs
        system('say -v Pipe {}'.format(self.hbd_string()))
        
    def hbd_linux_windows(self):
        # Sings for Linux and Windows
        system('espeak {}'.format(self.hbd_string()))
        
    def run_it(self):
        if self.espeak_checker():
            self.input_string()
            time.sleep(2)
            if self.os == 'Windows' or self.os == 'Linux':
                self.hbd_linux_windows()
            elif self.os == 'Darwin':
                self.hbd_mac()
            else:
                print("Hey, looks like you're not on Windows, Linux, or \
a Mac. So I guess I'll just say Happy Birthday, {}!".format(self.name))
        
    
if __name__ == '__main__':
    BDay = Birthday()
    try:
        BDay.run_it()
    except:
        print("That's weird, something isn't working. I thought I accounted for everything. Oh well, Happy Birthday, {}!".format(BDay.name))
