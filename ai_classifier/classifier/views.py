from django.shortcuts import render
from .forms import ImageUploadForm
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load model once globally
model = tf.keras.applications.MobileNetV2(weights='imagenet')


def predict_image(request):
    prediction = None

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img_file = form.cleaned_data['image']

            # Load and preprocess image
            img = Image.open(img_file).resize((224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)

            # Predict
            preds = model.predict(img_array)
            prediction = decode_predictions(preds, top=1)[0][0][1]  # class name

    else:
        form = ImageUploadForm()

    return render(request, 'home.html', {'form': form, 'prediction': prediction})
