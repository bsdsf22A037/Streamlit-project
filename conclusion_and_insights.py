import streamlit as st

def conclusion_and_insights():
    st.title("Conclusion and Insights")

    st.markdown("""
    ## **Project Summary**
    In this project, we analyzed the **Obesity Level Dataset** to uncover insights into the factors contributing to obesity. The dataset was carefully preprocessed to ensure data quality and compatibility for analysis. Key steps included:
    - Handling missing or inconsistent values.
    - Standardizing categorical and numerical data for better model performance.

    ---
    
    ## **Model Performance**
    A **Random Forest model** was implemented to predict obesity levels based on various health and lifestyle factors. Random Forest was chosen for its robustness and ability to handle complex, non-linear relationships. The model demonstrated:
    - **High Accuracy**: It effectively classified obesity levels across different categories.
    - **Feature Importance**: The model highlighted significant factors contributing to obesity, such as dietary habits, physical activity, and family history.

    ---
    
    ## **Key Insights**
    - **Dietary Habits**: Frequent consumption of high-calorie foods (e.g., fast food) was a strong predictor of higher obesity levels.
    - **Physical Activity**: Individuals with regular physical activity were less likely to be categorized as obese.
    - **Water Intake**: Adequate hydration showed a correlation with healthier weight levels.
    - **Family History**: A family history of overweight or obesity was a significant contributing factor.
    
    ---
    
    ## **Actionable Recommendations**
    - Encourage balanced dietary practices with lower calorie intake and healthier food options.
    - Promote regular physical activity as a key preventive measure against obesity.
    - Raise awareness about the importance of hydration for overall health.
    - Implement targeted interventions for individuals with a family history of obesity.

    ---
    
    Thank you for exploring the **Obesity Level Dataset**! These findings can help guide better health practices and inform future research on obesity prevention.
    """)
