"""
Author : Jinwoo Lee
Date : 2021.12.07.
Program Name : OCR_Program (PDF File)
Explanation : Make OCR_Program from Tesseract OCR
"""

import pytesseract as pt
from PIL import Image

pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'          # 테서렉트 설치 위치

import fitz

doc = fitz.open('pdfFile.pdf')                  # 읽어올 pdf 파일 열기
page = doc.load_page(4)                         # 읽어올 페이지 번호(0부터 시작)
mat = fitz.Matrix(2, 2)                         # X, Y 방향의 확대/축소 비율을 입력받아 행렬을 생성
pix = page.get_pixmap(matrix=mat)               # 래스터 형식으로 페이지 이미지 생성
output = 'pdfFile.png'                          # pdf 파일을 png 파일로 저장하기 위해 파일명 지정
pix.save(output)                                # png 파일 저장

img = Image.open('pdfFile.png')                 # 읽어올 이미지 파일 열기
result = pt.image_to_string(img, lang='kor')    # 이미지를 통해 변환한 문자열을 담는  result 변수
print(result)                                   # 변환한 문자열 출력