# Grayify: Image histogram equalization and contrast enhancement filter

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://choosealicense.com/licenses/mit/)


> A simple Streamlit application that allows users to upload images, convert them to grayscale, generate histograms, and apply basic image filters like contrast enhancement or histogram equalization.

---

### Table of Contents

- [Grayify: Image histogram equalization and contrast enhancement filter](#grayify-image-histogram-equalization-and-contrast-enhancement-filter)
    - [Table of Contents](#table-of-contents)
  - [About the Project](#about-the-project)
  - [Features](#features)
  - [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running Script](#running-script)
  - [Expectations When Running This App](#expectations-when-running-this-app)
  - [Demo](#demo)
  - [Acknowledgments](#acknowledgments)
  - [License](#license)

---

## About the Project

This app is a simple yet powerful demonstration of image processing using **Python**, **Streamlit**, and **Pillow**.

It provides an intuitive interface to:
- Upload images
- Convert them to grayscale
- Visualize histograms of pixel intensities
- Apply basic filters like contrast enhancement or histogram equalization

---

## Features

| Feature              | Description                                                                        |
| -------------------- | ---------------------------------------------------------------------------------- |
| Image Upload         | Supports JPG, JPEG, and PNG formats.                                               |
| Grayscale Conversion | Converts uploaded image to grayscale using Pillow's `ImageOps.grayscale()` method. |
| Histogram Generation | Displays a histogram of pixel intensities using Matplotlib.                        |
| Image Filters        | Includes options for **contrast enhancement** or **histogram equalization**.       |

---

## Getting Started

Clone the repository and set up your environment to run the app.

---

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.8+
- Streamlit (`pip install streamlit`)
- Pillow (`pip install pillow`)
- Matplotlib (`pip install matplotlib`)
- Numpy (`pip install numpy`)

You can install all dependencies with:

```bash
pip install streamlit pillow matplotlib numpy
```

or run the provided ```requirements.txt``` file.

---

## Installation

1. Clone the repository (or download it as a ZIP):
   ```bash
   git clone https://github.com/your-repo-url.git
   ```

2. Navigate to the project directory:
   ```bash
   cd image-to-grayscale-converter
   ```

---

## Running Script

To run the app, use the following command in your terminal:

```bash
streamlit run main.py
```

This will start a local development server and open the Streamlit app in your browser.

---

## Expectations When Running This App

- Upload an image file (JPG, JPEG, or PNG).
- The original image is displayed alongside its grayscale version.
- A histogram of pixel intensities is shown for the grayscale image.
- You can apply filters like **enhance** or **equalize** to further process the image.

---

## Demo

Here's a quick overview of how the app works:

1. Upload an image using the file uploader.
2. The original and grayscale versions are displayed side-by-side.
3. A histogram is shown for pixel intensity distribution.
4. Select a filter (Enhance or Equalize) to modify the image further.

> 📌 *Note: This is not a video, but you can imagine how it works by running the app locally.*

---

## Acknowledgments

- **Streamlit** – For creating the web interface.
- **Pillow** – For handling and manipulating images.
- **Matplotlib** – For generating histograms.
- **Numpy** – For array operations.

---

## License
This project is licensed under the MIT License - see [LICENSE](https://github.com/pabs-code/grayify-equalize-enhance-filter/blob/main/LICENSE) file for details.
