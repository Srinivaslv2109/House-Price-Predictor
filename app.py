#necessary libraries
import pandas as pd
import streamlit as st
import pickle

df=pd.read_csv('cleaned_house_data.csv')
with open('RFmodelHPP.pkl','rb') as f:
    model=pickle.load(f)

with st.sidebar:
    st.title('House Price Predictor')
    st.image('house_logo.png')

def get_encoded_loc(location):
    for loc,encoded in zip(df['location'],df['enc_loc']):
        if location==loc:
            return encoded
#user inputs location,bhk,sqft,bath
location=st.selectbox('Location:',options=df['location'].unique())
location=get_encoded_loc(location)
sqft=st.number_input("Total_sqft:",min_value=300)
BHK=st.selectbox('BHK:',options=sorted(df['size'].unique()))
Bath=st.selectbox('No.of Bathrooms:',options=sorted(df['bath'].unique()))

if st.button('Predict Price'):
    data=[[BHK,sqft,Bath,location]]
    pred=model.predict(data)[0]
    st.subheader(str(int(pred))+'  Lakhs')

