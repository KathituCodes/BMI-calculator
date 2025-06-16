import streamlit as st

st.title("BMI Calculator")

# Step 1: Get user input
weight = st.number_input("Enter your weight in Kilograms:", min_value=0.0, step=0.1)
height_cm = st.number_input("Enter your height in centimeters:", min_value=0.0, step=0.1)

# Step 2: Calculate BMI
if weight > 0 and height_cm > 0:
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    # Step 3: Determine BMI category
    if bmi <= 18.5:
        category = "Underweight - Consult a doctor or eat more."
    elif 18.5 <= bmi < 25:
        category = "Normal weight - You're healthy, keep it up!"
    elif 25 <= bmi < 29.9:
        category = "Overweight - Consider exercising to avoid health issues."
    else:
        category = "Obese - Consult a nutritionist for better lifestyle choices."

    # Step 4: Display results
    st.write(f"**Your BMI is: {bmi:.2f}**")
    st.write(f"**Category: {category}**")
else:
    st.write("Please enter valid weight and height values.")