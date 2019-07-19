#!/usr/bin/env python3

import sys
import pytesseract
import numpy as np
from PIL import Image

argv = sys.argv
if len(argv) != 2:
    print('Usage: ./ocr.py <filename>')

img = Image.open(argv[1])
im_list = np.array(img)

txt = pytesseract.image_to_string(img)
print(txt)
