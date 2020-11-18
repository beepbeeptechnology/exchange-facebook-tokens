import streamlit as st
from app import debug_access_token, refresh_long_lived_access_token, exchange_token
import time


st.title("TripScout App")
st.subheader("Exchange Facebook Token")

activity =  ["Debug token", "Exchange initial token", "Exchange long-lived token"]

choice = st.selectbox("Select activity", activity)

# 1. Debug token: input access token, display token debug details
if choice == "Debug token":
    st.subheader("Debug token")
    access_token = st.text_input("Enter debug token")

    if st.button("Submit"):
        result = access_token.title()

        try:
            response = debug_access_token(access_token)
            st.subheader("Data result:")
            st.write(response)
        except Exception as e:
            print(e)
            

#2. Exchange initial token: inputs client_id, client_secret, access_token and debug, display new token and debug
if choice == "Exchange initial token":
    st.subheader("Exchange initial token")

    client_id = st.text_input("Client ID")
    client_secret = st.text_input("Client secret")
    access_t = st.text_input("Insert your access token")

    if st.button("Send to exchange"):

        try:
            response = exchange_token(client_id, client_secret, access_t)
            st.subheader("Data result:")
            st.write(response)
        except Exception as e:
            print(e)

# 3. Exchange long-lived token: inputs access_token and debug, display new token and debug
if choice == "Exchange long-lived token":
    st.subheader("Exchange long-lived token")

    long_access = st.text_input("Insert token")

    if st.button("Exchange to Long Live Token"):

        try:
            response = refresh_long_lived_access_token(long_access)
            st.subheader("Data result:")
            st.write(response)
        except Exception as e:
            print(e)


