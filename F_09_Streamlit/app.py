import streamlit as st
import pandas as pd

# for writing something
st.write("Hello world")

#for title
st.title("Hello Streamlit")

st.write("This is my first streamlit app")

# this one for header
st.header("Welcome to streamlit")

# this one for subheader
st.subheader("This is a subheader")

#this one for text
st.text("This is plain text")


## these for buttons, checkboxes and sliders

if st.button("Click Me!"):
    st.write("Button Clicked!")

agree=st.checkbox("I agre!e")
if agree:
    st.write("Your agree!")

level=st.slider("Select a Level : ", 1,10,5)
st.write(f"Selected level:{level}")

#this one is for uploading files
uploaded_file=st.file_uploader("Upload a File",type=["csv","txt"])
if uploaded_file is not None :
    df=pd.read_csv(uploaded_file)
    st.write(df.head())