#!/usr/bin/env python3

from PIL import Image
import pytesseract
import sys

def extract_text(file_path, language):
    img = None
    if isinstance(file_path, str):
        try:
            img = Image.open(file_path)
        except:
            sys.stderr.write("Cannot open file\n")
            raise
    else:
        img = file_path

    return pytesseract.image_to_string(img, lang=language)
