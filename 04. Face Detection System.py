#!/usr/bin/env python
# coding: utf-8

# # Part 3
# ## 1.Study about haarcascade algorithm.
# ## 2.Try to import haarcascade algorithm for face detection in ide (.xml).
# ## 3.Prepare a model which will detect the face and boundary it using green color box.

# In[1]:


import cv2


# In[2]:


face_cap = cv2.CascadeClassifier("C:/Users/sampa/anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)

while True:
    ret, video_data = video_cap.read()
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(col, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Video_Live", video_data)
    if cv2.waitKey(10) == ord("a"):
        break

video_cap.release()


