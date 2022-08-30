from PIL import Image
import streamlit as st
import os

filename = st.file_uploader("Choose a file")
image = Image.open(filename)
st.image(image, caption='image file')

if image.mode == "RGBA":
     image = image.convert("RGB")

# output ='output.pdf'
image.save("output.png") 

with open("image.png", "rb") as file:
     btn = st.download_button(
             label="Download image",
             data=filename,
             file_name="output",
             mime="image/png"
           )
