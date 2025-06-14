import numpy as np
import pickle
import xgboost as xgb
from xgboost import XGBClassifier
from preprocessing import *
import joblib


clf_path = './Classifiers/'




def predict_proba(testdata):
    testdata = preprocess(testdata)

    # Charger le modèle
    with open(clf_path + 'clf_0.pkl', 'rb') as handle:
        clf_0 = pickle.load(handle)

    # Récupérer les colonnes utilisées à l'entraînement
    training_columns = clf_0.feature_name_

    # Aligner les colonnes du test
    for col in training_columns:
        if col not in testdata.columns:
            testdata[col] = 0  # ou np.nan

    testdata = testdata[training_columns]

    # Prédire
    test_proba = clf_0.predict_proba(testdata)[:, 1]
    return test_proba
