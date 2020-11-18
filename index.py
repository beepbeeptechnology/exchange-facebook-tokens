import streamlit as st


st.title("TripScout App")
st.subheader("Exchange Facebook Token")

activity =  ["Debug token", "Exchange initial token", "Exchange long-lived token"]

choice = st.selectbox("Select activity", activity)

# 1. Debug token: input access token, display token debug details
if choice == "Debug token":
    st.subheader("Debug token")
    debug_token = st.text_input("Enter debug token")
    if st.button("Submit"):
        result = debug_token.title()
        st.success("Token have been received")


#2. Exchange initial token: inputs client_id, client_secret, access_token and debug, display new token and debug
if choice == "Exchange initial token":
    st.subheader("Exchange initial token")

    client_id = st.text_input("Client ID")
    client_secret = st.text_input("Client secret")
    access_t = st.text_input("Insert your access token")
    debug_t = st.text_input("Insert your debug token") 

    if st.button("Send to exchange"):
        st.success("This data have been sent")
        st.write("Client id:",client_id)
        st.write("Secret id:",client_secret)
        st.write("Access Token:",access_t)
        st.write("Debug token:",debug_t)


# 3. Exchange long-lived token: inputs access_token and debug, display new token and debug
if choice == "Exchange long-lived token":
    st.subheader("Exchange long-lived token")

    long_access = st.text_input("Insert token")
    long_debug = st.text_input("Insert debug token") 

    if st.button("Exchange to Long Live Token"):
        st.success("This data have been sent")
        st.write("Access Token:",long_access)
        st.write("Debug token:",long_debug)