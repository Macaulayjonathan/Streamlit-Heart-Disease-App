# -*- coding: utf-8 -*-
"""
Created on Sunday, August 23, 2020.

@author: Macaulay.Jonathan
"""



import numpy as np
import pickle
import pandas as pd
import streamlit as st


pickle_in = open("classifier.pk1","rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_heart_disease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    
    prediction=classifier.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    print(prediction)
    return prediction

def main():
    st.title("Heart Disease Predictor")
    html_temp = """
    <div style = "background-color:tomato; padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Heart Disease Predictor ML App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    age = st.text_input("Age", "Type here")
    sex = st.text_input("Sex", "Type here")
    cp = st.text_input("Cp", "Type here")
    trestbps = st.text_input("Trestbps", "Type here")
    chol = st.text_input("Chol", "Type here")
    fbs = st.text_input("Fbs", "Type here")
    restecg = st.text_input("Restecg", "Type here")
    thalach = st.text_input("Thalach", "Type here")
    exang = st.text_input("Exang", "Type here")
    oldpeak = st.text_input("Oldpeak", "Type here")
    slope = st.text_input("Slope", "Type here")
    ca = st.text_input("Ca", "Type here")
    thal = st.text_input("Thal", "Type here")
    result=""
    if st.button("Predict"):
        result=predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    st.success("The output is {}".format(result))
    if st.button("About"):
        st.text("Let's Learn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

