from PIL import Image
import streamlit as st
import os

filename = st.file_uploader("Choose a file")
image = Image.open(filename)

if image.mode == "RGBA":
     image = image.convert("RGB")

output ='output.pdf'
image.save(output) 
