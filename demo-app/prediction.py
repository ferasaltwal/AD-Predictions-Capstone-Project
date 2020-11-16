import streamlit as st
import numpy as np
from skimage.transform import resize
from PIL import Image
import cv2



def prepare_img(mri_img):
    img_size = 150
    img_array = cv2.imread(mri_img, 1)
    new_array = cv2.resize(img_array, (img_size, img_size))
    return new_array.reshape(-1, img_size, img_size, 3)

@st.cache
def predict_input(classifier_model, input):
    input = prepare_img(input)
    prediction = classifier_model.predict(input)
    return prediction[0][0]
