import pyautogui as pyt
import cv2 as cv
import numpy as np
import datetime
import random
import string

#Getting the size of Screen as Screenresolution
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def ScreenSize():
    img = pyt.screenshot()
    img = np.array(img)
    height, width, layers = img.shape
    size = (width,height)
    return size

def Screen_Recorder(out_video, start_rec):
    if start_rec == "start":
        while True:
            img = pyt.screenshot()
            frame = np.array(img)
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            out_video.write(frame)
            cv.imshow("Recording in progress ...", frame)
            if cv.waitKey(1)==ord("q"):
                break
        cv.destroyAllWindows()
        return out_video.release()
    else:
        exit(0)

if __name__=="__main__":
    fourcc = cv.VideoWriter_fourcc(*"XVID")
    start_rec = str(input())
    path = "../media/Recording"+str(id_generator())+".mp4"
    print(path)
    out_video = cv.VideoWriter(path, fourcc, 24.0, ScreenSize())
    Screen_Recorder(out_video, start_rec)