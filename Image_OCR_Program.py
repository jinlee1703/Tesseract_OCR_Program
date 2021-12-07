"""
Author : Jinwoo Lee
Date : 2021.12.07.
Program Name : OCR_Program (Image File)
Explanation : Make OCR_Program from Tesseract OCR
"""

import pytesseract as pt
from PIL import Image

pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('image.jpg')
result = pt.image_to_string(img, lang='kor')
print(result)

