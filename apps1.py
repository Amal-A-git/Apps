import streamlit as st

# Title of the app
st.title("Basic Calculator App")

# User input for two numbers
number1 = st.number_input("Enter the first number", step=1.0)
number2 = st.number_input("Enter the second number", step=1.0)

# User selects the operation
operation = st.selectbox("Select an operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Perform the calculation based on the selected operation
if operation == "Addition":
    result = number1 + number2
elif operation == "Subtraction":
    result = number1 - number2
elif operation == "Multiplication":
    result = number1 * number2
elif operation == "Division":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error: Division by zero"

# Display the result
st.write("Result:", result)
