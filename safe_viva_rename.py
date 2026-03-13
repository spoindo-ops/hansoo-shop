import os

def safe_replace_viva():
    path = r'c:\수익화웹싸이트 첫걸음\hansoo.html'
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. 브랜드명 통일 (한국어는 유지, 이후 영문 섹션 추가 시 자동 적용됨)
        # 이미 있는 영문 brand 영역이나 제목들을 VIVA DERMA로 교체
        content = content.replace('VIVADERMA', 'VIVA DERMA')
        content = content.replace('비바더마', 'VIVA DERMA') # 영문 섹션 추가 시 한글이 오면 안되므로 미리 교체
        
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Success: VIVA DERMA name unified safely.")
    except Exception as e:
        print(f"Error: {e}")

safe_replace_viva()
