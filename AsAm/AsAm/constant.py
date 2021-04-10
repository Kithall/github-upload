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

ENABLE_GPIO = 21   # GPIO channel for output driver enable pin

TL_CNT = 4 # Count of traffic lights classic (red,yellow,green)
TL_OUCH_CNT = 3 # Count of output channels per TL

TS_CNT = 0 # Count of traffic sensors ("Induktionsschleifen")
TS_INCH_CNT = 1 # Count of input channels per TS

PL_CNT = 0 # Count of pedestrian lights (red, green)
PL_OUCH_CNT = 1 # Count of input channels per PL

PS_CNT = 0 # Count of pedestrian switches
PS_INCH_CNT = 1 # Count of input channels per PS


LED_CHANNEL_CNT = TL_CNT * TL_OUCH_CNT + PL_CNT * PL_OUCH_CNT  # Number of output driver channels

