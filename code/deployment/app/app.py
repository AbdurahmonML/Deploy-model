# import streamlit as st
# import requests


import streamlit as st
import requests
import json

st.title("ML Model Prediction App")

st.write("Please provide the following details to get a prediction:")

MedInc = st.number_input("Median Income in block group", min_value=0.0, step=0.01)
HouseAge = st.number_input("Median house age in block group", min_value=0.0, step=0.01)
AveRooms = st.number_input("Average number of rooms per household", min_value=0.0, step=0.01)
AveOccup = st.number_input("Average number of household members", min_value=0.0, step=0.01)
Latitude = st.number_input("Latitude of the block group", step=0.01)
Longitude = st.number_input("Longitude of the block group", step=0.01)
Population = st.number_input("Population in the block group", min_value=0.0, step=1.0)
Households = st.number_input("Number of households in the block group", min_value=0.0, step=1.0)

if st.button("Predict"):
    input_data = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude,
        "Population": Population,
        "Households": Households
    }

    try:
        response = requests.post("http://backend:8001/predict", data=json.dumps(input_data), headers={"Content-Type": "application/json"})
        
        # Check if the request was successful
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.success(f"Prediction: {prediction}")
        else:
            st.error(f"Error: Unable to get a prediction. Status code {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
