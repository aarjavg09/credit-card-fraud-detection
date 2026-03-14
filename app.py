import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('fraud_model.pkl', 'rb'))

st.title("Credit Card Fraud Detection")
st.write("Transaction details bharo — fraud hai ya normal pata chalega!")

amount = st.number_input("Transaction Amount", 
                          min_value=0.0, 
                          max_value=100000.0, 
                          value=100.0)

time = st.number_input("Transaction Time", 
                        min_value=0.0, 
                        max_value=200000.0, 
                        value=50000.0)

v_features = []
for i in range(1, 29):
    v = st.slider(f"V{i}", 
                  min_value=-10.0, 
                  max_value=10.0, 
                  value=0.0)
    v_features.append(v)

if st.button("Check Transaction"):
    input_data = [time] + v_features + [amount]
    
    feature_names = ['Time','V1','V2','V3','V4','V5','V6','V7',
                     'V8','V9','V10','V11','V12','V13','V14',
                     'V15','V16','V17','V18','V19','V20','V21',
                     'V22','V23','V24','V25','V26','V27','V28',
                     'Amount']
    
    input_df = pd.DataFrame([input_data], columns=feature_names)
    prediction = model.predict(input_df)
    
    if prediction[0] == 1:
        st.error("FRAUD Transaction Detected!")
    else:
        st.success("Normal Transaction — Safe!")