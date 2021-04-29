from pathlib import Path
from tempfile import NamedTemporaryFile
from timeit import timeit

import cv2
import numpy as np

import pandas as pd
import psutil as ps

import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

from SessionState import get
from scorecam import ScoreCAM

model = load_model("model.h5")

st.set_page_config(page_title="KyleNet UI")
st.info("For Experimental Purposes Only")

# Create a state session to track the files details ie predictions/images/file info
state = get(files={}, dropdown=None)

# Add the sidebar and its contents
st.sidebar.subheader("Welcome to KyleNet UI\nAn interface for the KyleNet CNN model\nCreated by Kyle McPherson")
st.sidebar.subheader("Images")
buffer = st.sidebar.file_uploader(label="Upload your image file",
                                  type=["png", "jpeg", "jpg"],
                                  accept_multiple_files=True)

expander = None


def get_prediction(img):
    """
    Generates a prediction for an image file.
    Any predictions > 0.5 are considered NON-COVID (1), < 0.5 are considered COVID-19 (0).

    :param img: Path to the image file.
    :return: String value with a prediction of 'COVID-19' or 'NON-COVID'.
    """
    classes = {0: "COVID-19", 1: "NON-COVID"}
    img = load_img(img, target_size=(224, 224))
    img = img_to_array(img) / 255
    img = np.expand_dims(img, axis=0)
    prediction = (model.predict(img, batch_size=128) > 0.5).astype("int")
    return classes.get(prediction[0][0])


def process_buffer(file_buffer):
    """
    Process the contents of a file buffer to generate a score-cam and a prediction for each image.

    Images that have already been uploaded/processed are kept in a stateless session until the app
    is closed, allowing content to load faster. This prevents predictions and score-cams for existing
    images being re-generated if they're accidentally removed from the app.

    :param file_buffer: The files currently in the buffer.
    :return: Dict{} stored in the session containing each files images, prediction, and file information.
    """
    for file in file_buffer:
        file_info = {
            "name": file.name,
            "type": file.type,
            "mime": f".{file.type.split('/')[1]}",
            "size": f"{round(file.size / 1024, 2)}KB"
        }

        if file_info.get("name") not in state.files:
            # Save each image to a temp file that'll be removed after use to generate a score-cam and a prognosis.
            with NamedTemporaryFile(delete=False, suffix=file_info.get("mime")) as temp_file:
                temp_file.write(file.read())

                dim = (300, 300)
                prediction = get_prediction(temp_file.name)

                score_cam = ScoreCAM(temp_file.name)
                score_cam.cam()

                # Resize both images to the same sizes
                original_image = Image.open(file).resize(dim, Image.ANTIALIAS)
                superimposed = cv2.resize(score_cam.superimpose(), dim, cv2.INTER_AREA)

            Path(temp_file.name).unlink()

            # Store the files in the session state to avoid getting wiped
            state.files[file_info.get("name")] = [file_info, original_image, superimposed, prediction]


def main():
    if buffer is not None:
        process_buffer(buffer)

    if state.files:
        state.dropdown = st.sidebar.selectbox("Select an image to view",
                                              options=[file.name for file in buffer],
                                              index=0)

    # Only execute if the dropdown has options
    if state.dropdown is not None:
        results = state.files.get(state.dropdown)

        # Setup the columns for the images
        col1, col2 = st.beta_columns(2)
        col1.header("Original")
        col1.image(results[1])

        col2.header("Score-CAM")
        col2.image(results[2])

        st.subheader(f"Prediction: {results[3]}\n___")


if __name__ == '__main__':
    time_exec = timeit(main, number=1)
    expander = st.beta_expander("Click to View Miscellaneous Info", expanded=False)

    with expander:
        # Execution time
        st.write(f"### Execution Time\n{round(time_exec, 2)}s\n")

        # RAM usage
        st.write("___\n### RAM Usage (GB)\n")
        
        ram_usage = ps.virtual_memory()._asdict()
        for value in ram_usage:
            if value != "percent":
                ram_usage[value] /= np.power(1024, 3)

        st.write(ram_usage)
