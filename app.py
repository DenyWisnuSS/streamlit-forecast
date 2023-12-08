import pickle
import streamlit as st
import pandas as pd
import  matplotlib.pyplot as plt

model = pickle.load(open('forecast_CO2.sav', 'rb'))

data = pd.read_excel("CO2 dataset.xlsx")
data['Year'] = pd.to_datetime(data['Year'], format='%Y')
data.set_index(['Year'], inplace=True)

st.title('Forecasting Air Quality')
year = st.slider("Set Year", 1,30, step=1)

pred = model.forecast(year)
pred = pd.DataFrame(pred, columns=['CO2'])

if  st.button("Predict"):

    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax = plt.subplots()
        data['CO2'].plot(style='--', color='red', legend=True, label='known')
        pred['CO2'].plot(color='b', legend=True, label='Prediction')
        st.pyplot(fig)