#Import Lybraries
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from script.data_pipeline import load_data
import pandas as pd

#load model
model = tf.keras.models.load_model("model/best_model.keras")

#load class name
dataset_path = r"D:\Major_project\dataset\data"
_, _, class_names = load_data(dataset_path)
st.title("Braille Character Recognition System")

uploaded_file = st.file_uploader(
    "Upload braille Image",
    type=["jpg","jpeg","png"],
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image.resize((50,50)),
        width=50,
        caption="uploaded Image",
        use_container_width=False
    )
    #preprocessing
    img = image.resize((28, 28))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    #prediction
    prediction = model.predict(img)

    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction) * 100
    top3 = np.argsort(-prediction)[0][:3]
    re_l = [class_names[i] for i in top3]
    re_c = [ prediction[0][i] for i in top3]
    result = {
        "predicted":re_l,
        "Confidence":re_c
    }
    result_table = pd.DataFrame(result)
    st.table(result_table,width='content', border=False)
  