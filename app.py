import streamlit as st
import numpy as np
from PIL import Image
import pickle
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Crop Recommender System", layout="wide")

# --- Important Functions ---
def load_url(url):
    r = requests.get(url)       # to access the animation link
    if r.status_code !=200:
        return None
    return r.json()

# Animation Assests
plant = load_url("https://assets9.lottiefiles.com/packages/lf20_xd9ypluc.json")
farmer = load_url("https://assets1.lottiefiles.com/packages/lf20_CgexnTerux.json")

recommender = pickle.load(open('CropRecommender (2).sav','rb'))

def crs_output(input_data):
    input_array = np.array(input_data)
    final_input = input_array.reshape(1,-1)
    prediction = recommender.predict(final_input)
    output = prediction[0]
    return (f"Field conditions are most suitable for '{output}'")

def main():

    with st.container():
        c1, c2 = st.columns((1,1.5))
        with c1:
            st.title("Crop Recommendation System")
            st.write("")
            st.write('Algorithm used: K-nearest Neighbors')
            st.write("")
            st.write("This model takes 7 different parameters and recommends 22 different types of crops.")
            st.write("")
            st.write("Data Source: Crop Recommendation Dataset Kaggle")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write('---Scroll down to test the model---')



        with c2:
            st_lottie(farmer, height = 650, key="farmer")

    with st.container():
        col1, col2 = st.columns((1, 1))
        with col1:
            # -- Time to take user input --
            # our model takes 7 parameters so we need 7 input fields

            n = st.number_input("Nitrogen Level of Your field", min_value=0.0, max_value=100.0)
            p = st.number_input("Phosphorus Level of Your field", min_value=0.0, max_value=100.0)
            k = st.number_input("Potasium Level of Your field", min_value=0.0, max_value=100.0)
            temperature = st.number_input("Average temperature(°C) in your area", min_value=0.0, max_value=100.0)
            humidity = st.number_input("Relative humidity in %", min_value=0.0, max_value=100.0)
            ph_value = st.number_input("Ph value of the soil", min_value=0.0, max_value=15.0)
            rainfall = st.number_input("Average rainfall(in mm) in your area", min_value=0.0)

            # --- Code for recommendation ---
            crop_output = ""
            # --- creating a button ---
            if st.button("Find The Crop"):
                crop_output = crs_output([n, p, k, temperature, humidity, ph_value, rainfall])
                st.success(crop_output)  # executes after successful button press

                with col2:
                    st_lottie(plant, height=800, key="plant")




main()

### Hide the name ###

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)