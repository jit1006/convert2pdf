from PIL import Image
import streamlit as st
import os

filename = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)

image = Image.open(filename)

if image.mode == "RGBA":
     image = image.convert("RGB")

output ='output.pdf'
image.save(output) 
