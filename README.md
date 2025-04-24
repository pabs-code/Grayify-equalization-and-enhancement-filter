# Image-Grayscale Histogram Generator

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://choosealicense.com/licenses/mit/)

## Table of Contents
- [Image to Grayscale Converter](#image-to-grayscale-converter)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Setup Instructions](#setup-instructions)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [Tests](#tests)
  - [Contact Information](#contact-information)
  - [Acknowledgments](#acknowledgments)
  - [License](#license)

## About
This Streamlit application converts an uploaded image to grayscale and generates a histogram of pixel intensities. It also offers two filter options - Equalize (histogram equalization) and Enhance (contrast enhancement). This project uses Python libraries such as `streamlit`, `Pillow` for image processing, `numpy`, `matplotlib`, and `opencv-python`.

## Features
1. Image upload capability
2. Conversion to grayscale
3. Generation of pixel intensity histogram
4. Two filter options: Equalize and Enhance
5. A user-friendly interface powered by Streamlit

## Requirements
The application requires the following Python packages:
- `streamlit`
- `Pillow` (for image processing)
- `numpy`
- `matplotlib`
- `opencv-python`

You can install them using pip:
```bash
pip install streamlit Pillow numpy matplotlib opencv-python
```

## Setup Instructions
1. Clone this repository to your local machine.
2. Navigate into the project directory (e.g., `cd image_to_grayscale_converter`).
3. Run the app using Streamlit:
   ```bash
   streamlit run main.py
   ```
   
Note: Ensure you have [Streamlit](https://www.streamlit.io/install) installed on your machine to run this application.

## Usage
1. Open `main.py` in your browser (e.g., http://localhost:8501 if you're using Streamlit's default settings).
2. Click on "Choose an image..." button to upload a JPG, JPEG, or PNG file.
3. After uploading, the app will display the original image and convert it to grayscale.
4. A histogram of pixel intensities will be generated and displayed below the grayscale image.
5. Optionally, you can apply an Equalize (histogram equalization) or Enhance (contrast enhancement) filter.

## Contributing
Contributions are welcome! Feel free to report bugs, request new features, or submit pull requests. Please follow the [Code of Conduct](https://github.com/yourusername/image_to_grayscale_converter/blob/master/CODE_OF_CONDUCT.md).

1. Fork this repository.
2. Create a new branch for your feature (`git checkout -b feature/awesome-feature`).
3. Commit your changes (`git commit -m 'Add some awesome feature'`).
4. Push to the branch (`git push origin feature/awesome-feature`).
5. Submit a pull request.

## Tests
This project includes unit tests in `test_main.py` file using Python's built-in `unittest` framework. To run the tests, execute:
```bash
python -m unittest test_main.py
```

## Contact Information
For questions or support, please contact [Your Name](mailto:your.email@example.com).

## Acknowledgments
This project was inspired by the need for a straightforward grayscale converter with histogram generation and simple filters. Thanks to Streamlit for providing an easy way to create web apps in Python!

## License
This project is licensed under the MIT License - see [LICENSE](https://github.com/pabs-code/image-grayscale-histogram-generator/blob/main/LICENSE) file for details.
