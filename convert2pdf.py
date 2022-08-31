from PIL import Image
import streamlit as st
import os


st.title("Image to Pdf file Converter ") 
filename = st.sidebar.file_uploader("Load your image File Here")
if filename is not None:
        image = Image.open(filename)
else:
        
        image = Image.open("output.png")
          
st.image(image, caption='UPLOADED FILE ! ')

if image.mode == "RGBA":
        image = image.convert("RGB")

image = image.save("output.pdf") 

with open("output.pdf", "rb") as file:
        st.title("Converted File Here -> ")
        btn = st.download_button(
                label="Download pdf file !",
                data=file,
                file_name="output.pdf",
                mime="image/pdf"
                )
