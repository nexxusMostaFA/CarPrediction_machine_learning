import streamlit as st
import pandas as pd
import pickle
import numpy as np
import math
import random

 
data = pickle.load(open(r"C:\Users\mostafa\Desktop\Cars_prediction_model.sav" ,  'rb'))

 
st.title('Car Price Prediction')
st.sidebar.header('RESULTS')
st.image("https://www.carandbike.com/_next/image?url=https%3A%2F%2Fmedia.mahindrafirstchoice.com%2Flive_web_images%2Fusedcarsimg%2Fmfc%2F1551%2F622756%2Fcover_image-20241205161329.jpg&w=1920&q=75")
st.info('Application For Predicting Car Price')
st.sidebar.info('Application For Predicting Car Price')

 
m1 = ['LEXUS', 'CHEVROLET', 'HONDA', 'FORD', 'HYUNDAI', 'TOYOTA', 'MERCEDES-BENZ', 'OPEL', 'PORSCHE', 'BMW', 'JEEP', 'VOLKSWAGEN', 'AUDI', 'RENAULT', 'NISSAN', 'SUBARU', 'DAEWOO', 'KIA', 'MITSUBISHI', 'SSANGYONG', 'MAZDA', 'GMC', 'FIAT', 'INFINITI', 'ALFA ROMEO', 'SUZUKI', 'ACURA', 'LINCOLN', 'VAZ', 'GAZ', 'CITROEN', 'LAND ROVER', 'MINI', 'DODGE', 'CHRYSLER', 'JAGUAR', 'ISUZU', 'SKODA', 'DAIHATSU', 'BUICK', 'TESLA', 'CADILLAC', 'PEUGEOT', 'BENTLEY', 'VOLVO', 'სხვა', 'HAVAL', 'HUMMER', 'SCION', 'UAZ', 'MERCURY', 'ZAZ', 'ROVER', 'SEAT', 'LANCIA', 'MOSKVICH', 'MASERATI', 'FERRARI', 'SAAB', 'LAMBORGHINI', 'ROLLS-ROYCE', 'PONTIAC', 'SATURN', 'ASTON MARTIN', 'GREATWALL']
m2 = [21, 16, 23, 58, 36, 61, 46, 41, 8, 55, 11, 5, 28, 39, 54, 35, 18, 15, 56, 32, 42, 3, 10, 38, 13, 27, 0, 60, 26, 53, 9, 33, 6, 43, 64, 20, 31, 7, 51, 24, 45, 30, 37, 49, 62, 1, 50, 17, 25, 12, 57, 4, 22, 59, 63, 48, 52, 40, 34, 14, 29, 47, 44, 2, 19]
Manufacturer_mapping = dict(zip(m1, m2))
Manufacturer1 = st.selectbox('Manufacturer', m1)
Manufacturer = Manufacturer_mapping[Manufacturer1]

 
mm1 = ['RX 450', 'Equinox', 'FIT', 'E 230 124', 'RX 450 F SPORT', 'Prius C aqua']
mm2 = [684, 661, 1305, 582, 1243, 1169]
Model_mapping = dict(zip(mm1, mm2))
Model1 = st.selectbox('Model', mm1)
Model = Model_mapping[Model1]

 
c1 = ['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon', 'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine', 'Pickup']
c2 = [3, 4, 9, 10, 7, 0, 1, 6, 2, 8, 5]
Category_Mapping = dict(zip(c1, c2))
Category1 = st.selectbox('Category', c1)
Category = Category_Mapping[Category1]

# Leather Interior  
l1 = ['yes', 'no']
l2 = [0, 1]
leather_mapping = dict(zip(l1, l2))
Leather1 = st.selectbox('Leather interior', l1)
Leather = leather_mapping[Leather1]

# Fuel Type  
f1 = ['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG', 'Hydrogen']
f2 = [5, 2, 1, 6, 4, 0, 3]
Fuel_Mapping = dict(zip(f1, f2))
Fuel1 = st.selectbox('Fuel type', f1)
Fuel = Fuel_Mapping[Fuel1]

# Gear Box Type  
g1 = ['Automatic', 'Tiptronic', 'Variator', 'Manual']
g2 = [3, 0, 2, 1]
Gear_mapping = dict(zip(g1, g2))
Gear1 = st.selectbox('Gear box type', g1)
Gear = Gear_mapping[Gear1]

# Drive Wheels  
d1 = ['4x4', 'Front', 'Rear']
d2 = [1, 0, 2]
Drive_mapping = dict(zip(d1, d2))
Drive1 = st.selectbox('Drive wheels', d1)
Drive = Drive_mapping[Drive1]

# Wheel  
w1 = ['Left wheel', 'Right-hand drive']
w2 = [1, 0]
Wheel_mapping = dict(zip(w1, w2))
Wheel1 = st.selectbox('Wheel', w1)
Wheel = Wheel_mapping[Wheel1]

# Color  
cc1 = ['Silver', 'Black', 'White', 'Grey', 'Blue', 'Green', 'Red', 'Sky blue', 'Orange', 'Yellow', 'Brown', 'Golden', 'Beige', 'Carnelian red', 'Purple', 'Pink']
cc2 = [1, 14, 12, 7, 2, 13, 11, 6, 15, 3, 5, 0, 8, 4, 10, 9]
color_mapping = dict(zip(cc1, cc2))
Color1 = st.selectbox('Color', cc1)
Color = color_mapping[Color1]

# Engine Volume
Engine = st.selectbox('Engine volume', [1.3, 2.5, 2., 1.8, 2.4, 1.6, 2.2, 1.5, 1.4, 2.3, 1.2, 1.7, 2.9, 1.9, 3.5, 2.1, 2.7, 1., 0.8, 3., 3.3, 2.8, 3.2, 1.1])

# Airbags
Airbags = st.selectbox('Airbags', [2., 0., 4., 12., 8., 10., 6., 1., 16., 7., 9., 5., 11., 3., 14., 15., 13.])

# Age
carAge = st.number_input('Age')

# Mileage
Mileage = st.number_input('Mileage')

# Levy
Levy = st.number_input('Levy')

 
df = pd.DataFrame({
    'Price': 0,   
    'Levy': Levy,
    'Engine volume': Engine,
    'Mileage': Mileage,
    'Cylinders': 4,   
    'Airbags': Airbags,
    'carAge': carAge,
    'Manufacturer': Manufacturer,
    'Model': Model,
    'Category': Category,
    'Leather interior': Leather,
    'Fuel type': Fuel,
    'Gear box type': Gear,
    'Drive wheels': Drive,
    'Wheel': Wheel,
    'Color': Color
}, index=[0])

 
print("Columns in df:", df.columns)

# Predict Button
p = st.sidebar.button('Predict Price')
if p:
    Pre = data.predict(df.drop(columns=['Price']))   
    st.sidebar.write('Price is:', Pre)
    st.table(df)