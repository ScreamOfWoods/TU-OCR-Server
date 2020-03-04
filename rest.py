#!/usr/bin/env python3

import base64
import random
import string
import os
from flask import Flask
from flask import request


IMAGE_DIR = '/mnt/win/TU_Projects/KZ/recv_imgs/'
lang="eng"

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def invoke_ocr():
    error = None
    #Get the parameters from the request
    photo_str = request.get_data()
    #print(photo_str)
    lang = request.args.get('lang')

    #TODO spawn the ocr tool
    #Save the photo data to the storage
    filename = save_photo(photo_str)
    print("OCR IN PROGRESS")
    print(lang)
    #print("Deleting photo from server")
    #os.remove(filename) 
    return 'Hello!'


def save_photo(photo_stream):
    img = base64.b64decode(photo_stream)
    filename = IMAGE_DIR + random_string() + ".png"
    with open(filename, 'wb') as file:
        file.write(img)
        file.close()
    return filename


def random_string(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

