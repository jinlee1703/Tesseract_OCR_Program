"""
Author : Jinwoo Lee
Date : 2021.12.07.
Program Name : OCR_Program (Image File)
Explanation : Make OCR_Program from Tesseract OCR
"""

import pytesseract as pt
from PIL import Image

pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'      # 테서렉트 설치 위치

img = Image.open('image.jpg')                   # 읽어올 이미지 파일 열기
result = pt.image_to_string(img, lang='kor+eng')    # 이미지를 통해 변환한 문자열을 담는  result 변수
print(result)                                   # 변환한 문자열 출력

