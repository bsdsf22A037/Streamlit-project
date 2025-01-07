# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
def EDA():
    # Load the dataset
    data = pd.read_csv('project/sampled_dataset.csv')

    # Streamlit App
    st.title('Data Analysis and Visualization')

    # 1. Summary Statistics
    st.header('Summary Statistics')
    summary_stats = data.describe(include='all')
    st.write(summary_stats)

    # 2. Visualizations
    # Histogram of Weight
    st.header('Distribution of Weight')
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.hist(data['Weight'], bins=30, color='blue', alpha=0.7)
    ax1.set_title('Distribution of Weight')
    ax1.set_xlabel('Weight')
    ax1.set_ylabel('Frequency')
    st.pyplot(fig1)

    # Boxplot of Height
    st.header('Boxplot of Height')
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=data, x='Height', color='orange', ax=ax2)
    ax2.set_title('Boxplot of Height')
    st.pyplot(fig2)

    # Correlation Matrix Heatmap
    st.header('Correlation Matrix')
    numeric_data = data.select_dtypes(include=['float64', 'int64'])  # Select only numeric columns
    correlation_matrix = numeric_data.corr()
    fig3, ax3 = plt.subplots(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax3)
    ax3.set_title('Correlation Matrix')
    st.pyplot(fig3)

    # Unique Value Counts (Bar Plot for Categorical Features)
    st.header('Unique Value Counts by Feature')
    categorical_columns = data.select_dtypes(include=['object']).columns
    unique_value_counts = data[categorical_columns].nunique()
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    unique_value_counts.sort_values(ascending=False).plot(kind='bar', color='purple', ax=ax4)
    ax4.set_title('Unique Value Counts by Feature')
    ax4.set_ylabel('Count')
    ax4.set_xlabel('Features')
    st.pyplot(fig4)

    # Data Types (Pie Chart)
    st.header('Data Types Distribution')
    data_types_counts = data.dtypes.value_counts()
    fig5, ax5 = plt.subplots(figsize=(8, 8))
    data_types_counts.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightblue', 'pink'], startangle=90, ax=ax5)
    ax5.set_title('Data Types Distribution')
    st.pyplot(fig5)

    # Outlier Detection (Boxplot for Multiple Numeric Columns)
    st.header('Outlier Detection Across Numeric Features')
    fig6, ax6 = plt.subplots(figsize=(12, 8))
    sns.boxplot(data=numeric_data, orient='h', palette='Set2', ax=ax6)
    ax6.set_title('Outlier Detection Across Numeric Features')
    st.pyplot(fig6)
