import streamlit as st

# Title of the app
st.title("BMI Calculator")

# Get user input for height and weight
height = st.number_input("Enter your height (in meters):", min_value=0.1, max_value=8.0, value=1.75, step=0.01)
weight = st.number_input("Enter your weight (in kilograms):", min_value=1, max_value=500, value=70, step=1)

# Calculate BMI
if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    # Show the BMI category based on the result
    if bmi < 18.5:
        st.write("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.write("You are overweight.")
    else:
        st.write("You are obese.")
else:
    st.write("Please enter valid weight and height.")
