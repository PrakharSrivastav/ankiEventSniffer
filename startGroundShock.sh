#!/bin/bash

#device=`ls -1 /dev/ttyU* | head -4 | tail -1`
device='/dev/ttyUSB0'
#Ground Shock
./venv/bin/python ./sniffer.py -v --carToFollow=Ground\ Shock $device
