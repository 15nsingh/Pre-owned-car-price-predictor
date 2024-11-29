import streamlit as st
import pickle
import pandas as pd


car_list= pickle.load(open("car.pkl","rb"))
company_list=sorted(car_list["company"].unique())
model_list = sorted(car_list["name"].unique())
fuel_list = sorted(car_list["fuel_type"].unique())
model = pickle.load(open("LinearRegressionModel.pkl", "rb"))

st.markdown("<h1 style='text-align: center; color: black;'>Car Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: black;'>A Portfolio Project by - Nikhil Singh</h2>", unsafe_allow_html=True)

company = st.selectbox(
    "Select Company",
    company_list, index=None)

filtered_list = []
for i in model_list:
    parts = i.split()
    if parts[0] == company:
        filtered_list.append(i)
car_model = st.selectbox(
    "Select Model",
    filtered_list, index=None
)
year = st.slider("Select Year", 2000,2024)

kms_driven = st.number_input("Enter Kms Driven", 0, 999999, value=None, placeholder="Kms...")
st.write(kms_driven," Kilometers driven")

fuel_type = st.selectbox(
    "Select Fuel Type",
    fuel_list, index=None
)
def prediction():
    st.write(company,car_model,year,kms_driven,fuel_type)
    estimate = model.predict(pd.DataFrame([[car_model,company,year,kms_driven,fuel_type]] , columns=["name","company","year","kms_driven","fuel_type"]))
    st.write(str(round(estimate[0],2)))


left, middle, right = st.columns(3)
if middle.button("Estimate Price", type="primary"):
    prediction()


