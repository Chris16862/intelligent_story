import glob
import os
import cv2
import configure as cfg


def getFrame(vdo_pth, count, sec):
    vidcap = cv2.VideoCapture(vdo_pth)
    #frameRate = vidcap.get(5)
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = vidcap.read()
    if hasFrames:
        # save frame as JPG file
        path = os.path.join(cfg.STORE_IMG_PATH, f"{vdo_pth[-6:-4]}\image_{count}.jpg")
        # print (path)
        cv2.imwrite(path, image)
    print(hasFrames)
    return hasFrames


vdo = glob.glob(cfg.DATA_SET_PATH+'/*.mp4')

for v in vdo:
    # vdo number
    # print(v[-6:-4])
    os.makedirs(f'{cfg.STORE_IMG_PATH}/{v[-6:-4]}') if not os.path.exists(
        f'{cfg.STORE_IMG_PATH}/{v[-6:-4]}') else 0
    sec = 0
    frameRate = 1  # //it will capture image in each 0.5 second
    count = 1
    success = getFrame(v,count,sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(v,count,sec)
