import streamlit as st
import requests

def main():
    st.set_page_config(page_title="SpamSniffer", page_icon="🐶")
    st.markdown(
        """
        <style>
        .reportview-container {
            background-color: #FFDAB9; /* Peach color */
        }
        .sidebar .sidebar-content {
            background: #1f4e78;
            color: white;
        }
        .stButton>button {
            color: white;
            background-color: #007BFF;
            border-radius: 10px;
            box-shadow: 2px 2px 5px grey;
        }
        .stTextInput>div>div>input {
            border: 2px solid #007BFF;
            border-radius: 5px;
            padding: 10px;
            box-shadow: 2px 2px 5px grey;
        }
        .stAlert {
            background-color: #e0f7fa;
            border-left: 6px solid #007BFF;
            box-shadow: 2px 2px 5px grey;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("🐶 SpamSniffer")
    
    user_input = st.text_input("Enter a message:")

    if st.button("Predict"):
        data = {"message": [user_input]}
        response = requests.post("http://127.0.0.1:5000/predict", json=data)

        if response.status_code == 200:
            result = response.json()
            st.success(f"The prediction is: {result['prediction']}")
        else:
            st.error("An error occurred")

if __name__ == "__main__":
    main()
