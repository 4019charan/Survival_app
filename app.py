import streamlit as st
import pickle
import numpy as np

# Load the trained model and scaler
with open('model.pickle', 'rb') as f:
    predictor = pickle.load(f)

with open('model_scaler.pickle', 'rb') as f:
    scaler = pickle.load(f)

# Function to predict survival
def predict_survival(pclass, sex, age, sibsp, parch, fare):
    data = np.array([[pclass, sex, age, sibsp, parch, fare]])
    scaled_data = scaler.transform(data)
    prediction = predictor.predict(scaled_data)[0]
    return prediction

# Streamlit app layout
def main():
    st.title("Titanic Survival Prediction")
    st.markdown("Enter the passenger details to predict survival")

    pclass = st.selectbox("Pclass", [1, 2, 3])
    sex = st.selectbox("Sex", ["Male", "Female"])
    age = st.number_input("Age", min_value=0, max_value=100, value=30)
    sibsp = st.number_input("SibSp", min_value=0, max_value=10, value=0)
    parch = st.number_input("Parch", min_value=0, max_value=10, value=0)
    fare = st.number_input("Fare", min_value=0.0, value=50.0)

    if st.button("Predict"):
        sex_num = 1 if sex == "Male" else 0
        prediction = predict_survival(pclass, sex_num, age, sibsp, parch, fare)

        if prediction == 1:
            st.success("Congrats! You are most likely to survive the crash")
        else:
            st.warning("I'm sorry, you didn't make it this time, but since my model accuracy is only 87%, "
                       "there's a high likelihood that you might survive. "
                       "Note: I've made this for fun. Please don't get offended.")

if __name__ == "__main__":
    main()
