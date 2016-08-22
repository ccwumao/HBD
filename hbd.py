#!/usr/bin/env python
import platform
from os import system

class Birthday(object):
    """
    A class to make your computer 'sing' you happy birthday
    """
    def __init__(self):
        self.os = platform.system()
        self.name = ''
    
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
        self.input_string()
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
        print("I think you're missing espeak. If you're on Linux, try \
sudo apt-get install espeak. For Windows it's at this address: \
http://sourceforge.net/projects/espeak/files/espeak/espeak-1.48/setup_espeakedit-1.48.03.exe")
        print("Anyway, Happy Birthday, {}!".format(BDay.name))
