from time import strftime

import numpy as np


import imagehash
from PIL import Image
import cv2
import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
# from matplotlib.path import Path
from datetime import datetime
from sample_data import student
import smtplib
net = cv2.dnn.readNet('nm.onnx')
# net = cv2.dnn.readNet('C:/Users/sufya/Desktop/smoking detetction/NEW/mlk.onnx')
            # step 2 - feed a 640x640 image to get predictions
def format_yolov5(frame):

            row, col, _ = frame.shape
            _max = max(col, row)
            result = np.zeros((_max, _max, 3), np.uint8)
            result[0:row, 0:col] = frame
            return result


def image_matching(a,b):
    i1 = Image.open(a)
    i2 = Image.open(b)
    assert i1.mode == i2.mode, "Different kinds of images."
    assert i1.size == i2.size, "Different sizes."

    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
    # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

    ncomponents = i1.size[0] * i1.size[1] * 3
    xx= (dif / 255.0 * 100) / ncomponents
    return xx


def match_templates(in_image):
    name=[]
    values=[]
    entries = os.listdir('train/')
    folder_lenght= len(entries)
    i=0
    for x in entries:
        val=100
        directory=x
        name.append(x)
        x1="train/"+x

        arr = os.listdir(x1)
        for x2 in arr:
             path=x1+"/"+str(x2)
             find=image_matching(path,in_image)
             hash0 = imagehash.average_hash(Image.open(path))
             hash1 = imagehash.average_hash(Image.open(in_image))
             cc1=hash0 - hash1
             # print(cc1)
             find=cc1
             if(find<val):
                 val=find
        values.append(val)
    values_lenght= len(values)
    pos=0;
    pos_val=100
    for x in range(0, values_lenght):
        if values[x]<pos_val:
            pos=x
            pos_val=values[x]

    if(pos_val<17):
        # print(pos,pos_val,name[pos])
        return name[pos]
    else:
        return "unknown"












cascPath = "data/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
train=True
# video_capture = cv2.VideoCapture('http://192.168.1.12:8080/video')
video_capture = cv2.VideoCapture(0)
# video_capture = cv2.VideoCapture(0)
name="testing"
if os.path.exists(name):
    h=0;
else:
    os.mkdir(name)
e_mail=0
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
######
    if (frame is None):
            print("Can't open image file")
    face_cascade = cv2.CascadeClassifier(cascPath)
    faces = face_cascade.detectMultiScale(frame, 1.1, 3, minSize=(100, 100))
    if (faces is None):
            print('Failed to detect face')

    if (True):
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
    facecnt = len(faces)
    if facecnt<1:
        # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv2.rectangle(frame, (100, 100), (500, 500), (0, 255, 0), -1)

        img=frame
        height, width = frame.shape[:2]
        cv2.rectangle(frame, (0, 0), (width, height), (0, 0, 0), 3)


    else:
        input_image = format_yolov5(frame)  # making the image square
        blob = cv2.dnn.blobFromImage(input_image, 1 / 255.0, (640, 640), swapRB=True)
        net.setInput(blob)
        predictions = net.forward()

        # step 3 - unwrap the predictions to get the object detections

        class_ids = []
        confidences = []
        boxes = []

        output_data = predictions[0]

        image_width, image_height, _ = input_image.shape
        x_factor = image_width / 640
        y_factor = image_height / 640

        for r in range(25200):
            row = output_data[r]
            confidence = row[4]
            if confidence >= 0.18:

                classes_scores = row[5:]
                _, _, _, max_indx = cv2.minMaxLoc(classes_scores)
                class_id = max_indx[1]
                if (classes_scores[class_id] > .18):
                    confidences.append(confidence)

                    class_ids.append(class_id)

                    x, y, w, h = row[0].item(), row[1].item(), row[2].item(), row[3].item()
                    left = int((x - 0.5 * w) * x_factor)
                    top = int((y - 0.5 * h) * y_factor)
                    width = int(w * x_factor)
                    height = int(h * y_factor)
                    box = np.array([left, top, width, height])
                    boxes.append(box)

        class_list = ['smoking']

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.18, 0.18)

        result_class_ids = []
        result_confidences = []
        result_boxes = []

        for i in indexes:
            result_confidences.append(confidences[i])
            result_class_ids.append(class_ids[i])
            result_boxes.append(boxes[i])

        for i in range(len(result_class_ids)):
            box = result_boxes[i]
            class_id = result_class_ids[i]
            # confi= str(result_confidences[i]+0.4)
            confi = str(100 * result_confidences[i].round(2) + 40) + "%"


            cv2.rectangle(frame, box, (0, 255, 255), 2)
            cv2.rectangle(frame, (box[0], box[1] - 20), (box[0] + box[2], box[1]), (0, 255, 255), -1)
            cv2.putText(frame, class_list[class_id] + " " + confi, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, .5,
                        (0, 0, 0))
            ddd=int(100 * result_confidences[i].round(2) + 40)
            if int(ddd)>=70:
                for (x, y, w, h) in faces:
                    r = max(w, h) / 2
                    centerx = x + w / 2
                    centery = y + h / 2
                    nx = int(centerx - r)
                    ny = int(centery - r)
                    nr = int(r * 2)

                    faceimg = frame[ny:ny + nr, nx:nx + nr]
                    font = cv2.FONT_HERSHEY_SIMPLEX

                    str1 = name + '\\tt.jpg'
                    # kk=kk+1

                    lastimg = cv2.resize(faceimg, (100, 100))

                    cv2.imwrite(str1, lastimg)
                    ar = match_templates(str1)
                    print(ar)
                    if ar == "unknown":
                        e_mail = e_mail + 1
                    else:
                        e_mail = 0
                    if e_mail >= 25:
                        msg = MIMEMultipart()
                    cv2.putText(faceimg, (ar), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
                    now = datetime.now()
                    dt_string = now.strftime("%Y_%m_%d")
                    name = "fine"
                    if os.path.exists(name):
                        h = 0
                    else:
                        os.mkdir(name)
                    file = os.path.join(name + "/" + dt_string + '.txt')
                    print(file)
                    with open((file), 'w') as f:
                        f.writelines(ar)
                    f.close()
            # now = datetime.now()
            # dt_string = now.strftime("%Y_%m_%d")
            # name = "fine"
            # if os.path.exists(name):
            #     h = 0
            # else:
            #     os.mkdir(name)
            # file = os.path.join(name + "/" + dt_string + '.txt')
            # print(file)
            # with open((file), 'w') as f:
            #     f.writelines(ar)
            # f.close()

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

