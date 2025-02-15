import streamlit as st
import pickle
import base64
import numpy as np

class ReshapeTransformer():
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Reshape the data to (n_samples, 1, n_features)
        return X.reshape(X.shape[0], 1, X.shape[1])
    
# Page title and introduction
st.title('Fraud Credit Catcher.ML 🦹‍♂')
st.subheader("Detect potential fraudulent transactions")

# Load the pre-trained model
with open('asse.pkl', 'rb') as file:
    model = pickle.load(file)

# Page layout
col1, col2 = st.columns([1, 2])

# Result area in the layout
col1.subheader('Result:')
a = []

# Form for user inputs
with st.form('detection'):
    # User inputs for transaction details
    																														

    a.append(float(st.text_input('Time', '406')))
    a.append(float(st.text_input('V1', '-2.312226542')))
    a.append(float(st.text_input('V2', '1.951992011')))
    a.append(float(st.text_input('V3', '-1.609850732')))
    a.append(float(st.text_input('V4', '3.997905588')))
    a.append(float(st.text_input('V5', '-0.522187865')))
    a.append(float(st.text_input('V6', '-1.426545319')))
    a.append(float(st.text_input('V7', '-2.537387306')))
    a.append(float(st.text_input('V8', '1.391657248')))
    a.append(float(st.text_input('V9', '-2.770089277')))
    a.append(float(st.text_input('V10', '-2.772272145')))
    a.append(float(st.text_input('V11', '3.202033207')))
    a.append(float(st.text_input('V12', '-2.899907388')))
    a.append(float(st.text_input('V13', '-0.595221881')))
    a.append(float(st.text_input('V14', '-4.289253782')))
    a.append(float(st.text_input('V15', '0.38972412')))
    a.append(float(st.text_input('V16', '-1.14074718')))
    a.append(float(st.text_input('V17', '-2.830055675')))
    a.append(float(st.text_input('V18', '-0.016822468')))
    a.append(float(st.text_input('V19', '0.416955705')))
    a.append(float(st.text_input('V20', '0.126910559')))
    a.append(float(st.text_input('V21', '0.517232371')))
    a.append(float(st.text_input('V22', '-0.035049369')))
    a.append(float(st.text_input('V23', '-0.465211076')))
    a.append(float(st.text_input('V24', '0.320198199')))
    a.append(float(st.text_input('V25', '0.044519167')))
    a.append(float(st.text_input('V26', '0.177839798')))
    a.append(float(st.text_input('V27', '0.261145003')))
    a.append(float(st.text_input('V28', '-0.143275875')))
    a.append(float(st.text_input('Amount', '0')))
    
# Button to submit the form
    predict = st.form_submit_button('Predict')


# Perform prediction after form submission
if predict:
    # Make prediction using the loaded model
   # result = model.predict([a])
    
    # Display prediction result
    print(model.predict(np.array(a).reshape(1,-1)))
    if model.predict(np.array(a).reshape(1,-1)) > 0.4:
        col2.title('Fraud Detected')
    else:
        col2.title('Transaction Safe')