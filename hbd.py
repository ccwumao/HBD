#!/usr/bin/env python
import platform

def HBD(name):
    for i in range(0,4):
        print("Happy Birthday", ((i == 2 and 
            ("Dear {}".format(name),)) or ("to you",))[0])
        
if __name__ == __main__:
    platform.system()
    HBD('Jake')
