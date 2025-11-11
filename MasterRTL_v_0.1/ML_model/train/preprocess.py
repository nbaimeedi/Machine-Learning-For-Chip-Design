import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import json, pickle
from scipy.stats import stats


bench_type = "timing"
feat_type = "feat_timing"

def load_data(label_tpe):
    if label_tpe == "Area":
        return load_data_area(label_tpe)
    elif label_tpe in ["TNS", "WNS"]:
        return load_data_timing(label_tpe)
    elif label_tpe == "Power":
        return load_data_power(label_tpe)
    



def load_data_area(label_tpe):

    #design_name = 'TinyRocket'
    feat_dir = f'../../example/feature/'

    with open(f'{feat_dir}train_area.json', 'r') as f:
        feat_design_lst = json.load(f)
    test_feat_lst = []
    test_feat_lst.extend(feat_design_lst)
    print("test_feat_lst:",test_feat_lst)

    label_dir = f'../../example/label/'
    with open(f'{label_dir}train_label.json', 'r') as f:
        label_dct = json.load(f)
    print("label_dct:",label_dct)    
    #label = label_dct[label_tpe]
    #test_label_lst = [label]
    test_label_lst = [d[label_tpe] for d in label_dct]
    print("test_label_lst:",test_label_lst)

    test_x = np.array(test_feat_lst)
    test_y = np.array(test_label_lst)

    print("test_x:",test_x)
    print("test_y:",test_y)

    return test_x, test_y

def load_data_timing(label_tpe):
    #design_name = 'TinyRocket'
    #design_name = 'Aes'
    feat_dir = f'../../example/feature/'

    with open(f'{feat_dir}train_timing.json', 'r') as f:
        feat_timing_lst = json.load(f)
    with open(f'{feat_dir}train_area.json', 'r') as f:
        feat_design_lst = json.load(f)
    test_feat_lst = []
    test_feat_lst = [design + timing for design,timing in zip(feat_design_lst, feat_timing_lst)]
    #test_feat_lst.extend(feat_design_lst)
    #test_feat_lst.extend(feat_timing_lst)
    print("test_feat_lst:",test_feat_lst)

    label_dir = f'../../example/label/'
    with open(f'{label_dir}train_label.json', 'r') as f:
        label_dct = json.load(f)
    #label = label_dct[label_tpe]
    #test_label_lst = [label]
    test_label_lst = [d[label_tpe] for d in label_dct]

    test_x = np.array(test_feat_lst)
    print("test_x:",test_x)
    test_y = np.array(test_label_lst)

    return test_x, test_y


def load_data_power(label_tpe):
    
    #design_name = 'TinyRocket'
    feat_dir = f'../../example/feature/'

    with open(f'{feat_dir}train_area.json', 'r') as f:
        feat_design_lst = json.load(f)
    test_feat_lst = []
    test_feat_lst.extend(feat_design_lst)
    print("test_feat_lst:",test_feat_lst)

    label_dir = f'../../example/label/'
    with open(f'{label_dir}train_label.json', 'r') as f:
        label_dct = json.load(f)
    print("label_dct:",label_dct)    
    #label = label_dct[label_tpe]
    #test_label_lst = [label]
    test_label_lst = [d[label_tpe] for d in label_dct]
    print("test_label_lst:",test_label_lst)

    test_x = np.array(test_feat_lst)
    test_y = np.array(test_label_lst)

    print("test_x:",test_x)
    print("test_y:",test_y)

    return test_x, test_y

def draw_fig_kf(title, y_pred, y_test, method, train_test):
    pass
