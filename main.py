import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
import matplotlib.pyplot as plt
import numpy as np
import cv2
from io import BytesIO
import time


class ImageGrayscaleConverter:
    def __init__(self, image_file):
        self.image_file = image_file
        self.original_image = None
        self.grayscale_image = None

    def load_image(self):
        try:
            image_bytes = self.image_file.read()
            self.original_image = Image.open(BytesIO(image_bytes))
            return True
        except Exception as e:
            st.error(f"Error opening image: {e}")
            return False

    def show_original_image(self):
        if self.original_image:
            st.image(
                self.original_image, caption="Original Image", use_container_width=True
            )
            self.thumbnail = cv2.cvtColor(
                np.array(self.original_image), cv2.COLOR_RGB2BGR
            )
            st.image(self.thumbnail, caption="Thumbnail", use_container_width=True)

    def convert_to_grayscale(self):
        self.grayscale_image = ImageOps.grayscale(self.original_image)

    def show_grayscale_image(self):
        if self.grayscale_image:
            st.image(
                self.grayscale_image,
                caption="Grayscale Image",
                use_container_width=True,
            )

    def generate_histogram(self):
        if self.grayscale_image:
            img_array = np.array(self.grayscale_image)
            hist, bins = np.histogram(img_array.flatten(), 256, range=(0, 256))

            fig, ax = plt.subplots(figsize=(10, 4))
            ax.hist(hist, bins=bins, color="gray")
            ax.set_title("Grayscale Image Histogram")
            ax.set_xlabel("Pixel Intensity")
            ax.set_ylabel("Frequency")

            st.pyplot(fig)

    def apply_filter(self, filter_type):
        if self.grayscale_image:
            img_eq = None  # Initialize the variable to be assigned later
            if filter_type == "Equalize":
                img_eq = ImageOps.equalize(self.grayscale_image)
            elif filter_type == "Enhance":
                enhancer = ImageEnhance.Contrast(self.grayscale_image)
                img_eq = enhancer.enhance(1.5)

            if img_eq is not None:  # Check if the image was processed
                st.image(
                    img_eq,
                    caption=f"Processed Image ({filter_type})",
                    use_container_width=True,
                )
            else:
                return  # Return if no image was processed


def main():
    st.title("Image to Grayscale Converter")

    st.header("What is this app about?")
    st.write(
        "This app takes an image file as input, converts it to grayscale, and generates a histogram of pixel intensities."
    )

    st.header("How does it work?")
    st.write(
        "Here's what happens when you upload an image: 1. The original image is loaded from the file. 2. The image is converted to grayscale using Pillow's ImageOps.grayscale method. 3. A histogram of pixel intensities is generated using Matplotlib."
    )

    uploaded_file = st.file_uploader(
        label="Choose an image...", type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        converter = ImageGrayscaleConverter(uploaded_file)

        if converter.load_image():
            st.image(
                converter.original_image,
                caption="Original Image",
                use_container_width=True,
            )

            with st.spinner("Converting to grayscale..."):
                time.sleep(2)  # Simulate processing time
                converter.convert_to_grayscale()

            with st.spinner("Generating histogram..."):
                time.sleep(2)  # Simulate processing time
                converter.generate_histogram()

            filter_type = st.selectbox(
                "Select a processing method", ["None", "Equalize", "Enhance"]
            )
            if filter_type != "None":
                converter.apply_filter(filter_type)


if __name__ == "__main__":
    main()
