import streamlit as st
from app import debug_access_token, refresh_long_lived_access_token, exchange_token
from datetime import datetime, date
import time


st.title("Facebook Token Tool")
st.subheader("Debug or Exchange Facebook Access Tokens")
st.markdown('---')


# 1. Debug token: input access token, display token debug details
if st.checkbox("Debug token"):
    st.subheader("Debug access token")
    access_token = st.text_input("Access token")

    if st.button("Debug"):
        result = access_token.title()
        response = debug_access_token(access_token)
        data_access_expires_at = datetime.fromtimestamp(response['data']['data_access_expires_at'])

        st.subheader("Data result:")
        st.write("Data access expires at:", data_access_expires_at)
        
        st.write(response)

        
            

#2. Exchange initial token: inputs client_id, client_secret, access_token and debug, display new token and debug
if st.checkbox("Exchange access token"):
    st.subheader("Exchange access token")
    st.markdown('_App ID and App Secret can be found in the Basic Settings in your Facebook App Dashboard_')        
    client_id = st.text_input("App ID")
    client_secret = st.text_input("App Secret")
    access_t = st.text_input("Access Token")

    if st.button("Exchange"):

        response = exchange_token(client_id, client_secret, access_t)
        st.subheader("Data result:")
        st.write(response)

st.markdown('_Please note that no data is retained by this app_')        
st.markdown("> [![View Source on GitHub](https://assets.website-files.com/5eb1d49f3ed8c28a5a54769f/5eb7085ea11928da1d01a2d7_Github%20Icon.svg)](https://github.com/beepbeeptechnology/exchange-facebook-tokens) View Source on GitHub ([beepbeep.technology](https://beepbeep.technology))")


