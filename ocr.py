#!/usr/bin/env python3

import os
import pytesseract
from PIL import Image
import numpy as np

img = Image.open('table.png')
im_list = np.array(img)

txt = pytesseract.image_to_string(img)
print(txt)
