import pandas as pd
import streamlit as st 
from joblib import load

model = load('random_rorest2.joblib')

st.title('Laptop Price Prediction App')

st.header('Enter Laptop Information')
company = st.selectbox('Company',('Apple', 'HP', 'Acer', 'Asus', 'Dell', 'Lenovo', 'Chuwi', 'MSI','Microsoft', 'Toshiba', 'Huawei', 'Xiaomi', 'Vero', 'Razer','Mediacom', 'Samsung', 'Google', 'Fujitsu', 'LG'))
typename = st.selectbox('TypeName',('Ultrabook', 'Notebook', 'Gaming', '2 in 1 Convertible','Workstation'))
inches = st.number_input("Inches",min_value = 0.0,max_value=100.0,value=1.37) 
ram = st.selectbox('Ram',(8, 16,  4,  2, 12,  6, 32, 24, 64))
Memory = st.number_input('Memory',min_value=0,max_value=10000,value=128)
gpu = st.selectbox('Gpu',('Intel', 'AMD', 'Nvidia'))
opsys = st.selectbox('OpSys',('macOS', 'No OS', 'Windows 10', 'Linux', 'Chrome OS', 'Windows 7'))
Touchscreen = st.selectbox('TouchScreen',("Yes","No"))
ScreenHeight = st.number_input('Screen Heigth',min_value=0,max_value=10000,value=2560)
Screenweight = st.number_input('Screen Weight',min_value=0,max_value=10000,value=1600)
cpubrand = st.selectbox('Cpu Brand',('Intel', 'AMD'))
cpuhz = st.number_input('Cpu HZ',min_value=0.0,max_value=10.0,value=2.3)


# Prediction
if st.button('Predict Price'):
    input_features = ([[company, typename, inches, ram, Memory, gpu, opsys, Touchscreen, ScreenHeight, Screenweight, cpubrand,cpuhz]])
    prediction = model.predict(input_features)
    st.success(f"The predicted price of the laptop is: ${prediction[0]:.2f}")
    
    
    