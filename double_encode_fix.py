def double_encoding_fix():
    path = r'c:\수익화웹싸이트 첫걸음\hansoo.html'
    try:
        # 1. 현재 깨진 상태의 파일을 UTF-8로 읽어옴
        with open(path, 'r', encoding='utf-8') as f:
            broken_text = f.read()
        
        # 2. 이중 인코딩 복구 시도 (UTF-8로 읽은걸 다시 latin-1 바이트로 되돌린 후 UTF-8로 재해석)
        try:
            # 깨진 글자들을 바이트로 되돌림
            recovered_bytes = broken_text.encode('latin-1')
            # 정상적인 UTF-8로 다시 읽음
            fixed_text = recovered_bytes.decode('utf-8')
            print("Double encoding recovery successful!")
        except Exception as e:
            print(f"Standard recovery failed: {e}. Trying alternative recovery...")
            # 만약 실패하면 다른 특수 패턴 복구 시도
            fixed_text = broken_text
            
        # 3. 만약 복구된 텍스트에 여전히 문제가 없다면 저장
        if fixed_text and '<html' in fixed_text.lower():
            with open(path, 'w', encoding='utf-8', newline='') as f:
                f.write(fixed_text)
            print("File successfully restored and saved as UTF-8.")
        else:
            print("Restored text seems invalid, aborting save.")

    except Exception as e:
        print(f"Critical Error in double_encoding_fix: {e}")

double_encoding_fix()
