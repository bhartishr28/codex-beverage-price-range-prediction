# app.py

import streamlit as st
from predict import predict_price

st.set_page_config(page_title="Price Prediction", layout="wide")

st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>CodeX Beverage: Price Prediction</h1>",
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    age = st.number_input("Age", 10, 100, 25)
    income = st.selectbox("Income Level (In L)",
        ['<10L','10L - 15L','16L - 25L','26L - 35L','> 35L','Not Disclosed'])
    awareness = st.selectbox("Awareness of other brands",
        ['0 to 1','2 to 4','above 4'])
    packaging = st.selectbox("Packaging Preference",
        ['Simple','Premium','Eco-friendly'])

with col2:
    gender = st.selectbox("Gender", ['Male','Female'])
    consume_freq = st.selectbox("Consume Frequency(weekly)",
        ['0-2 times','3-4 times','5-7 times'])
    reason = st.selectbox("Reasons for choosing brands",
        ['Price','Quality','Availability','Brand Reputation'])
    health = st.selectbox("Health Concerns",
                          ['Low (Not very concerned)', 'Medium (Moderately health-conscious)',
                           'High (Very health-conscious)'])

with col3:
    zone = st.selectbox("Zone", ['Metro','Urban','Semi-Urban','Rural'])
    brand = st.selectbox("Current Brand",
        ['Established','Newcomer'])
    flavor = st.selectbox("Flavor Preference",
        ['Traditional','Exotic'])
    situation = st.selectbox("Typical Consumption Situations",
                             ['Active (eg. Sports, gym)', 'Casual (eg. At home)', 'Social (eg. Parties)'])

with col4:
    occupation = st.selectbox("Occupation",
        ['Student','Working Professional','Entrepreneur','Retired'])
    size = st.selectbox("Preferable Consumption Size",
        ['Small (250 ml)','Medium (500 ml)','Large (1 L)'])
    purchase = st.selectbox("Purchase Channel",
        ['Online','Retail Store'])



# -------- BUTTON -------- #
if st.button("Calculate Price Range"):

    user_input = {
        "age": age,
        "income_levels": income,
        "health_concerns": health,
        "consume_frequency(weekly)": consume_freq,
        "preferable_consumption_size": size,
        "gender": gender,
        "zone": zone,
        "occupation": occupation,
        "current_brand": brand,
        "awareness_of_other_brands": awareness,
        "reasons_for_choosing_brands": reason,
        "flavor_preference": flavor,
        "purchase_channel": purchase,
        "packaging_preference": packaging,
        "typical_consumption_situations": situation
    }

    try:
        result = predict_price(user_input)
        st.success(f"Predicted Price Range: {result}")

    except Exception as e:
        st.error(f"Error: {e}")

