import streamlit as st
import pickle

st.title('Microclimate Forecast')
user_input = st.number_input('Day Number',
                             min_value=1, max_value=100, value=10)

@st.cache
def load_model():
    temp_model_file = open('TC_forecast.pkl', 'rb')
    hum_model_file = open('HUM_forecast.pkl', 'rb')

    temp_model = pickle.load(temp_model_file)
    hum_model = pickle.load(hum_model_file)
    return (temp_model, hum_model)

@st.cache
def predict(user_input=user_input):
    temp_model, hum_model = load_model()
    temp = temp_model.predict([[user_input]])
    hum = hum_model.predict([[user_input]])
    return (temp, hum)

temp, hum = predict(user_input)
st.subheader("Predictions")
col1, col2 = st.columns(2)
col1.metric("Temperature (Deg Cel.)", round(temp[0][0], 1))
col2.metric("Humidity (%)", round(hum[0][0], 1))
