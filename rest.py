#!/usr/bin/env python3

import base64
import random
import string
import os
import ocr
from flask import Flask
from flask import request
from PIL import Image
from io import BytesIO

lang="eng"
recognized_text = ""

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def invoke_ocr():
    #Get the parameters from the request
    photo_str = request.get_data()
    lang = request.args.get('lang')

    #Load the image in memory
    #spawn the ocr tool
    img = Image.open(BytesIO(base64.b64decode(photo_str)))
    print("OCR IN PROGRESS")

    try:
        recognized_text = ocr.extract_text(img, lang)
    except Exception as e:
        print(str(e))
        return "Something happend. Cannot parse photo", 500

    return recognized_text;
