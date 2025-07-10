import streamlit as st
import pandas as pd
import subprocess
import os
from datetime import datetime

st.set_page_config(page_title="Smart Attendance System", page_icon="✅")

# 1️⃣ Simple Login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":  # CHANGE THIS!
            st.session_state.logged_in = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")
    st.stop()

st.title("🎓 Smart Attendance System")

# 2️⃣ Register new face (calls capture_faces.py)
st.subheader("📸 Register New Face")
new_name = st.text_input("Enter name")
if st.button("Capture Faces"):
    if new_name:
        command = f"python capture_faces.py"
        os.environ["NEW_NAME"] = new_name
        st.info(f"Running: {command}")
        subprocess.run(["python", "capture_faces.py"])
        st.success("Capture done! Now run training.")
    else:
        st.warning("Enter a name first!")

# 3️⃣ Train model
if st.button("🔁 Train Model"):
    subprocess.run(["python", "train_model.py"])
    st.success("Training complete!")

# 4️⃣ Show live attendance table with auto-refresh
st.subheader("✅ Attendance Records")
if os.path.exists("attendance.csv"):
    df = pd.read_csv("attendance.csv", names=["Name", "Time"])
    st.dataframe(df)
else:
    st.info("No attendance records yet.")

# 5️⃣ Download attendance PDF
if st.button("📥 Download Attendance (CSV)"):
    if os.path.exists("attendance.csv"):
        with open("attendance.csv", "rb") as f:
            st.download_button("Download", f, "attendance.csv", "text/csv")
    else:
        st.warning("No attendance.csv found.")

# 6️⃣ Run recognition
if st.button("🎥 Start Recognition"):
    subprocess.run(["python", "recognize_faces.py"])
