import streamlit as st

st.title("This is a title")
st.title(":blue[PENENTUAN BILANGAN PANGKAT] :sunglasses:")


number = int(st.number_input("Insert a number", min_value=0, max_value=))
if number%2==1:
  st.write('bilangan', number, 'termasuk bilangan ganjil')
else:
  st.write('bilangan', number, 'termasuk bilangan genap')
