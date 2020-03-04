#!/usr/bin/env python3

import argparse
import sys
import ocr

language="eng"

argparser = argparse.ArgumentParser(description="Simple OCR python scrpit")
argparser.add_argument('-i', '--image-path', required=True, type=str, help="Path to the image that will be recognized")
argparser.add_argument('-l', '--language', default=language, type=str, help="Choose desired language")
args = argparser.parse_args()

filename = args.image_path
language = args.language

try:
    print(ocr.extract_text(filename, language))
except:
    sys.exit(1)
