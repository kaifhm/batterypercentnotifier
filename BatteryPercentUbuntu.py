#!/usr/bin/env python3
import os
from time import sleep


while True:
    status = open('/sys/class/power_supply/BAT1/status','r').readline().strip()
    charging = 0 if status == 'Discharging' else 1
    with open('/sys/class/power_supply/BAT1/capacity','r') as file:
        battery_percent = int(file.readline().strip())

    if battery_percent > 89 and charging:
        message = f"'Battery charged to {battery_percent}%'"
        os.system(f"notify-send 'Battery sufficiently charged' {message}")
        sleep(120)
    elif battery_percent < 21 and not charging:
        message = f"'Battery is at {battery_percent}%. Please plug-in your AC adapter'"
        os.system(f"notify-send 'Battery Low' {message}")
        sleep(120)
    else:
        sleep(1)
