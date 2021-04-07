############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    COVID-19 AI Classification
# Project:       COVID-19 Pneumonia Detection/Early Detection
#
# Author:        Nitin Mane
# Title:         Predict CT Scan on Web Page
# Description:   Analyze the CT Scan images and predict whether they are COVID-19 or normal Scans by using Pretrained Model on a Web Page
# License:       MIT License
# Last Modified: 2021-02-10
#
############################################################################################

from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import pandas as pd

#from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from tensorflow.keras.preprocessing import image

#import libraries
from tensorflow import keras
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import Model

# src 
from src.xDNN_class import *
from src.xDNN_class import xDNN
from numpy import genfromtxt
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt


# coding=utf-8
import sys, os, glob, re, matlab.engine
import logging, json


#######################################################################################################################
app = Flask(__name__)
app.secret_key = ('7LQl_lAfBQMjT4rkNMrV3g')

#creating logger file
logger = logging.getLogger('Server.py')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('./Logs/allLogs.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#Loads the program configuration
with open('config.json') as confs:
    confs = json.loads(confs.read())


categories = ["COVID-19", "Normal"]

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    # Preprocessing the image
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x, mode='caffe')
    preds = model.predict(x)
    return (preds)

def ext_feature(img_path):
    #del x 
    #del test
    #del features
    from tensorflow.keras.preprocessing import image 
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    model = VGG16(weights='imagenet', include_top= True )
    layer_name = 'fc2'
    intermediate_layer_model = keras.Model(inputs=model.input,outputs=model.get_layer(layer_name).output)
    features = intermediate_layer_model.predict(x)
    image = []
    image.append(features[0])
    img_feature = np.array(image)
    
    
    return(img_feature)
    
def classify_image(out_fe):
    
    # Load the files, including features, images and labels.    

    X_train_file_path = r'./features/data_df_X_train_lite.csv'
    y_train_file_path = r'./features/data_df_y_train_lite.csv'

    X_train = genfromtxt(X_train_file_path, delimiter=',')
    y_train = pd.read_csv(y_train_file_path, delimiter=';',header=None)

    pd_y_train_labels = y_train[1]
    pd_y_train_images = y_train[0]

    # Convert Pandas to Numpy
    y_train_labels = pd_y_train_labels.to_numpy()
    y_train_images = pd_y_train_images.to_numpy()

    # Model Learning
    Input1 = {}

    Input1['Images'] = y_train_images
    Input1['Features'] = X_train
    Input1['Labels'] = y_train_labels
    
    Mode1 = 'Learning'

    Output1 = xDNN(Input1,Mode1)
    
    Input3 = {}
    Input3['xDNNParms'] = Output1['xDNNParms']
    Input3['Features'] = out_fe
    Mode3 = 'classify'

    Output3 = xDNN(Input3,Mode3)
    
    return(Output3)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return ('.') in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    # Main page
    return (render_template('index.html'))

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # filename = secure_filename(file.filename)
            UPLOAD_FOLDER = ('static/uploads/')
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'test.png'))
        #img = ('./static/uploads/test.png')
        #img = image.load_img(img, target_size=(224, 224))
    img_feature = ext_feature('./static/uploads/test.png')
    logger.info("Image file {} successfully saved in {} folder".format(f, dir_name))
    prediction = classify_image(img_feature)
        
    out1 = prediction['Scores'][0][0]
    out2 = prediction['Scores'][0][1]
    
    # Responds to standard HTTP request.

	message = ""
	classification = self.model.http_classify(request)

	if out1 > out2:
        message = ("COVID-19 detected!")
		diagnosis = ("Positive")
        result = ('COVID19 Detected')
        print('COVID19 Detected  Prediction:', str(out1))
	else:
		message = ("COVID-19 not detected!")
		diagnosis = ("Negative")

	resp = jsonpickle.encode({
		Response': 'OK',
		'Message': message,
		'Diagnosis': diagnosis

        
    #return render_template('base.html', filename=filename)
    return (result)
    

if __name__ == '__main__':
      app.run(debug=True)
      