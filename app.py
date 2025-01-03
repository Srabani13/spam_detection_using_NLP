import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="SpamSniffer", page_icon="🐶", layout="centered")

# Custom CSS for UI styling
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #FFFAF0; /* Light beige background */
    }
    .sidebar .sidebar-content {
        background: #1f4e78;
        color: white;
    }
    .stButton>button {
        color: white;
        background-color: #007BFF;
        border-radius: 10px;
        padding: 10px 20px;
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

# Title and description
st.title("🐶 SpamSniffer")
st.write("Say goodbye to spam with our AI-powered slayer!.")

# Text input
user_input = st.text_input("Enter a message:", placeholder="Type your message here...")

# Buttons for prediction and clearing
col1, col2 = st.columns(2)
with col1:
    predict_btn = st.button("Predict")
with col2:
    clear_btn = st.button("Clear")

if clear_btn:
    st.experimental_rerun()

if predict_btn and user_input:
    with st.spinner("Analyzing the message..."):
        data = {"message": [user_input]}
        try:
            response = requests.post("http://127.0.0.1:5000/predict", json=data)
            if response.status_code == 200:
                result = response.json()["predictions"][0]
                if result == 1:
                    st.error("This message is predicted as **Spam**.")
                else:
                    st.success("This message is predicted as **Not Spam**.")
            else:
                st.error("An error occurred while predicting. Please try again.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
