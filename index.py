import streamlit as st
from app import debug_access_token, refresh_long_lived_access_token, exchange_token
from datetime import datetime, date
import time


st.title("TripScout App")
st.subheader("Exchange Facebook Token")


# 1. Debug token: input access token, display token debug details
if st.checkbox("Debug token"):
    st.subheader("Check the debug token")
    access_token = st.text_input("Enter debug token")

    if st.button("Submit"):
        result = access_token.title()
        response = debug_access_token(access_token)
        data_access_expires_at = datetime.fromtimestamp(response['data']['data_access_expires_at'])

        st.subheader("Data result:")
        st.write("Data access expires at:", data_access_expires_at)
        
        st.write(response)

        
            

#2. Exchange initial token: inputs client_id, client_secret, access_token and debug, display new token and debug
if st.checkbox("Exchange initial token"):
    st.subheader("Exchange initial token")

    client_id = st.text_input("Client ID")
    client_secret = st.text_input("Client secret")
    access_t = st.text_input("Insert your access token")

    if st.button("Send to exchange"):

        response = exchange_token(client_id, client_secret, access_t)
        st.subheader("Data result:")
        st.write(response)

