import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
import matplotlib.pyplot as plt
import numpy as np
import cv2
from io import BytesIO
import time


class ImageGrayscaleConverter:
    """
    A class to handle image conversion to grayscale and related operations.

    Attributes:
        image_file (file): The uploaded image file.
        original_image (PIL.Image): The original loaded image.
        grayscale_image (PIL.Image): The converted grayscale image.
    """

    def __init__(self, image_file):
        """
        Initialize the ImageGrayscaleConverter with an image file.

        Args:
            image_file: A file-like object containing the uploaded image.
        """
        self.image_file = image_file
        self.original_image = None
        self.grayscale_image = None

    def load_image(self):
        """
        Load the image from the uploaded file.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            image_bytes = self.image_file.read()
            self.original_image = Image.open(BytesIO(image_bytes))
            return True
        except Exception as e:
            st.error(f"Error opening image: {e}")
            return False

    def show_original_and_gray_image(self):
        """
        Display the original and grayscale images side by side.
        """
        if self.original_image and self.grayscale_image:
            col1, col2 = st.columns(2)

            with col1:
                st.image(
                    self.original_image,
                    caption="Original Image",
                    use_container_width=True
                )

            with col2:
                st.image(
                    self.grayscale_image,
                    caption="Grayscale Image",
                    use_container_width=True
                )

    def convert_to_grayscale(self):
        """
        Convert the original image to grayscale using Pillow.
        """
        if self.original_image:
            self.grayscale_image = ImageOps.grayscale(self.original_image)

    def generate_histogram(self):
        """
        Generate a histogram of pixel intensities for the grayscale image.
        """
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
        """
        Apply a specified image processing filter to the grayscale image.

        Args:
            filter_type (str): The type of filter to apply. Options are 
                               "Equalize" or "Enhance".
        """
        if self.grayscale_image:
            processed_image = None
            if filter_type == "Equalize":
                processed_image = ImageOps.equalize(self.grayscale_image)
            elif filter_type == "Enhance":
                enhancer = ImageEnhance.Contrast(self.grayscale_image)
                processed_image = enhancer.enhance(1.5)

            if processed_image is not None:
                st.image(
                    processed_image,
                    caption=f"Processed Image ({filter_type})",
                    use_container_width=True
                )
            else:
                return  # Return if no image was processed


def main():
    """
    Main function to run the Streamlit application.
    """
    st.title("Image to Grayscale Converter")

    st.header("What is this app about?")
    st.write(
        "This app takes an image file as input, converts it to grayscale, "
        "and generates a histogram of pixel intensities."
    )

    st.header("How does it work?")
    st.markdown(
        """
    Here's what happens when you upload an image:
    1. 📎 The original image is loaded from the file.
    2. 🖼️ The image is converted to grayscale using Pillow's `ImageOps.grayscale()` method.
    3. 📊 A histogram of pixel intensities is generated using Matplotlib.
    4. 🔧 Select a processing method to either **enhance** or **equalize** the image further.
    """
    )

    uploaded_file = st.file_uploader(
        label="Choose an image...",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        converter = ImageGrayscaleConverter(uploaded_file)

        if converter.load_image():
            with st.spinner("Converting to grayscale..."):
                time.sleep(2)  # Simulate processing time
                converter.convert_to_grayscale()

            converter.show_original_and_gray_image()  # Display both images

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
