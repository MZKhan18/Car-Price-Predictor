import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title("Car Price Estimation")

# Commpany Name
company = st.selectbox("Car Company",df['company'].unique())

#Model
company_index = df[df['company']==company].index
model = st.selectbox("Car Model",df['car_model'][company_index].unique())

#Variant
model_index = df[df['car_model']==model].index
variant = st.selectbox("Variant",df['car_name'][model_index].unique())

# kms driven
kms_driven = st.number_input("How many KMs driven")

# gear
gear = st.selectbox("transmission",['Automatic','Manual'])

#Manufacture year
man_year = st.number_input('Manufacture Year')

#engine
enigne = st.number_input("Engine")

# seats
seats = st.selectbox("Seats",df['Seats'].unique())

# fuel type
fuel = st.selectbox("Fuel Type",df['fuel_type'].unique())

#owner
owner= st.selectbox("Owner",[1,3,4,5,6,'other'])

if st.button('Predict Price'):
    # pass
    if gear == 'Automatic':
        gear =0
    else:
        gear = 1

    if owner == 'other':
        ips =0



    query = np.array([kms_driven,fuel,man_year,enigne,seats,owner,company,model,gear,variant])

    query = query.reshape(1,10)
    st.title('Price Of Car is Rs '+str(int(np.exp(pipe.predict(query)[0]))) + ' Lakh')


