import os

def absolute_fix():
    path = r'c:\수익화웹싸이트 첫걸음\hansoo.html'
    try:
        # 1. 바이너리 모드로 읽기
        with open(path, 'rb') as f:
            raw = f.read()
        
        # 2. 가능한 모든 디코딩 전략 시도
        text = None
        # UTF-8 with BOM, UTF-8, UTF-16, CP949 순으로 시도
        for enc in ['utf-8-sig', 'utf-8', 'utf-16', 'cp949', 'latin-1']:
            try:
                text = raw.decode(enc)
                if '<html' in text.lower():
                    print(f"Decoded with {enc}")
                    break
            except:
                continue
        
        if not text:
            # 최후의 수단: 에러 무시하고 읽기
            text = raw.decode('utf-8', errors='ignore')
            print("Decoded with UTF-8 (ignoring errors)")

        # 3. 비정상적인 Null 바이트(\x00)가 있다면 제거 (UTF-16이 꼬였을 때 흔함)
        cleaned_text = text.replace('\x00', '')
        
        # 4. 완벽한 UTF-8(BOM 없음)로 저장
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(cleaned_text)
            
        print(f"Final Cleanup Success. Size: {os.path.getsize(path)} bytes")

    except Exception as e:
        print(f"Error during absolute fix: {e}")

absolute_fix()
