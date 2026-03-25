import streamlit as st

st.title("User Registration Form")

# Create a form
with st.form("registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    age = st.number_input("Age", min_value=1, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    
    submit = st.form_submit_button("Register")

# After submission
if submit:
    if name and email and password:
        st.success("Registration Successful 🎉")
        st.write("### Entered Details:")
        st.write("Name:", name)
        st.write("Email:", email)
        st.write("Age:", age)
        st.write("Gender:", gender)
    else:
        st.error("Please fill all required fields ❗")