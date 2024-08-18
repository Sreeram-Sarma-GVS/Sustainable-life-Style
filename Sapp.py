import streamlit as st
import numpy as np
import pandas as pd
import pickle
import sklearn
from sklearn.ensemble import RandomForestClassifier

image_path = 'innomatics-logo-img.png'  # Replace with your actual PNG image file path

# Display the PNG image
st.image(image_path)

st.title("Building a Sustainable Future: Join Our Journey")

file_path = r'C:\Users\Administrator\MachineLearning\sustainable_life_file\sustainablelifestyle.pkl'
#new
with open(file_path , 'rb') as f:
    model = pickle.load(f)



Age=st.number_input("enter the Age of the participant:")
Location=st.selectbox(label="enter the location of the participant",options=['Urban','Suburban','Rural'])
DietType=st.selectbox(label="enter the diet type of the participant:",options=['Mostly Plant-Based', 'Balanced', 'Mostly Animal-Based'])

LocalFoodFrequency=st.selectbox(label="enter the local food frequency of the participant:",options=['Often', 'Sometimes', 'Rarely', 'Always'])
TransportationMode=st.selectbox(label="enter the transportation mode of the participant:",options=['Bike', 'Public Transit', 'Car', 'Walk'])
EnergySource= st.selectbox(label="enter the energy source of the participant:",options=['Renewable', 'Mixed', 'Non-Renewable'])
HomeType=st.selectbox(label="enter the home type of the participant:",options=['Apartment', 'House', 'Other'])
HomeSize=st.slider(label="homesize",min_value=400,max_value=3000,value=400,step=1)
ClothingFrequency=st.selectbox(label="enter the clothing frequency of the participant:",options=['Often', 'Sometimes', 'Rarely', 'Always'])
Stype=[True,False]
SustainableBrands=st.radio("enter the Sustainable Brands",Stype)
EnvironmentalAwareness=st.slider(label="Environment awareness",min_value=1,max_value=5,value=1,step=1)
CommunityInvolvement=st.selectbox(label="enter the community involvement of the participant:",options= ['High', 'Moderate', 'Low'])
MonthlyElectricityConsumption=st.number_input("enter the monthly Electricity Consumption")
MonthlyWaterConsumption=st.number_input("enter the monthly Water Consumption")
Gtype=['Male','Female','non-binary','Prefer not to say']
Gender=st.radio('Gender',Gtype)
st.write("your gender is :",Gender)
UsingPlasticProducts=st.selectbox(label="enter the using plastic product of the participant:",options=['Rarely', 'Sometimes', 'Often', 'Never'])
DisposalMethods=st.selectbox(label="enter the disposal method of the participant:",options= ['Composting', 'Recycling', 'Landfill', 'Combination'])
PhysicalActivities=st.selectbox(label="enter the physical activity of the participant:",options=['High', 'Moderate', 'Low'])


if st.button('Submit'):

    input_values=[Age, Location, DietType, LocalFoodFrequency,
        TransportationMode, EnergySource, HomeType, HomeSize,
        ClothingFrequency, SustainableBrands, EnvironmentalAwareness,
        CommunityInvolvement, MonthlyElectricityConsumption,
        MonthlyWaterConsumption, Gender, UsingPlasticProducts,
        DisposalMethods, PhysicalActivities]


    col_name=['Age', 'Location', 'DietType', 'LocalFoodFrequency',
        'TransportationMode', 'EnergySource', 'HomeType', 'HomeSize',
        'ClothingFrequency', 'SustainableBrands', 'EnvironmentalAwareness',
        'CommunityInvolvement', 'MonthlyElectricityConsumption',
        'MonthlyWaterConsumption', 'Gender', 'UsingPlasticProducts',
        'DisposalMethods', 'PhysicalActivities']

    input_df = pd.DataFrame([input_values], columns=col_name)
    result=model.predict(input_df)
    st.write("Rating is :",result)