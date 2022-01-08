# Tesseract_OCR_Program

## 프로그램 설명

Google Tesseract를 이용하여 이미지 파일 혹은 PDF 파일의 문자를 읽어와 Console에 출력하는 OCR 프로그램입니다.

## 작업 설계

### 1. **Image_OCR_Program.py**

- 설명 : 이미지 파일에서 문자를 읽어와 Console에 출력하는 파일
- 프로세스
    1. 읽어올 이미지 파일 열기
    2. 이미지를 통해 변환한 문자열을 저장
    3. 저장한 문자열을 출력

### 2. **PDF_OCR_Program.py**

- 설명 : PDF 파일에서 문자를 읽어와 Console에 출력하는 파일
- 프로세스
    1. 읽어올 PDF 파일 열기
    2. 페이지 번호, 페이지 배율 등의 설정값을 입력받음
    3. PDF 파일을 PNG 파일로 저장
    4. PNG 파일 열기
    5. PNG 파일을 통해 변환한 문자열을 저장
    6. 저장한 문자열을 출력
