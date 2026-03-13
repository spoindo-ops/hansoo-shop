import sys
import os

def final_repair():
    path = r'c:\수익화웹싸이트 첫걸음\hansoo.html'
    try:
        # 1. 파일을 바이너리로 읽음
        with open(path, 'rb') as f:
            raw = f.read()
        
        # 2. UTF-16LE (BOM 포함/미포함) 시도
        # PowerShell 5.1의 기본은 UTF-16LE입니다.
        possible_encodings = ['utf-16', 'utf-16-le', 'utf-8-sig', 'utf-8', 'cp949']
        
        for enc in possible_encodings:
            try:
                text = raw.decode(enc)
                if 'DOCTYPE' in text or 'html' in text:
                    print(f"Success with {enc}!")
                    # 3. 브라우저가 가장 좋아하는 UTF-8 (BOM 없음)으로 저장
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(text)
                    print("Repair successful!")
                    return True
            except:
                continue
                
        # 3. 만약 다 실패하면... null 바이트가 섞인 것임
        print("Standard decodings failed. Trying emergency null-strip...")
        text = raw.replace(b'\x00', b'').decode('utf-8', errors='ignore')
        if 'DOCTYPE' in text:
             with open(path, 'w', encoding='utf-8') as f:
                f.write(text)
             print("Emergency repair via null-strip successful!")
             return True
             
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

final_repair()
