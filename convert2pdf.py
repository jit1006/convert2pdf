from PIL import Image
import streamlit as st
import os

filename = st.file_uploader("Choose a file", accept_multiple_files=False , key = None ) 
if filename is not None:
        image = Image.open(filename)
else:
        
        image = Image.open("output.png")
          
st.image(image, caption='UPLOADED FILE ! ')

if image.mode == "RGBA":
        image = image.convert("RGB")

image = image.save("output.pdf") 

with open("output.pdf", "rb") as file:
        btn = st.download_button(
                label="Download pdf file !",
                data=file,
                file_name="output.pdf",
                mime="image/pdf"
                )
