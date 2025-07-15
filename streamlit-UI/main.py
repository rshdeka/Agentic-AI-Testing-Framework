import streamlit as st

USERNAME = "rajashrideka04@gmail.com"
PASSWORD = "RDeka@123"

st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# Initialize session state for authentication
if "authenticated" not in st.session_state:
   st.session_state.authenticated = False

# Login Form
st.title("🔐 Login Page")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Login button
if st.button("Login"):
   if username == USERNAME and password == PASSWORD:
       st.session_state.authenticated = True
       st.success("Login successful! Navigate to the Heart Disease Predictor from the sidebar.")
   else:
       st.error("Invalid credentials")

# Block sidebar access to app page until login
if not st.session_state.authenticated:
   st.sidebar.warning("Please log in to access the app.")
else:
   st.sidebar.success("Go to: Heart Disease Predictor 👉")