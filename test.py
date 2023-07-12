import cv2 as cv
import numpy as np
from mss import mss
import time

with mss() as sct:

    while(True):
        print(dir(sct))
        screenshot = np.array(sct.grab(sct.monitors[0]))

        cv.imshow('Computer Vision', screenshot)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break


print('Done.')
