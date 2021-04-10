#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2021  <pi@zpi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys
import signal # e.g. for SIGINT to stop execution    
import RPi.GPIO as GPIO  # Pincontrol
import time # Timecontrol

import initdeinit as idi
import constant # AsAm Constants

def main(args):
    return 0

if __name__ == '__main__':

    idi.init()  
           
    
    d = 0.2

    for i in range(9,22):
        GPIO.setup(i, GPIO.OUT)
    
    

    while True:
        for i in range(9,21):        
            GPIO.output(i, GPIO.HIGH)
            time.sleep(d)
            GPIO.output(i, GPIO.LOW)                
    
    # sys.exit(main(sys.argv))
    # Errorcase In normal run, this will not be reached 
    sys.exit(1)
