# Import necessary libraries
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
def ml():
# Streamlit app
    st.title("ML Model for Weight Classification")

    # File uploader
    uploaded_file = st.file_uploader("Upload your raw CSV file", type=["csv"])

    if uploaded_file is not None:
        # Load the dataset
        data = pd.read_csv(uploaded_file)
        st.write("Dataset Preview:")
        st.write(data.head())

        # Preprocessing
        st.write("Preprocessing the data...")
        data.dropna(inplace=True)  # Drop missing values

        # Encode categorical variables using LabelEncoder
        label_encoders = {}
        for column in ['Gender', 'family_history_with_overweight', 'FAVC', 'CAEC', 'SMOKE', 'SCC', 'CALC', 'MTRANS']:
            if column in data.columns:
                le = LabelEncoder()
                data[column] = le.fit_transform(data[column])
                label_encoders[column] = le

        # Encode the target variable
        target_column = '0be1dad'
        if target_column in data.columns:
            le_target = LabelEncoder()
            data[target_column] = le_target.fit_transform(data[target_column])
            label_encoders[target_column] = le_target
        else:
            st.error("The target column '0be1dad' is not found in the dataset. Please check your file.")
            st.stop()

        # Separate features and target variable
        X = data.drop(['id', target_column], axis=1, errors='ignore')
        y = data[target_column]

        # Standardize numerical features
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a Random Forest Classifier
        st.write("Training the model...")
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Evaluate the model
        accuracy = accuracy_score(y_test, y_pred)
        st.write("Model Accuracy:", accuracy)
        st.write("Classification Report:")
        st.text(classification_report(y_test, y_pred))

        # Save the trained model and encoders for future use
        joblib.dump(model, 'best_ml_model.pkl')
        joblib.dump(scaler, 'scaler.pkl')
        for column, le in label_encoders.items():
            joblib.dump(le, f'label_encoder_{column}.pkl')

        st.write("Model and encoders saved successfully.")