#to start enumerate over, sudo rm /home/pi/Documents/pic_temp.txt
#** this will start overwriting any pics that exist in Desktop/Pictures dir.

from picamera import PiCamera
from time import sleep
import os
from subprocess import call
import sys
import datetime

current_dir = os.path.dirname(os.path.realpath(__file__))
filename = "/home/pi/Documents/pic_temp.txt"
loopnum = 0
camera = PiCamera()
camera.rotation = 180

def setup2():
    with open(filename,"w") as writefile:
        writefile.write("0")
        writefile.close()
    setup()

def setup():
    if os.path.exists(filename) != 1:
        setup2()
    else:
        global picnum
        picnum = int(open(filename,"r").readlines()[0])    
        global repeat
        global wait
        repeat = int(open(current_dir + "/config.txt","r").readlines()[0])
        wait = int(open(current_dir + "/config.txt","r").readlines()[1])

def loop(loopnum,picnum):
    uppath = current_dir + "/dropbox_uploader.sh upload "
    while True:
        if loopnum == repeat:
            destroy()
        else:
            date_time = datetime.datetime.strftime(datetime.datetime.now(),"%d-%m-%Y %H:%M:%S")
            loopnum += 1
            picnum += 1
            camera.annotate_text=str(loopnum) + "/" + str(repeat) + " @ " + date_time
            sleep(wait)
            picfile = '/home/pi/Desktop/Pictures/image%s.jpg' % picnum
            camera.capture(picfile)
            with open(filename,"w") as writefile:
                writefile.write(str(picnum))
                writefile.close()
            try:
                call([uppath + picfile + " image" + str(picnum) + ".jpg"],shell=True)
            except:
                print "upload failed"
                destroy()

def destroy():
    sys.exit()

if __name__ == '__main__':
    setup()
    try:
        loop(loopnum,picnum)
    except KeyboardInterrupt:
        destroy()
