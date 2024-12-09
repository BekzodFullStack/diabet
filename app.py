import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

# 1. Modelni yuklash
with open("small_random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)

# 2. Streamlit sarlavhasi
st.title("Diabet Xavfi Bashorat Dasturi")
st.write("Ushbu dastur sizning kiritgan ma'lumotlaringiz asosida diabet xavfini bashorat qiladi.")

# 3. Foydalanuvchi ma'lumotlarini kiritish
st.header("Ma'lumotlaringizni kiriting:")
age = st.number_input("Yoshingiz (18-90 oralig'ida):", min_value=18, max_value=90, value=30, step=1)
bmi = st.number_input("Tana massasi indeksi (BMI):", min_value=10.0, max_value=150.0, value=25.0, step=0.1)
blood_pressure = st.number_input("Qon bosimi (mmHg):", min_value=70, max_value=200, value=120, step=1)
cholesterol = st.number_input("Xolesterin darajasi (mg/dL):", min_value=100, max_value=400, value=200, step=1)
smoking = st.selectbox("Chekasizmi?", options=["Yo'q", "Ha"])
physical_activity = st.selectbox("Jismoniy faollik darajasi", options=["Past", "Yuqori"])
family_history = st.selectbox("Oilaviy anamnezda diabet mavjudmi?", options=["Yo'q", "Ha"])

# 4. Ma'lumotlarni tayyorlash
smoking = 1 if smoking == "Ha" else 0
physical_activity = 1 if physical_activity == "Yuqori" else 0
family_history = 1 if family_history == "Ha" else 0

input_data = pd.DataFrame({
    "Age": [age],
    "BMI": [bmi],
    "BloodPressure": [blood_pressure],
    "Cholesterol": [cholesterol],
    "Smoking": [smoking],
    "PhysicalActivity": [physical_activity],
    "FamilyHistory": [family_history]
})

# 5. Bashorat qilish
if st.button("Bashorat qilish"):
    prediction = model.predict(input_data)
    risk = "Yuqori xavf" if prediction[0] == 1 else "Past xavf"
    st.subheader(f"Bashorat natijasi: {risk}")
