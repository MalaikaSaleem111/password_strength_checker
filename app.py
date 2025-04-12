import random
import re
import string 
import streamlit as st

st.set_page_config(page_title="Password Strength Checker", layout="centered")

st.title("🔐Password Strength Checker")
st.write("Type a password to see how strong it is.")

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score +=1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score +=1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score+=1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        st.success("✅ **Strong Password!**")
    elif score == 3:
        st.info("⚠️ **Moderate Password**- Consider adding more security features.")
    else:
        st.error("❌ **Weak Password** - Improve it using the suggestions below.")

     # Visual Progress Bar
    st.progress(score / 4)
    
    # feedback
    if feedback:
        with st.expander("💡 Click here to see suggestions for improvement"):
           for tip in feedback:
            st.write(tip)
     
        
# Function to generate a random password

def generate_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+={}\[\]:;<>,.?/~"
    return "".join(random.choice(characters) for _ in range(12))

password = st.text_input("Enter Your Password:", type="password")
if password:
        check_password_strength(password)
else:
        st.warning("⚠️Please enter a password")

st.markdown("---")

# Password Generator Section
st.subheader("🔑 Generate a Strong Password")

if st.button("Generate Password"):
    generated_password = generate_password()
    st.success(f"**Generated Password:** `{generated_password}`")
