import os
import time
import datetime
from pros.serial.devices.vex.v5_user_device import V5UserDevice
from pros.serial.ports import DirectPort
from pros.serial.terminal import Terminal
# from serial import SerialException
import threading

def open_terminal():
    t = threading.currentThread()
    # while(getattr(t, 'do_run', True)):
    os.system('pros terminal COM5')



time.sleep(1.0)
# Tweak Ports to reflect the port your V5 Device is plugged into
ports = ['COM5'] #'COM6']
port = None
for p in ports:
    try:
        port = DirectPort(p)
    except:# SerialException as err:
        print('Port not on {}.'.format(p))
        continue


vfive = V5UserDevice(port)
term = Terminal(vfive, request_banner=False)
time.sleep(1)
term.start()
i = 0
while  True:
    time.sleep(1.0)
    term.write_to_screen(str(datetime.datetime.now())+'\n')
