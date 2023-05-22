import os
import sys
import time

TIME_LIMIT = 6*3600 # server runtime limit in s

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = int(float(f.readline().split()[0]))

    return uptime_seconds

def poweroff():    
    print('poweroff-timer: os.system("poweroff")', file=sys.stderr)
    os.system("poweroff")

while True:
    uptime = get_uptime()
    if uptime >= TIME_LIMIT:
        print('poweroff-timer: time limit of ' + str(TIME_LIMIT/60) + 'min exceeded, executing poweroff now', file=sys.stderr)
        poweroff()
    else:
        print('poweroff-timer systemd service: poweroff in ' + str(TIME_LIMIT - uptime) + 's', file=sys.stderr)
    time.sleep(300)

