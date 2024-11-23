from django.shortcuts import render
from .forms import PhotoUploadForm
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Muat model hanya sekali saat aplikasi dimulai
# model = load_model('path/to/model.h5')
model = load_model('./model_creation/mnist_model.h5')

def photo_upload(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Simpan file foto yang diunggah
            uploaded_photo = form.save()

            # Path ke file foto yang diunggah
            photo_path = uploaded_photo.photo.path

            # Proses foto dengan model Keras
            img = image.load_img(photo_path, target_size=(224, 224))  # Sesuaikan ukuran input model
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0  # Normalisasi jika diperlukan
            result = img_array
            # # Prediksi dengan model
            predictions = model.predict(img_array)
            result = np.argmax(predictions, axis=1)  # Sesuaikan dengan kebutuhan output model

            # Tampilkan hasil prediksi
            return render(request, 'tebak_angka/result.html', {'result': result})
    else:
        form = PhotoUploadForm()
    
    return render(request, 'tebak_angka/upload.html', {'form': form})
