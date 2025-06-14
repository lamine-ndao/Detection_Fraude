import gc
import numpy as np
import pandas as pd
import pickle
import datetime
from sklearn.preprocessing import LabelEncoder

input_path = './Input/'
mapping_path = './Mappings/'


def basic_feature_engineering(testdata):

    
    testdata['TransactionAmt_to_mean_card1'] = testdata['TransactionAmt'] / testdata.groupby(['card1'])['TransactionAmt'].transform('mean')
    testdata['TransactionAmt_to_mean_card4'] = testdata['TransactionAmt'] / testdata.groupby(['card4'])['TransactionAmt'].transform('mean')
    testdata['TransactionAmt_to_std_card1'] = testdata['TransactionAmt'] / testdata.groupby(['card1'])['TransactionAmt'].transform('std')
    testdata['TransactionAmt_to_std_card4'] = testdata['TransactionAmt'] / testdata.groupby(['card4'])['TransactionAmt'].transform('std')
    
    testdata['id_02_to_mean_card1'] = testdata['id_02'] / testdata.groupby(['card1'])['id_02'].transform('mean')
    testdata['id_02_to_mean_card4'] = testdata['id_02'] / testdata.groupby(['card4'])['id_02'].transform('mean')
    testdata['id_02_to_std_card1'] = testdata['id_02'] / testdata.groupby(['card1'])['id_02'].transform('std')
    testdata['id_02_to_std_card4'] =testdata['id_02'] / testdata.groupby(['card4'])['id_02'].transform('std')
    

    testdata['D15_to_mean_card1'] = testdata['D15'] / testdata.groupby(['card1'])['D15'].transform('mean')
    testdata['D15_to_mean_card4'] = testdata['D15'] / testdata.groupby(['card4'])['D15'].transform('mean')
    testdata['D15_to_std_card1'] = testdata['D15'] / testdata.groupby(['card1'])['D15'].transform('std')
    testdata['D15_to_std_card4'] = testdata['D15'] /testdata.groupby(['card4'])['D15'].transform('std')


    testdata['D15_to_mean_addr1'] = testdata['D15'] / testdata.groupby(['addr1'])['D15'].transform('mean')
    testdata['D15_to_mean_addr2'] = testdata['D15'] / testdata.groupby(['addr2'])['D15'].transform('mean')
    testdata['D15_to_std_addr1'] = testdata['D15'] / testdata.groupby(['addr1'])['D15'].transform('std')
    testdata['D15_to_std_addr2'] = testdata['D15'] / testdata.groupby(['addr2'])['D15'].transform('std')


    testdata[['P_emaildomain_1', 'P_emaildomain_2', 'P_emaildomain_3']] = testdata['P_emaildomain'].str.split('.', expand=True)
    testdata[['R_emaildomain_1', 'R_emaildomain_2', 'R_emaildomain_3']] = testdata['R_emaildomain'].str.split('.', expand=True)
    testdata[['P_emaildomain_1', 'P_emaildomain_2', 'P_emaildomain_3']] = testdata['P_emaildomain'].str.split('.', expand=True)
    testdata[['R_emaildomain_1', 'R_emaildomain_2', 'R_emaildomain_3']] = testdata['R_emaildomain'].str.split('.', expand=True)
       
    gc.collect()
  
    return testdata



