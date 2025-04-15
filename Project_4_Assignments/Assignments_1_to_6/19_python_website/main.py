from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Website", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ✅ Clean URL without any invisible characters
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_jcikwtux.json")
img_contact_form = Image.open("images/calculator.jpg")
img_lottie_animation = Image.open("images/cumputer_number_guesing.jpg")

st.subheader("Hi! Welcome to My First Streamlit Website :wave:")
st.title("I'm Programmer from Pakistan!")
st.write("This is my first website using Streamlit. I am excited to share it with you!")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("#")
        st.write(
            """
            I am a programmer with experience in various programming languages and technologies. I enjoy solving complex problems and building innovative solutions.
            """
        )
        st.write("[My Linkedin Account > ](https://www.linkedin.com/in/bilal-hussain-20799b251/)")
    with right_column:
        st_lottie(
            lottie_coding,
            height=300,
            key="coding",
        )

# projects 
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("#")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("CalCulator")
        st.write(
            """
            This is a simple calculator app that allows you to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.
            """
        )
        st.markdown("[Calculator..](https://github.com/Muhammad-Bilal-Hussain/Ramzan-Coding-2025/blob/main/simple_calculator/main.py)")
    with st.container():
        image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Computer number Guess game")
        st.write(
            """"
            This is a simple number guessing game where the computer generates a random number and the user has to guess it. The user receives feedback on whether their guess is too high or too low.
            """
        )
        st.markdown("[COmputer Number guess game..](https://github.com/Muhammad-Bilal-Hussain/SIR_ZIA-Assignment/blob/main/Project_4_Assignments/Assignments_1_to_6/project_2.py)")

with st.container():
    st.write("---")
    st.header("Get in Touch with Me!")
    st.write("#")

    contact_form = """
    <form action="https://formsubmit.co/bh1977955@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>

"""

left_column, right_column = st.columns((2))
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()