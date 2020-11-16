import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow import keras
from tensorflow.keras.models import load_model
import cv2
from skimage.transform import resize


st.title("Alzheimer's Disease Classifier")
st.header("Classifies brain MRI images as AD or normal")
st.header("")

uploaded_img = st.file_uploader('Choose an MRI image', type=['png', 'jpg', 'jpeg'])
if uploaded_img is not None:
    my_image = Image.open(uploaded_img)
    img_array = np.asarray(my_image)
    new_array = resize(img_array, (150, 150, 3))
    new_array = new_array.reshape(-1, 150, 150, 3)
    st.image(new_array, caption='Uploaded MRI image.', use_column_width=True)
    # new_array = (new_array.reshape(-1, 150, 150, 3))


#loading the model
AD_classifier = load_model('/Users/ferasaltwal/Documents/DSI/New-Capstone/saved-models/Kaggle-jupyter.h5')

#write a function to classify the input image
# def predict_input(classifier_model, input):
#     prediction = classifier_model.predict(input)
#     return prediction
    
st.write('\n')
    
if st.button("Click here to classify"):
    
    if uploaded_img is None:
        
        st.write("Please upload an image to classify")
    
    else:
        
        with st.spinner('Classifying ...'):
            prediction = AD_classifier.predict(new_array)
            st.success('Done!')
        st.header('Model predicts: ')


        if prediction <= 0.5:
            
            st.write("Alzheimer's Disease", '\n' )
            
            
                             
        else:
            st.write("Cognitive Normal ",'\n')
            
