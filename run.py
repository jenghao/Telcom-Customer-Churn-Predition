#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import flask
from flask import Flask, jsonify, request, render_template
import json
import numpy as np
import pickle


# In[ ]:


from sklearn.ensemble import GradientBoostingClassifier as gbc


# In[ ]:


with open("model.pk1", "rb") as f:
    model = pickle.load(f)


# In[ ]:


app = Flask(__name__)


# In[ ]:


def predict_churn(feature_list):
    feature = np.array(feature_list)
    feature = feature.reshape(1, -1)
    pred = model.perdict(feature)
    reture pred


# In[ ]:


def main():
    gbc.title("Customer Churn Prediction")
    feature_list = ['Gender', 'Senior Citizen', 'Partner', 'Dependents', 'Monthly Charges', 'Total Charges', 
                    'Paperless Billing', 'CLTV', 'Los Angeles Distance', 'San Francisco Distance', 'San Diago Distance', 
                    'Loyalty', 'Not_Help Score', 'Multiple Lines_No', 'Multiple Lines_No Phone Service', 
                    'Multiple Lines_Yes', 'Internet Service_DSL', 'Internet Service_Fiber Optic', 'Internet Service_No', 
                    'Online Security_No', 'Online Security_Yes', 'Online Backup_No', 'Online Backup_Yes', 'Device Protection_No', 
                    'Device Protection_Yes', 'Tech Support_No', 'Tech Support_Yes', 'Streaming TV_No', 'Streaming TV_Yes', 
                    'Streaming Movies_No', 'Streaming Movies_Yes', 'Contract Month-to-Month', 'Contract_One Year', 
                    'Contract_Two Years', 'Payment Method_Bank Transfer(Automatic)', 'Payment Method_Credit Card(Automatic)', 
                    'Payment Method_Eleectronic Check', 'Payment Method_Mailed Check']
    for i in feature_list:
        feature_list[i] = gbc.text_input(i)
        
    result = ""
    if gbc.buttom("predict"):
        result = predict_churn(feature_list)
    gbc.success("The result is {}".format(result))
    
if __name__ == "__main__":
    app.run(debug = True, host = "127.0.0.1", port = 5000)


# In[ ]:





# In[ ]:





# In[ ]:




