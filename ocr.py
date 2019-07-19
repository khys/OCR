#!/usr/bin/env python3

import os
import sys
import pytesseract
from PIL import Image
import numpy as np

argv = sys.argv
if len(argv) != 2:
    print('Usage: ./ocr.py <filename>')

img = Image.open(argv[1])
im_list = np.array(img)

txt = pytesseract.image_to_string(img)
print(txt)
