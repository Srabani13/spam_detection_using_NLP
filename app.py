import streamlit as st
import pandas as pd
import requests


def main():
    st.title("Streamlit App")
    
    user_input = st.text_input("Enter a message:")

    if st.button("Predict"):
        data = {"message": [user_input]}
        response = requests.post("http://localhost:5000/predict", json=data)


        if response.status_code == 200:
           result = response.text
           st.success(f"The prediction is: {result}")
        else:
            result = "An error occurred"

if __name__ == "__main__":
    main()