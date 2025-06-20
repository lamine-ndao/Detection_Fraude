import gc
import pickle
import pandas as pd
from feature_engineering import *
from encoding import *

input_path = './Input/'
mapping_path = './Mappings/'


def preprocess(testdata):
    placeholder_file = pd.read_csv(input_path + 'placeholder_file.csv')
    testdata.columns = placeholder_file.columns.values
    data = pd.DataFrame(testdata.values, columns=placeholder_file.columns)
    data = data.astype(testdata.dtypes.to_dict()) 
    testdata = data
    del placeholder_file, data

    testdata = basic_feature_engineering(testdata)

    # Drop features
    with open(mapping_path + 'drop_features.pkl', 'rb') as handle:
        features_to_drop = pickle.load(handle)
    testdata.drop(features_to_drop, axis=1, inplace=True)
    del features_to_drop

    # Encode les colonnes catégorielles
    with open(mapping_path + 'cat_cols_dict.pkl', 'rb') as f:
        cat_cols_dict = pickle.load(f)
    testdata = label_encode_testdata(testdata, cat_cols_dict)

    gc.collect()
    return testdata


