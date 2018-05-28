import cv2
import os
import re
import numpy as np
from tkinter.filedialog import askdirectory

pattern = re.compile(r'\S*\.(mp4|MP4|avi)')
skipFrameNum = 1
frameCnt = 0
segXNum = 1
segYNum = 1

def getVideoName(path, nameList):
    fileList = os.listdir(path)
    for file in fileList:
        filePath = os.path.join(path, file)
        if os.path.isdir(filePath):          #is a dir
            continue
            #getVideoName(filePath, nameList)  #rescursive search
        elif re.match(pattern, file) != None:          #is a video in mp4 format
            nameList.append(filePath)
    return nameList

def videoToFrame(videoName, out_folder):
    print(videoName)
    cap = cv2.VideoCapture(videoName)
    flag, frame = cap.read()
    global frameCnt
    skipCnt = 0
    width, height = np.shape(frame)[1], np.shape(frame)[0]

    while flag:
        for i in range(segXNum):
            for j in range(segYNum):
                frame2 = frame[j * height // segYNum : (j + 1) * height // segYNum,
                               i * width // segXNum : (i + 1) * width // segXNum] #get ROI
                cv2.imencode('.jpg', frame2)[1].tofile(out_folder + "/" + '{:0>6}'.format(str(frameCnt + 1)) + '.jpg')
                frameCnt += 1
        skipCnt += 1
        cap.set(1, skipCnt * skipFrameNum)
        flag, frame = cap.read()
    return

if __name__ == "__main__":
    in_folder = askdirectory(title="Select folder with video files")
    videoNameList = getVideoName(in_folder,[])
    out_folder = askdirectory(title="Select output folder")
    print("video Num: %d" %len(videoNameList))
    for video in videoNameList:
        videoToFrame(video)

