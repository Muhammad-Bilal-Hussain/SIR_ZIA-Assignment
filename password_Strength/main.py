import streamlit as st
import re

st.set_page_config(
    page_title="Password Strength Checker",page_icon="🔒",layout="centered")

st.title("🔒Password Strength Checker")
st.markdown(
    """This app checks the strength of your password based on various criteria. strength is rated as Weak, Medium, or Strong based on the following rules:
- **Weak**: Less than 8 characters or contains only letters or digits. 
- **Medium**: At least 8 characters, contains letters and digits, but no special characters.
- **Strong**: At least 8 characters, contains letters, digits, and special characters."""
    )

password = st.text_input("Enter your password:", type="password")

feedback = []
score = 0

if password:
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")

    # Check for letters
    if re.search(r'[a-zA-Z]', password) and re.search(r'[a-zA-Z]', password):
        score += 1
    else:
        feedback.append("❌Password should contain both upper and lower case character.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Password must contain at least one digit.")

    # Check for special characters
    if re.search(r'[@$!%*?&]', password):
        score += 1
    else:
        feedback.append("❌Password must contain at least one special character [@$!%*?&].")
    if score == 4:
        feedback.append("🤩Now your password is strong🎉")
    elif score == 3:
        feedback.append("🙄 your password is medium")
    else:
        feedback.append("😒 your password is weak")

    if feedback:
        st.markdown("### Feedback:")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please Enter your Password.")
