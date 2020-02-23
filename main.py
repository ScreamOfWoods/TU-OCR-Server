#!/usr/bin/env python3

from PIL import Image
import pytesseract
import argparse
import sys

language="eng"

argparser = argparse.ArgumentParser(description="Simple OCR python scrpit")
argparser.add_argument('-i', '--image-path', required=True, type=str, help="Path to the image that will be recognized")
argparser.add_argument('-l', '--language', default=language, type=str, help="Choose desired language")
args = argparser.parse_args()

filename = args.image_path
language = args.language
img = None

try:
    img = Image.open(filename)
except:
    sys.stderr.write("Cannot open file\n")
    sys.exit(1)

text = pytesseract.image_to_string(img, lang=language)
print(text)
