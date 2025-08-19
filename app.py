from flask import Flask,render_template,request,jsonify
from werkzeug.utils import secure_filename
import uuid
import os

import google.generativeai as genai
import PIL.Image
from pathlib import Path
import base64
import io
from PIL import Image

app =  Flask(__name__)

def setup_gemini_api():

    api_key = "AIzaSyA4tiLvv2wajS0FEy2a1BwSqmdTQPNPHKA"
    genai.configure(api_key=api_key)
    return genai

def select_model(model_name="gemini-2.5-flash"):
    """
    Select and initialize a specific model
    
    Available models (August 2025):
    - gemini-2.5-pro: Most powerful, best for complex reasoning
    - gemini-2.5-flash: Best price-performance, general use
    - gemini-2.5-flash-lite: Cost-efficient, high throughput
    - gemini-2.0-flash: Next-gen features, 1M token context
    - gemini-2.0-flash-preview-image-generation: Image generation capable
    - gemini-1.5-flash: Legacy but still functional
    - gemini-1.5-pro: Legacy, higher capability
    """
    try:
        model = genai.GenerativeModel(model_name)
        print(f"✅ Successfully loaded model: {model_name}")
        return model
    except Exception as e:
        print(f"❌ Error loading model {model_name}: {str(e)}")
        return None

def query_with_image_from_path(model, text_prompt, image_path):
    """Query model with image from local file path"""
    try:
        image = PIL.Image.open(image_path)
        response = model.generate_content([text_prompt, image])
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


@app.route('/')
def home():
    return render_template('emotion_detector.html')

@app.route('/engine', methods=['GET','POST'])
def engine():
    if request.method == 'POST':
        img = request.files.get('image')

        if img and img.filename != "":
            upload_folder = 'uploads'
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
        # i am overwrinting the name here on purpose
        file_extension = 'jpg'
        name = f"lunafireX.{file_extension}"

        filename = secure_filename(name)
        file_path = os.path.join(upload_folder,filename)
        img.save(file_path)

        setup_gemini_api()
        model = select_model(model_name="gemini-2.5-flash-lite")
        prompt = """
        I will present you with a picture.
        Your task is to identify the emotion on the face and select the closest match from:
        ['happiness', 'sadness', 'fear', 'anger', 'surprise', 'disgust','no_face','neutral'].
        Respond with only one word — the chosen emotion.
        """
        path = file_path

        result = query_with_image_from_path(model, prompt,path)
        print(f'---------------{result}')


        detected_emotion = result

        return jsonify({
            'result': detected_emotion
        })
            
    return 'prime'

if __name__ == "__main__":
    app.run(debug = True)