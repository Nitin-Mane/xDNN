# Peter Moss COVID-19 AI Research Project

## COVID-19 xDNN

### COVID-19 xDNN Python Classifier

[![xDNN](../../../Media/Images/covid-19-ai-research-xdnn.png)]()

&nbsp;

# Table Of Contents

- [Introduction](#introduction)
- [DISCLAIMER](#disclaimer)
- [Installation](#installation)
- [Train](#train)
  - [Start Training](#start-training)
  - [Training Results](#training-results)
  - [Metrics Overview](#metrics-overview)
  - [Figures Of Merit](#figures-of-merit)
  - [Training on your own Dataset](#training-on-your-own-dataset)
- [Real World Testing](#real-world-testing)
- [Citation](#citation)
- [Contributing](#contributing)
  - [Contributors](#contributors)
- [Versioning](#versioning)
- [License](#license)
- [Bugs/Issues](#bugsissues)


#  Introduction

The contamination by SARS-CoV-2 which causes the COVID-19 disease has generally spread everywhere throughout the world since the start of 2020. On January 30, 2020, the World Health Organization (WHO) proclaimed a worldwide health crisis. Analysts of various orders work alongside general health authorities to comprehend the SARS-CoV-2 pathogenesis and together with the policymakers direly create techniques to control the spread of this new disease.

Recent findings have observed imaging patterns on computed tomography (CT) for patients infected by SARS-CoV-2.

In this research, we have used a public available [SARS-COV-2 Ct-Scan Dataset](https://www.kaggle.com/plameneduardo/sarscov2-ctscan-dataset),
containing 1252 CT scans that are positive for SARS-CoV-2 infection (COVID-19) and 1230 CT scans for patients non-infected by SARS-CoV-2.
This dataset of CT scans for SARS-CoV-2 (COVID-19) identification is created by our collaborators, Plamenlancaster:
[Professor Plamen Angelov](https://www.lancaster.ac.uk/lira/people/#d.en.397371) from [Lancaster University](https://www.lancaster.ac.uk/)/
Centre Director @ [Lira](https://www.lancaster.ac.uk/lira/), & his researcher,
[Eduardo Soares PhD](https://www.lancaster.ac.uk/sci-tech/about-us/people/eduardo-almeida-soares).

These data have been collected from real patients in hospitals from Sao Paulo, Brazil.

The aim of this dataset is to encourage the research and development of artificial intelligent methods which are able to identify if a person is is infected by SARS-CoV-2 through the analysis of his/her CT scans.
As baseline result for this dataset we used an eXplainable Deep Learning approach (xDNN) which we could achieve an F1 score of **0.9678** which is very promising.

&nbsp;

# DISCLAIMER

This project should be used for research purposes only. The purpose of the project is to show the potential of Artificial Intelligence for medical support
systems such as diagnosis systems. Although the program is fairly accurate and shows good results both on paper and in real world testing, it is not meant
to be an alternative to professional medical diagnosis. I am a self taught developer with some experience in using Artificial Intelligence for detecting
certain types of cancer and COVID-19. I am not a doctor, medical or cancer/COVID-19 expert. Please use this system responsibly.

&nbsp;

# Installation

Please follow the [Installation Guide](../1/Documentation/Installation/Installation.md) to install COVID-19 xDNN Python Classifier.

# Download Dataset 

Download the dataset from this [link](https://www.kaggle.com/plameneduardo/sarscov2-ctscan-dataset)
Extract the file and move data to the (./Model/Data/) folder. 

If using linux, the dataset will be saved at the Download folder default. Use the following command for unzipping the data and moving to the Data folder. Please note that the terminal directory path should be in the main project directory.

```
unzip ~/Downloads/archive.zip -d ./Model/Data/
```

After the data is extracted cut any 10 images from both class and paste in the [Sample](./Model/Sample) Folder. This will be used for the unique image test to actual classification in the real world case scenerio. 

# Data Pre-processing 

In this techniques, we need to process the data for training and testing model. 
Execute the file [Feature_Extraction_VGG19.py](./Classes/Feature_Extraction_VGG19.py) for data processing and feature extraction from the data file. 

```
python(3) ./Classes/Feature_Extraction_VGG19.py
```

This will take time to download the VGG19 Model file and process for converting data file into the train and test features with the respect to the label and feature data in the csv format. This will be saved at (./Model/Features/) folder. 

We will be using [VGG19 Model](https://github.com/keras-team/keras-applications/blob/master/keras_applications/vgg19.py) for extracting features and data points. 

```
Model: "model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         [(None, 224, 224, 3)]     0         
_________________________________________________________________
block1_conv1 (Conv2D)        (None, 224, 224, 64)      1792      
_________________________________________________________________
block1_conv2 (Conv2D)        (None, 224, 224, 64)      36928     
_________________________________________________________________
block1_pool (MaxPooling2D)   (None, 112, 112, 64)      0         
_________________________________________________________________
block2_conv1 (Conv2D)        (None, 112, 112, 128)     73856     
_________________________________________________________________
block2_conv2 (Conv2D)        (None, 112, 112, 128)     147584    
_________________________________________________________________
block2_pool (MaxPooling2D)   (None, 56, 56, 128)       0         
_________________________________________________________________
block3_conv1 (Conv2D)        (None, 56, 56, 256)       295168    
_________________________________________________________________
block3_conv2 (Conv2D)        (None, 56, 56, 256)       590080    
_________________________________________________________________
block3_conv3 (Conv2D)        (None, 56, 56, 256)       590080    
_________________________________________________________________
block3_conv4 (Conv2D)        (None, 56, 56, 256)       590080    
_________________________________________________________________
block3_pool (MaxPooling2D)   (None, 28, 28, 256)       0         
_________________________________________________________________
block4_conv1 (Conv2D)        (None, 28, 28, 512)       1180160   
_________________________________________________________________
block4_conv2 (Conv2D)        (None, 28, 28, 512)       2359808   
_________________________________________________________________
block4_conv3 (Conv2D)        (None, 28, 28, 512)       2359808   
_________________________________________________________________
block4_conv4 (Conv2D)        (None, 28, 28, 512)       2359808   
_________________________________________________________________
block4_pool (MaxPooling2D)   (None, 14, 14, 512)       0         
_________________________________________________________________
block5_conv1 (Conv2D)        (None, 14, 14, 512)       2359808   
_________________________________________________________________
block5_conv2 (Conv2D)        (None, 14, 14, 512)       2359808   
_________________________________________________________________
block5_conv3 (Conv2D)        (None, 14, 14, 512)       2359808   
_________________________________________________________________
block5_conv4 (Conv2D)        (None, 14, 14, 512)       2359808   
_________________________________________________________________
block5_pool (MaxPooling2D)   (None, 7, 7, 512)         0         
_________________________________________________________________
flatten (Flatten)            (None, 25088)             0         
_________________________________________________________________
fc1 (Dense)                  (None, 4096)              102764544 
_________________________________________________________________
fc2 (Dense)                  (None, 4096)              16781312  
=================================================================
Total params: 139,570,240
Trainable params: 139,570,240
Non-trainable params: 0
_________________________________________________________________
```

The extracted features will be shown like this 

```
[[0.         0.         0.         ... 0.         0.         0.97085285]
 [2.2869196  0.         0.64155865 ... 0.         0.         1.4732528 ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 ...
 [0.         0.         0.         ... 0.         0.         0.91862583]
 [0.         0.         0.         ... 0.         0.         0.7122305 ]
 [0.         0.         0.07393801 ... 0.         0.         0.75918955]]
['Covid (1).png;0' 'Covid (10).png;0' 'Covid (100).png;0' ...
 'Non-Covid (997).png;1' 'Non-Covid (998).png;1' 'Non-Covid (999).png;1']
```

# Training Model 

In the Command prompt navigate to the project root directory and execute the following command:

```
python(3) main.py
```

The extracted features are further process in the xDNN model for the training purpose. 

```
###################### Data Loaded ######################
Data Shape:
X train:  (1952, 4096)
Y train:  (1952, 2)
X test:  (489, 4096)
Y test:  (489, 2)

###################### Model Trained ####################
Time:  59.88 seconds
```

Further the results are shown on the Readme file. 

## Training Results

The trained model is processed on data features extracted from the VGG19 Model and further the data peaks are , this contains a Model file which is trained on 1737 images containing xDNN Parameters.
 When the training finishes the model will show the results related to metrics and figures of merit.

```
###################### Results ##########################

Elapsed time is 76.35 seconds.
Results:

Accuracy =

    0.948875


precision =

    0.948875


recall =

    0.948875


F1 =

    0.948875


Cohens kappa =

    0.897631


Confusion_Matrix =

   242     7
    18   222

```
The figures will popup on screen with the each results outcome and saved in the [Image](./Media/Images/) folder.

![Accuracy](../1/Media/Images/accuracy.png)

_Fig 1. Accuracy_

![Precision](../1/Media/Images/recall.png)

_Fig 2. Precision, Recall and F1_

![Confusion Matrix](../1/Media/Images/confusion_matrix.png)

_Fig 3. Confusion Matrix_

### Metrics Overview

| Accuracy  | Recall     | Precision  | AUC/ROC   |
| --------- | ---------- | ---------- | --------- |
| 0.948875  |  0.948875   | 0.948875     | 0.897631    |

### Figures Of Merit

| Figures of merit     | Amount/Value      | Percentage  |
| -------------------- | ------------------| ------------|
| True Positives       | 242               | 97.188755% |
| False Positives      | 7                 | 02.811245%  |
| True Negatives       | 222               | 92.5% |
| False Negatives      | 18                | 0.75%  |
| Misclassification    | 25                | 03.561245%  |
| Sensitivity / Recall | 0.975425            | 94.8875%         |

## Training on your own Dataset

The Python file [Feature_Extraction_VGG19.py](./Classes/Feature_Extraction_VGG19.py) can be used to make the dataloader and Features extracted in csv files for training
on your own dataset. Before running the above script, paste the dataset folder with containing subfolders in the project root directory. After running
the above script save the generated Train and Test files in [**data**](./Model/Data) and features files of data_df_X_train_lite, data_df_y_train_lite, data_df_X_test_lite, data_df_y_test_lite in
[**Features**](./Model/Features) Folder.

&nbsp;

# Custom Classifier 

You can run `classifier.py` file for classifying the image from the CT Scan data. 
It will provide COVID or normal results with the prediction accurate score on the command prompt.

```
python(3) classifier.py
```

The outcome represents as per the following note for the 20 images taken from the dataset.

```
###################### Results ##########################

Test Image No:  1
Result Time:  0.16 seconds
Input Image: Covid (1060).png
Result: COVID
Prediction 0.031588138091213795

Test Image No:  2
Result Time:  0.15 seconds
Input Image: Covid (119).png
Result: COVID
Prediction 1.9993806885388816e-09

Test Image No:  3
Result Time:  0.16 seconds
Input Image: Covid (1226).png
Result: Normal
Prediction 1.5732839015365827e-09

Test Image No:  4
Result Time:  0.15 seconds
Input Image: Covid (2).png
Result: COVID
Prediction 6.70681162432005e-12

Test Image No:  5
Result Time:  0.16 seconds
Input Image: Covid (232).png
Result: COVID
Prediction 6.962768279421297e-09

Test Image No:  6
Result Time:  0.15 seconds
Input Image: Covid (294).png
Result: COVID
Prediction 9.952293710441506e-15

Test Image No:  7
Result Time:  0.15 seconds
Input Image: Covid (445).png
Result: COVID
Prediction 1.1249652679479841e-08

Test Image No:  8
Result Time:  0.15 seconds
Input Image: Covid (55).png
Result: COVID
Prediction 1.6259068607291937e-08

Test Image No:  9
Result Time:  0.17 seconds
Input Image: Covid (680).png
Result: COVID
Prediction 1.29845402431108e-06

Test Image No: 10
Result Time:  0.15 seconds
Input Image: Covid (862).png
Result: COVID
Prediction 4.352890743507003e-06

Test Image No: 11
Result Time:  0.15 seconds
Input Image: Non-Covid (1036).png
Result: Normal
Prediction 0.001772926232429088

Test Image No: 12
Result Time:  0.15 seconds
Input Image: Non-Covid (1167).png
Result: Normal
Prediction 8.162991045344149e-06

Test Image No: 13
Result Time:  0.16 seconds
Input Image: Non-Covid (1211).png
Result: Normal
Prediction 0.0002029218211931952

Test Image No: 14
Result Time:  0.16 seconds
Input Image: Non-Covid (13).png
Result: Normal
Prediction 6.747919985455099e-11

Test Image No: 15
Result Time:  0.16 seconds
Input Image: Non-Covid (271).png
Result: Normal
Prediction 0.00010900308786931037

Test Image No: 16
Result Time:  0.15 seconds
Input Image: Non-Covid (309).png
Result: Normal
Prediction 0.0015956689206031993

Test Image No: 17
Result Time:  0.15 seconds
Input Image: Non-Covid (587).png
Result: Normal
Prediction 6.708945273342042e-05

Test Image No: 18
Result Time:  0.16 seconds
Input Image: Non-Covid (69).png
Result: Normal
Prediction 4.500791479748551e-13

Test Image No: 19
Result Time:  0.17 seconds
Input Image: Non-Covid (768).png
Result: COVID
Prediction 7.071275297244958e-13

Test Image No: 20
Result Time:  0.16 seconds
Input Image: Non-Covid (871).png
Result: Normal
Prediction 1.6469236398851145e-05

```

# Real World Testing

For testing the model and getting the results on random CT Scan Images, we will upload an Image on a webpage for the given default IP Address and
Port set at localhost, then it will provide the result for the given Image.The webpage interface to upload and predict images is
one using Flask API and we will use python script [app.py](./app.py), which will call Flask API to interact with the webpage and
call the [xDNN.py](./Classes/src/xDNN.py) and [xDNN_class.py](./Classes/src/xDNN_class.py) for the classifying the function for the model to fetch and 

To test an Image, navigate to the project root(../xDNN/Projects/Python/1/) and execute the following command in command prompt:

```
python(3) app.py
```

If using localhost IP address (127.0.0.1) using for other purpose you can change the address and port and run the script. The Script will start running and initiate with the Flask API.

```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
  stacklevel=1)
 * Debugger is active!
 * Debugger PIN: 131-166-024
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now go to your default browser and search for given HTTP address. You will see a web page as shown below:

![WebPage1](../1/Media/Project_Images/Server_Start.png)

Go the browser and on the given HTTP address assigned you will be prompt to a webpage. 

![WebPage2](../1/Media/Project_Images/Webpage_image.png)

Now Upload any JPG, JPEG or PNG CT Scan image file by clicking **Upload Image**. Keep in Mind that the Image file should have at atleast size of
 (224,224) image pixels. After Uploading Image, click on **Show Results**:

 ![WebPage2](../1/Media/Project_Images/webpage_input.png)

The Web Page will provide a predict button to classify the image from the server. 

![WebPage3](../1/Media/Project_Images/webpage_predict.png)

The classifier takes time for processing the image and classifying the result as shown:

![WebPage4](../1/Media/Project_Images/webpage_covid.png)

In the command prompt or terminal, the result will shown as follows: 

```
COVID19 Detected  Prediction: 9.957084049494994e-09
127.0.0.1 - - [Date/Month/year xx:xx:xx] "←[37mPOST /predict HTTP/1.1←[0m" 200 -

```
The images can be selected multiple time and the classified results shown in least time.

&nbsp;

# Citation

```
Angelov, Plamen, and Eduardo Almeida Soares. "EXPLAINABLE-BY-DESIGN APPROACH FOR COVID-19 CLASSIFICATION VIA CT-SCAN." medRxiv (2020).
Soares, Eduardo, Angelov, Plamen, Biaso, Sarah, Higa Froes, Michele, and Kanda Abe, Daniel. "SARS-CoV-2 CT-scan dataset: A large dataset of real
patients CT scans for SARS-CoV-2 identification." medRxiv (2020). doi: https://doi.org/10.1101/2020.04.24.20078584.

Link:
https://www.medrxiv.org/content/10.1101/2020.04.24.20078584v2
```

&nbsp;

# Contributing

The Peter Moss COVID-19 AI Research Project encourages and welcomes code contributions, bug fixes and enhancements from the Github.

Please read the [CONTRIBUTING](../../../CONTRIBUTING.md "CONTRIBUTING") document for a full guide to forking our repositories and submitting your pull
requests. You will also find information about our code of conduct on this page.

## Contributors

- [Nitin Mane](https://www.leukemiaresearchassociation.ai/team/nitin-mane "Nitin Mane") - [Peter Moss Leukemia AI Research](https://www.leukemiaresearchassociation.ai "Peter Moss Leukemia AI Research")
AI R&D, Aurangabad, India.

&nbsp;

# Versioning

We use SemVer for versioning. For the versions available, see [Releases](../../../../../releases "Releases").

&nbsp;

# License

This project is licensed under the **MIT License** - see the [LICENSE](../../../LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues

We use the [repo issues](../../../../../issues "repo issues") to track bugs and general requests related to using this project. See
[CONTRIBUTING](../../../CONTRIBUTING.md "CONTRIBUTING") for more info on how to submit bugs, feature requests and proposals.
