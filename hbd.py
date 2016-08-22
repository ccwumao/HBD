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
        self.name = input('I hear it's your bday. What's your name?')
        
    def hbd_string(self):
        text = ''
        for i in range(0,4):
            text += 'Happy birthday'
            if i == 2:
                text += 'dear {}'.format(self.name)
            else:
                text += 'to you!'
        return text
        
    def hbd_mac(self):
        system('say -v Pipe {}'.format(self.hbd_string()))
        
    def hbd_linux_windows(self):
        system('espeak {}'.format(self.hbd_string()))
        
    def run_it(self):
        if self.os == 'Windows' or self.os == 'Linux':
            self.hbd_linux_windows()
        if self.os == 'Darwin':
            self.hbd_mac()
        else:
            print('Hey, looks like you're not on Windows, Linux, or \
            a Mac. So I guess I'll just say Happy Birthday, {}!'.format(self.name))
        
    
if __name__ == __main__:
    BDay = Birthday()
    try:
        Bday.run_it()
    except:
        print('I think you're missing espeak. If you're on Linux, try \
        "sudo apt-get install espeak". For Windows it's at this address: \
        http://sourceforge.net/projects/espeak/files/espeak/espeak-1.48/setup_espeakedit-1.48.03.exe')
