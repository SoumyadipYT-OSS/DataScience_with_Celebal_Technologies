import streamlit as st
import pandas as pd
from ConversationalModel import ConversationalModel

# Function to load the dataset
def load_data(file):
    data = pd.read_csv(file)
    return data

# Streamlit UI
st.title("CSV Dataset Analyzer")

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = load_data(uploaded_file)
    st.write("Dataset Loaded Successfully!")
    
    # Display basic information about the dataset
    if st.checkbox("Show Dataset"):
        st.write(data)
    
    # Instantiate the conversational model
    model = ConversationalModel()
    
    # User input for querying dataset characteristics
    query = st.text_input("Enter your query (e.g., 'length', 'columns', 'summary')")

    if query:
        response = model.get_response(query)

        try:
            res = eval(response)
            st.write(res)
        except:
            st.write
