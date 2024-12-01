import tkinter as tk
from tkinter import messagebox
import pickle
import pandas as pd

def predict():
    try:
        # Mengambil input nilai dari user
        sepal_length = float(entry_sepal_length.get())
        sepal_width = float(entry_sepal_width.get())
        petal_length = float(entry_petal_length.get())
        petal_width = float(entry_petal_width.get())

        # Membuat array dari semua inputan
        input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

        # Memuat kembali model yang sudah dilatih
        import joblib
        model = joblib.load('iris_model.pkl')  # Sesuaikan nama file model Anda

        # Melakukan prediksi menggunakan model
        prediction = model.predict(input_data)

        # Menampilkan hasil prediksi
        species = prediction[0]
        messagebox.showinfo("Hasil Prediksi", f"Jenis bunga Iris adalah: {species}")

    except ValueError:
        messagebox.showerror("Error", "Masukkan nilai numerik yang valid untuk semua input!")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")