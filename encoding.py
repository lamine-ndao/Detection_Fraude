import gc
import pickle
from sklearn.preprocessing import LabelEncoder

mapping_path = './Mappings/'


def label_encode_testdata(testdata, cat_cols_dict):
    """
    Encode les colonnes catégorielles de testdata avec LabelEncoder, indépendamment.
    
    Args:
        testdata (pd.DataFrame): données à encoder.
        cat_cols_dict (list): liste des colonnes catégorielles.
        
    Returns:
        pd.DataFrame: testdata encodé.
    """
    for col in cat_cols_dict:
        if col in testdata.columns:
            le = LabelEncoder()
            combined = list(testdata[col].astype(str).values)
            le.fit(combined)
            testdata[col] = le.transform(testdata[col].astype(str).values)

    return testdata






    