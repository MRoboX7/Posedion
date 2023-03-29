# Posedion
Poseidon is a yoga pose detection project that uses a convolutional neural network (CNN), OpenCV, and MediaPipe to detect and track yoga poses in real time. It is deployed on Streamlit and provides users with a variety of features, including the ability to set model parameters, display real-time input and output streams with landmark recording, and use both cameras and uploaded files as input.

## Installation
To run Poseidon, you will need to have Python 3 installed on your system, as well as several Python packages, including OpenCV, MediaPipe, TensorFlow, and Streamlit. You can install these packages using the following command:

```pip install opencv-python mediapipe tensorflow streamlit```

## Usage
To use Poseidon, navigate to the project directory in your terminal and run the following command:

```streamlit run app.py```

This will launch the Poseidon app in your default browser. From there, you can use your camera or upload a file to detect yoga poses in real time.

Poseidon provides several options for setting model parameters, such as the confidence threshold and the number of threads to use. You can also view real-time input and output streams with landmark recording, which can be useful for debugging or analyzing the performance of the model.

## Encoded Images
The images used in project have been encoded in UTF-8 format and are included within the code itself to make the project more portable. The encoded images can be found in the code itself.
The encoder used to encode images is also attatched : ```image_encoder.py```

## Contributing
If you would like to contribute to Poseidon, feel free to fork the project on GitHub and submit a pull request with your changes.

## License
Poseidon is distributed under the MIT license

## Contact
If you have any questions or feedback about Poseidon, please feel free to contact us at mrobox7@gmail.com. I would love to hear from you!
