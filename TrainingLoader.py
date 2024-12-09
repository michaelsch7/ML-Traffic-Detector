import os
import cv2
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

def load_arrays_from_pics():
    i=0
    folder_path = 'ClassNoTraffic'
    rgb_data_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg')): 
            file_path = os.path.join(folder_path, filename)
            img = cv2.imread(file_path)
            rgb_data_list.append(img.reshape(1,-1))
    
    no_traf = []
    for i in range(len(rgb_data_list)):  
        array_traffic = np.array(rgb_data_list[i]).reshape(240, 352, 3)
        no_traf.append(array_traffic)
    
    i=0
    folder_path = 'ClassTraffic'
    rgb_data_list2 = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg')): 
            file_path = os.path.join(folder_path, filename)
            img = cv2.imread(file_path)
            rgb_data_list2.append(img.reshape(1,-1))
    
    traf = []
    for i in range(len(rgb_data_list2)):  
        array_traffic2 = np.array(rgb_data_list2[i]).reshape(240, 352, 3)
        traf.append(array_traffic2)

    return np.array(traf), np.array(no_traf)

def create_train_data_from_array(traffic: np.array, no_traffic: np.array):
    
    X_train, X_test, y_train, y_test = train_test_split(traffic, np.ones(len(traffic)), test_size=0.2, random_state=42)
    X_train2, X_test2, y_train2, y_test2 = train_test_split(no_traffic, np.zeros(len(no_traffic)), test_size=0.2, random_state=42)
    
    X_train = np.concatenate((X_train, X_train2), axis=0)
    y_train = np.concatenate((y_train, y_train2), axis=0)
    X_test = np.concatenate((X_test, X_test2), axis=0)
    y_test = np.concatenate((y_test, y_test2), axis=0)
    
    X_train, y_train = shuffle(X_train, y_train, random_state=42)
    X_test, y_test = shuffle(X_test, y_test, random_state=42)
    
    return X_train, X_test, y_train, y_test