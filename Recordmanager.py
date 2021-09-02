# Recordmaneger bot
# Developed by Abbas Mohamadi
# Sep 9th 2021
# All copy rights have been reserved

# import require libraries
import pyautogui as pg
import time
import os


def record():
    # your record button
    pg.press('f12')


def stop():
    # your stop record button
    pg.press('f12')


def manager():
    try:

        # type your directory here for example : 'c:\\recordfolder'
        folder_dir = 'G:\\recordtest\\'
        files = os.listdir(folder_dir)

        # for f in files:
        #    print(f)
        # print(files[2])

        # check if the files in the directory is more or equal than 4
        # if there are more or equal than 4 then remove the older files
        # if there are less than 4 items then just pass
        if len(files) >= 4:
            deletepath = folder_dir + str(files[0])
            os.remove(deletepath)
            print('file: ' + str(files[0]) + ' is deleted from directory' + deletepath)
        else:
            print('there is less than 4 files available in the directory')
            pass
    except:

        # just make sure to protect code from crashing
        print('Something went wrong please double check everything and try again ! :) ')


def wait(x):
    time.sleep(x)


while True:
    record()
    # wait for about 300 sec = 5 min then stop the recording
    # here you can change the time manually
    wait(300)
    stop()
    wait(5)
    manager()
    wait(5)
