import streamlit as st
import joblib
import numpy as np
import logging

# Configure logging to help debug issues
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    logger.info("Attempting to load model...")
    model = joblib.load("rfr_model.pkl")
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    st.error(f"Error loading model: {e}")
    st.stop()


st.title("House Price Prediction app")

st.divider()

st.write("This app predicts the price of a house based on various features.")

st.divider()

bedrooms = st.number_input("Number of bedrooms", min_value=0 , max_value=10, value=0)
bathrooms = st.number_input("Number of bathrooms", min_value=1 , max_value=5, value=1 )
living_area = st.number_input("Living area (in square feet)", min_value=100 , max_value=10000, value=1000)
condition = st.slider("Condition of the house", min_value=0, max_value=4, value=2)
number_of_schools = st.number_input("Number of schools nearby", min_value=0 , max_value=7, value=0)

st.divider()

x = [[bedrooms, bathrooms, living_area, condition, number_of_schools]],

preict_button = st.button("Predict Price !!")


if preict_button:
    try:
        st.balloons()

        x_array = np.array(x).reshape(1, -1)
        logger.info(f"Input array shape: {x_array.shape}")

        predction = model.predict(x_array)[0]
        logger.info(f"Prediction successful: {predction}")

        st.write (f"price prediction is : {predction:,.2f}")
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        st.error(f"Error making prediction: {e}")
        st.write("Please check your input values and try again.")
else:
    st.write ("please use predict button after entering all the values")


# order of x 
#['number of bedrooms', 'number of bathrooms', 'living area',
 #      'condition of the house'