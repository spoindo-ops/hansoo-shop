import sys

def fix():
    try:
        # 1. 바이너리 모드로 원본 데이터를 통째로 읽어옴
        with open(r'c:\수익화웹싸이트 첫걸음\hansoo.html', 'rb') as f:
            raw_data = f.read()
        
        # 2. 여러 인코딩으로 디코딩 시도
        for enc in ['utf-8', 'utf-8-sig', 'cp949', 'utf-16', 'latin-1']:
            try:
                decoded_text = raw_data.decode(enc)
                print(f"Decoded successfully with {enc}")
                
                # 3. 브라우저가 읽을 수 있는 표준 UTF-8로 강제 재저장
                with open(r'c:\수익화웹싸이트 첫걸음\hansoo.html', 'w', encoding='utf-8') as f:
                    f.write(decoded_text)
                print("Repair Complete!")
                return
            except Exception as e:
                continue
        print("All decoding attempts failed.")
    except Exception as e:
        print(f"Error: {e}")

fix()
