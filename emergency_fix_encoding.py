import sys

try:
    # 1. 파일을 여러 인코딩으로 시도하여 읽음 (보통 한글 윈도우는 cp949 혹은 utf-8)
    encodings = ['utf-8', 'cp949', 'utf-16']
    content = None
    
    for enc in encodings:
        try:
            with open(r'c:\수익화웹싸이트 첫걸음\hansoo.html', 'r', encoding=enc) as f:
                content = f.read()
            print(f"Successfully read with {enc}")
            break
        except:
            continue
            
    if content:
        # 2. 강제로 표준 UTF-8 (BOM 없음)으로 저장
        with open(r'c:\수익화웹싸이트 첫걸음\hansoo.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully fixed encoding to UTF-8")
    else:
        print("Failed to read file with known encodings")

except Exception as e:
    print(f"Error: {e}")
