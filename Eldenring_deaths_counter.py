import cv2 
import numpy as np
import os
from PIL import ImageGrab

encounter_image = cv2.imread('death.jpg')
w,h,c = encounter_image.shape[:3]

state = False

while True:
    img = ImageGrab.grab(all_screens=True)
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = cv2.matchTemplate(frame, encounter_image, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= 0.5)
    locations = list(zip(*locations[::-1]))
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), w, h]
        rectangles.append(rect)
        rectangles.append(rect)
    rectangles, weights = cv2.groupRectangles(rectangles, groupThreshold=1, eps=0.5)
    if len(rectangles) != 0 and state == False:
        state= True
        with open('eldenring_deaths.txt', 'r') as f:
            count = int(f.read())
            with open('eldenring_deaths.txt', 'w') as out:
                count += 1
                out.write(str(count))
                
    elif len(rectangles) == 0 and state == True:
        state = False
    

    if cv2.waitKey(10) == ord('q'):
        cv2.destroyAllWindows()
        break