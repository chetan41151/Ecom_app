import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns



def main():
    st.title("This is a app for ecom i am creating")
    st.sidebar.title("you can upload your file here")

    upload_file = st.sidebar.file_uploader("Upload your file here", type=["csv", "xlsx"])

    if upload_file is not None:
        try:
            if upload_file.name.endswith(".csv"):
                data = pd.read_csv(upload_file)
            else:
                data = pd.read_excel(upload_file)
            st.sidebar.success("File uploaded successfully")

            st.subheader("i am going to show you a data details")
            st.dataframe(data.head())

            st.subheader("lets see some more detail in the data")
            st.write("shape of the data", data.shape)
            st.write("columns in the data", data.columns)
            st.write("missing value into column", data.isnull().sum())

            st.subheader("i will show you the bit os stats")
            st.write(data.describe())


        except Exception as e:
            print(e)



if __name__ == "__main__":
    main()