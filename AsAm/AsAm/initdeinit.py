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

import sys, signal
import RPi.GPIO as GPIO  # Pincontrol
import constant, structures # AsAm Constants and structures

def init ():
	print ("Init")
	signal.signal(signal.SIGINT, signal_handler) # Give Signalhandler callback for SIGINT
	GPIO.setmode(GPIO.BCM) # Set all BPIO to BCM
	AsAm_init()
	print ("Enable output drivers")
	GPIO.setup(constant.ENABLE_GPIO, GPIO.OUT)
	GPIO.output(constant.ENABLE_GPIO, GPIO.HIGH) 
	
def AsAm_init():
	# Configure and initialize ample structure
	print ("Init Ampel")
	for i in range(constant.TL_CNT):
		structures.tl.append(structures.tl_struct)
	# Init in / output channels
	print ("Init in / output")


def deinit ():
	print ("DeInit")
	print ("Disable output drivers")
	GPIO.output(constant.ENABLE_GPIO, GPIO.LOW) 
	
	
	sys.exit(0)
	

def signal_handler(signal, frame):
       print("\nprogram exiting gracefully")
       deinit()
