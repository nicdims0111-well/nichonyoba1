import streamlit as st

st.title("This is a title")
st.title(":blue[PENENTUAN BILANGAN PANGKAT] :sunglasses:")


number = st.number_input("Insert a number")
st.write("The current number is ", number)
