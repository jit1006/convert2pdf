from PIL import Image
import streamlit as st
import os

filename = st.file_uploader("Choose a file")
if filename is not None:
     # To read file as bytes:
     bytes_data = filename.getvalue()
     st.write(bytes_data)

image = Image.open(filename)
st.image(image, caption='Sunrise by the mountains')

if image.mode == "RGBA":
     image = image.convert("RGB")

output ='output.pdf'
# image.save(output) 

with open("output", "rb") as file:
     btn = st.download_button(
             label="Download image",
             data=file,
             file_name="output",
             mime="image/png"
           )
