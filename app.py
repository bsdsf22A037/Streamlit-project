# Importing necessary libraries and modules
import streamlit as st
from introduction import introduction
from eda import EDA
from preprocessing import data_preprocessing
from ml_model import ml
from conclusion_and_insights import conclusion_and_insights

# Configure the Streamlit page
st.set_page_config(
    page_title="Obesity level model project",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# App Title
st.title("Obesity level  Project Dashboard")
st.write("Welcome to Muhammad Farhan's project on obesity level dataset in which their are interactive dashboard for exploring the project, performing EDA, building models, and deriving insights.")

# Define sections and map them to functions
sections = {
    "Introduction": introduction,
    "EDA (Exploratory Data Analysis)": EDA,
    "Data Preprocessing": data_preprocessing,
    "Model": ml,
    "Conclusion and Insights": conclusion_and_insights,
}

# Sidebar for navigation
st.sidebar.title("Navigation")
st.sidebar.write("Use the sidebar to navigate through the sections.")
selected_section = st.sidebar.radio("Go to", list(sections.keys()))

# Display the selected section
st.markdown("---")  # Add a horizontal line for better UI separation
sections[selected_section]()
