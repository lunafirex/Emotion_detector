# Emotion Detector 🎭

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-3.1.1-blue.svg)](https://flask.palletsprojects.com/en/3.0.x/)
[![Google Generative AI](https://img.shields.io/badge/Google%20AI-Generative-yellowgreen)](https://ai.google/)

A simple web application that detects emotions from images. 📸

## Description

This project is a Flask-based web application that allows users to upload an image and get the emotion detected from the face in the image. It uses the Google Generative AI's Gemini model to analyze the image and determine the emotion.

## Features ✨

-   Upload an image file.
-   Detects the following emotions:
    -   Happiness 😊
    -   Sadness 😢
    -   Fear 😨
    -   Anger 😠
    -   Surprise 😮
    -   Disgust 🤢
    -   Neutral 😐
-   Displays the detected emotion to the user.
-   Simple and easy-to-use web interface.

## How it Works ⚙️

1.  The user uploads an image through the web interface.
2.  The Flask server receives the image and saves it to the `uploads` directory.
3.  The application then calls the Google Generative AI API with the uploaded image and a prompt to detect the emotion.
4.  The Gemini model processes the image and returns the detected emotion as a single word.
5.  The Flask server sends the detected emotion back to the web interface as a JSON response.
6.  The web interface displays the detected emotion to the user.

## Installation 🛠️

1.  **Clone the repository:**

    ```bash
    https://github.com/lunafirex/Emotion_detector.git
    ```

2.  **Create a virtual environment and activate it:**

    ```bash
    uv venv
    source .venv/bin/activate # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    ```bash
    uv sync
    ```

4.  **Set up your environment variables:**

    Create a `.env` file in the root directory and add your Gemini API key:

    ```
    GEMINI_API_KEY=your_api_key
    ```

## Usage 🚀

1.  **Run the Flask application:**

    ```bash
    uv run app.py
    ```

2.  **Open your web browser and go to:**

    ```
    http://127.0.0.1:5000
    ```

3.  **Upload an image and see the detected emotion!**

## Technologies Used 💻

-   **Backend:**
    -   [Flask](https://flask.palletsprojects.com/en/3.0.x/)
    -   [Google Generative AI](https://ai.google/)
-   **Frontend:**
    -   HTML
    -   CSS
    -   JavaScript
-   **Dependencies:**
    -   `google-generativeai`
    -   `Pillow`
    -   `python-dotenv`

---

Made with ❤️ by [LunafireX](https://github.com/lunafirex)