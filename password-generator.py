import streamlit as st
import re 

#app styling 
st.set_page_config(page_title="Password Strength Meter By Javeria Arshad Qureshi", page_icon="🔑", layout="centered")

#using custom css to style the app
st.markdown("""
<style>
    .main{text-align: start;}
    .stTextInput {width: 100% !important; margin: auto;}
    .stButton button {width: 60%; background-color: white; color: black; font-size: 18px;  }
    .stButton button:hover { background-color:black; color:white; }
</style>    
""",unsafe_allow_html=True)

#page details
st.title("🔐 Password Strength Meter ⏱️ ")
st.write("Enter your password below to check it strength 💪🏻.")

#make function on which we can check password strength
def password_strength_checker(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increase score by 1
    else:
        feedback.append("👎🏻Password should be **at least 8 character long**")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]",password):
        score += 1 #increase score by 1
    else:
        feedback.append("👎🏻Password must contain **at least one Uppercase(A-Z) and Lowercase(a-z)**")

    if re.search(r"\d", password):
        score += 1 #increase score by 1
    else:
        feedback.append("👎🏻Password must contain **at least one number (0-9)**")

    if re.search(r"[!@#$%^&*]", password):
        score += 1 #increase score by 1
    else:
        feedback.append("👎🏻Password must contain **at least one special character(!@#$%^&*)**")    


    #display the result 
    if score == 4:
        st.success("✔️ **Strong Password** - Your is safe and secure.")
    elif score == 3 :
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more feature")
    else:
        st.error("❌ **Weak Password** - Follow the given sugguestion below to strength it.")     

#Feedback
    if feedback:
        with st.expander("🔍 ** Improve Your Password** "):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔒")      

#button
if st.button("Check Password Strength"):
    if password:
        password_strength_checker(password)
    else:
        st.write("⚠️ Please enter password first")                    


