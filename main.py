#!/usr/bin/python3
import datetime
import resource
import time
import os
logtimer = os.getenv("LOG_TIMER")

os.system("nohup python3 -m http.server 80 --bind :: > output.log &")
while True:
  time.sleep(15)
  print("hey now")
