# Onvisson
Online video streaming &amp; social networking website
*A product development project for software engineering assignment assignment*


**Installing Onvisson on Ubuntu**

1. Clone project and run command on terminal
   - cd django_project
   - cd youtube_search
   
2. On the terminal install django
   - pipenv install django

3. Start the shell and runserver
   - pipenv shell
   - python manage.py runserver


**Installation for ML Model**

1. Dependencies used :
   - pip install numpy
   - pip install pandas
   - pip install tensorflow
   - pip install keras
   - pip install opencv-python

2. Emotion_recognition.py : This is the main program. The pseudo code here shows how the model has been implemented.

  **Importing libraries:** 

   - Importing sys, os
   - Importing pandas as pd
   - Importing numpy as np
   - from keras.models Importing Sequential
   - from keras.layers Importing Dense, Dropout, Activation, Flatten
   - from keras.layers Importing Conv2D, MaxPooling2D, BatchNormalization,AveragePooling2D
   - from keras.losses Importing categorical_crossentropy
   - from keras.optimizers Importing Adam
   - from keras.regularizers Importing l2
   - from keras.utils Importing np_utils
