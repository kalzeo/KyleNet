from pathlib import Path
from tempfile import NamedTemporaryFile
import cv2
import numpy as np
import streamlit as st
import pandas as pd
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from scorecam import ScoreCAM
from SessionState import get

st.set_page_config(page_title="KyleNet UI")
st.info("For Experimental Purposes Only")

# Create a state session to track the files details ie predictions/images/file info
state = get(files={})

# Add the sidebar and its contents
st.sidebar.subheader("Welcome to KyleNet UI\nAn interface for the KyleNet CNN model\nCreated by Kyle McPherson")
st.sidebar.subheader("Images")
buffer = st.sidebar.file_uploader(label="Upload your image file",
                                  type=["png", "jpeg", "jpg"],
                                  accept_multiple_files=True)

model = load_model("../models/Experiment 4.h5")


def get_prediction(model, img):
    classes = {0: "COVID-19", 1: "NON-COVID"}
    img = load_img(img, target_size=(224, 224))
    img = img_to_array(img) / 255
    img = np.expand_dims(img, axis=0)
    prediction = (model.predict(img, batch_size=128) > 0.5).astype("int")
    return classes.get(prediction[0][0])


def read_buffer(buffer):
    for file in buffer:
        file_info = {"name": file.name,
                     "type": file.type,
                     "mime": f".{file.type.split('/')[1]}",
                     "size": f"{round(file.size / 1024, 2)}KB"
                     }

        # Store the file if its not been uploaded already
        if file_info.get("name") not in state.files:
            # Save the buffer to a temp file so that predictions / score-cam can be carried out
            with NamedTemporaryFile(delete=False, suffix=file_info.get("mime")) as temp_file:
                temp_file.write(file.read())

                prediction = get_prediction(model, temp_file.name)

                dim = (300, 300)

                # Build the score cam
                score_cam = ScoreCAM(temp_file.name)
                score_cam.cam()

                # Make sure both images are the same sizes
                original_image = Image.open(file).resize(dim, Image.ANTIALIAS)
                superimposed = cv2.resize(score_cam.superimpose(), dim, cv2.INTER_AREA)

            # Remove the temp file after use
            Path(temp_file.name).unlink()

            # Store the files in the session state
            state.files[file_info.get("name")] = [file_info, original_image, superimposed, prediction]


def main():
    if buffer is not None:
        read_buffer(buffer)

    if state.files:
        state.dropdown = st.sidebar.selectbox("Select an image to view",
                                              options=[file for file in state.files.keys()],
                                              index=0)

    if state.dropdown is not None:
        selection = state.files.get(state.dropdown)

        # Setup the columns for the images
        col1, col2 = st.beta_columns(2)
        col1.header("Original")
        col1.image(selection[1])

        col2.header("Score-CAM")
        col2.image(selection[2])

        # Misc Info
        st.subheader(f"Prediction: {selection[3]}")
        st.write("___")
        st.subheader("File Information")
        df = pd.json_normalize(selection[0])
        st.table(df)


if __name__ == '__main__':
    main()
