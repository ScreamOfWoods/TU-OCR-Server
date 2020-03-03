#!/usr/bin/env python3

import base64
from flask import Flask
from flask import request

IMAGE_DIR = '/mnt/win/TU_Projects/KZ/recv_imgs/'

app = Flask(__name__)

@app.route('/ocr', methods=['GET', 'POST'])
def invoke_ocr():
    error = None
    #TODO Get the parameters from the request
    photo_str = request.form.get('photo')
    #photo_name = request.form.get('photo_name')
    #TODO spawn the ocr tool
    print(photo_str)
    return 'Hello!'


def save_photo(photo_stream, photo_name):
    img = base64.b64decode(photo_stream)
    filename = IMAGE_DIR + photo_name + ".png"
    with open(filename, 'wb') as f:
        f.write(img)

