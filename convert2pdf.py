from PIL import Image
import streamlit as st
import os

filename = st.file_uploader("Choose a file")
if filename is not None:
     dataframe = pd.read_csv(filename)
     st.write(dataframe)
     
image = Image.open(filename)
st.image(image, caption='image file')

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
