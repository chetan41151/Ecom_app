import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns



def main():
    st.title("This is a app for ecom i am creating")
    st.sidebar.title("you can upload your file here")

pload_file = st.sidebar.file_uploader("Upload Excel file", type=['xlsx'])

if upload_file is not None:
    try:
        # Read the uploaded Excel file
        data = pd.read_excel(upload_file)

        # Display success message
        st.sidebar.success("File uploaded successfully")

        # Display the data details
        st.subheader("Data Details")
        st.dataframe(data.head())  # Display first 5 rows

        st.subheader("Data Shape")
        st.write("Shape of the data:", data.shape)

        st.subheader("Columns in the Data")
        st.write("Columns:", data.columns)

        st.subheader("Missing Values")
        st.write("Missing values per column:", data.isnull().sum())

        st.subheader("Data Statistics")
        st.write(data.describe())

    except Exception as e:
        # Handle any errors while reading or displaying data
        st.error(f"Error reading the file: {e}")
else:
    st.sidebar.warning("Please upload an Excel file.")


if __name__ == "__main__":
    main()
