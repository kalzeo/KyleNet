from tempfile import NamedTemporaryFile

import timeit
import numpy as np
import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

from scorecam import ScoreCAM


def get_prediction(model, img):
    classes = {0: "COVID-19", 1: "NON-COVID"}
    img = load_img(img, target_size=(224, 224))
    img = img_to_array(img) / 255
    img = np.expand_dims(img, axis=0)
    prediction = (model.predict(img, batch_size=128) > 0.5).astype("int")
    return classes.get(prediction[0][0])


def main():
    model = load_model("../models/Experiment 4.h5")
    st.set_page_config(page_title="KyleNet UI")

    # Add the sidebar
    st.sidebar.subheader("Welcome to KyleNet UI\nAn interface for the KyleNet CNN model")
    st.sidebar.subheader("Images")
    buffer = st.sidebar.file_uploader(label="Upload your image file.",
                                      type=["png", "jpeg", "jpg"],
                                      accept_multiple_files=False)

    if buffer is not None:
        file_info = {"name": buffer.name,
                     "type": buffer.type,
                     "size": f'{round(buffer.size / 1024, 2)}KB'
                     }

        # Save the buffer to a temp file so that predictions / score-cam can be carried out
        temp_file = NamedTemporaryFile(delete=False, suffix=".png")
        temp_file.write(buffer.read())

        prediction = get_prediction(model, temp_file.name)

        # Build the score cam
        score_cam = ScoreCAM(temp_file.name)
        score_cam.cam()
        superimposed = score_cam.superimpose()

        # Setup the columns for the images
        col1, col2 = st.beta_columns(2)
        original_image = Image.open(buffer)

        col1.header("Original")
        col1.image(original_image, use_column_width=True)

        col2.header("Score-CAM")
        col2.image(superimposed, use_column_width=True)

        # Misc Info
        st.write(f"### Prediction: {prediction}")
        st.write("___")
        st.write("### File Information")
        st.write(file_info)


if __name__ == '__main__':
    main()
    #exe_time = timeit.timeit(main, number=1)
    #st.write("___")
    #st.write("### Execution Time")
    #st.write(exe_time)
