import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Load model, scaler, dan feature names
model = joblib.load("model_dropout.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("feature_names.pkl")  # fitur saat training

st.title("Prediksi Dropout Mahasiswa - Jaya Jaya Institut")
st.markdown("Silakan isi data berikut:")

# Input minimal dari user
marital_status = st.selectbox("Status Pernikahan", [1, 2, 3, 4, 5, 6])
application_mode = st.selectbox("Metode Aplikasi", [1, 2, 5, 7, 10, 15, 16, 17, 18, 26, 27, 39, 42, 43, 44, 51, 53, 57])
prev_qualification_grade = st.slider("Nilai Kualifikasi Sebelumnya", 0.0, 200.0, 120.0)
admission_grade = st.slider("Nilai Masuk", 0.0, 200.0, 120.0)
age_enroll = st.slider("Usia Saat Mendaftar", 16, 60, 19)
debtor = st.selectbox("Status Pembayaran (Debtor)?", [0, 1])
tuition_up_to_date = st.selectbox("Pembayaran Terkini Up-to-date?", [0, 1])
gender = st.selectbox("Jenis Kelamin", [0, 1])
semester1_grade = st.slider("Rata-rata Nilai Semester 1", 0.0, 20.0, 10.0)
sem1_enrolled = st.slider("Mata Kuliah Diambil (Semester 1)", 0, 10, 6)
sem1_approved = st.slider("Mata Kuliah Lulus (Semester 1)", 0, 10, 6)
sem1_evaluations = st.slider("Jumlah Evaluasi (Semester 1)", 0, 10, 6)
sem2_grade = st.slider("Nilai Rata-rata Semester 2", 0.0, 20.0, 16.0)

# Dataframe kosong dengan semua fitur
input_data = pd.DataFrame(columns=feature_names)
input_data.loc[0] = 0 

# Mengisi fitur utama dengan input user
input_data.loc[0, 'Marital_status'] = marital_status
input_data.loc[0, 'Application_mode'] = application_mode
input_data.loc[0, 'Previous_qualification_grade'] = prev_qualification_grade
input_data.loc[0, 'Admission_grade'] = admission_grade
input_data.loc[0, 'Age_at_enrollment'] = age_enroll
input_data.loc[0, 'Debtor'] = debtor
input_data.loc[0, 'Tuition_fees_up_to_date'] = tuition_up_to_date
input_data.loc[0, 'Gender'] = gender
input_data.loc[0, 'Curricular_units_1st_sem_grade'] = semester1_grade
input_data.loc[0, 'Curricular_units_1st_sem_enrolled'] = sem1_enrolled
input_data.loc[0, 'Curricular_units_1st_sem_approved'] = sem1_approved
input_data.loc[0, 'Curricular_units_1st_sem_evaluations'] = sem1_evaluations
input_data.loc[0, 'Curricular_units_2nd_sem_grade'] = sem2_grade
input_data.loc[0, 'Application_order'] = 1
input_data.loc[0, 'Displaced'] = 0
input_data.loc[0, 'Educational_special_needs'] = 0
input_data.loc[0, 'Scholarship_holder'] = 0
input_data.loc[0, 'Nacionality'] = 1
input_data.loc[0, 'Mothers_qualification'] = 1
input_data.loc[0, 'Fathers_qualification'] = 1
input_data.loc[0, 'Mothers_occupation'] = 4
input_data.loc[0, 'Fathers_occupation'] = 4
input_data.loc[0, 'Unemployment_rate'] = 7.0
input_data.loc[0, 'Inflation_rate'] = 1.2
input_data.loc[0, 'GDP'] = 2.3

# Standardisasi
X_scaled = scaler.transform(input_data)

# Prediksi
if st.button("Prediksi Status Mahasiswa"):
    prediction = model.predict(X_scaled)[0]
    label_mapping = {0: "Enrolled", 1: "Dropout", 2: "Graduate"}
    st.success(f"Hasil prediksi: **{label_mapping[prediction]}**")