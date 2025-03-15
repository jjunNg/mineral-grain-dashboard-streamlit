import streamlit as st
import pandas as pd
# import math
# from pathlib import Path
# from PIL import Image
from ultralytics import YOLO


# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Mineral Grain Recognition'
)

st.title("Mineral grain recognition")
st.subheader('validating BSE SEM images using YOLO model to classify images')
uploaded_image = st.file_uploader("Upload Image")

# Load a pretrained YOLO11n model
# model = YOLO("yolo11n.pt")

# Run inference on 'bus.jpg'
# results = model(["https://ultralytics.com/images/bus.jpg", "https://ultralytics.com/images/zidane.jpg"])  # results list

# # Visualize the results
# for i, r in enumerate(results):
#     # Plot results image
#     im_bgr = r.plot()  # BGR-order numpy array
#     im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image

#     # Show results to screen (in supported environments)
#    # r.show()

#     # Save results to disk
#     #r.save(filename=f"results{i}.jpg")

 
# returned_image = model.predict(uploaded_image)


# if uploaded_image:
#     st.image(uploaded_image)

# if returned_image:
#     st.image(returned_image)


# col1, col2 = st.columns(2)

# with col1:
#     st.header("Input image")
#     st.image("./data/image.jpg")

# with col2:
#     st.header("Returned image")
#     st.image("returned_image")


