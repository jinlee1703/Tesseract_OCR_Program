"""
Author : Jinwoo Lee
Date : 2021.12.07.
Program Name : OCR_Program (PDF File)
Explanation : Make OCR_Program from Tesseract OCR
"""

import pytesseract as pt
from PIL import Image

pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

import fitz
doc = fitz.open('pdfFile.pdf')
page = doc.load_page(4)
mat = fitz.Matrix(2, 2)
pix = page.get_pixmap(matrix=mat)
output = 'pdfFile.png'
pix.save(output)

img = Image.open('pdfFile.png')
result = pt.image_to_string(img, lang='kor')
print(result)
