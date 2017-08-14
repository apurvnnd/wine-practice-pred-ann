from csv import reader

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('wine.data')

X = dataset.iloc[:, 1:14].values
y = dataset.iloc[:, :1].values

#Error mention: hadn't applied onehotencoder before
#onehotencoder applied on y dataset 
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [0])
y = onehotencoder.fit_transform(y).toarray()
#y = y[:, 1:] #to prevent data duplicy 
#Note: no need for above mentioned code for data duplicy

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Making the ANN

#Importing keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

#Initializing the ANN
classifier = Sequential()

#Adding input layer and first hidden layer
classifier.add(Dense(output_dim = 7, init = 'uniform', activation = 'relu', input_dim = 13))

#Adding second hidden layer
classifier.add(Dense(output_dim = 7, init = 'uniform', activation = 'relu'))

#Adding the output layer
classifier.add(Dense(output_dim = 3, init = 'uniform', activation = 'softmax')) 
#edit: output_dim changed to 3 and activation changed from sigmoid to softmax because of multiple outputs

#Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
#edit: loss changed from binary to categorical_crossentropy 

#Fitting the ANN to the training set
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 50)


# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)
