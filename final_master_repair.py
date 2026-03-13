import os

def final_master_repair():
    path = r'c:\수익화웹싸이트 첫걸음\hansoo.html'
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. 시카 마스크 섹션 교체
        cica_target = """                <div class="story-title reveal">
                    <h4>02. VIVA DERMA 데일리케어 마스크류</h4>
                </div>"""
        cica_replace = """                <div class="story-title reveal">
                    <h4>
                        <span class="lang-ko">02. VIVA DERMA 데일리케어 마스크 - 시카</span>
                        <span class="lang-en">02. VIVA DERMA Daily Care Mask - Cica</span>
                    </h4>
                </div>"""
        
        # 2. 브랜드 태그 및 가격WON 교체 (반복적인 패턴 활용)
        # 여러번 고생했던 WON 단위들을 정규식 느낌으로 일괄 교체
        content = content.replace('판매가: 4,000원 (정가: 6,000원)', '<span class="lang-ko">판매가: 4,000원 (정가: 6,000원)</span><span class="lang-en">Price: 4,000 WON (Retail: 6,000 WON)</span>')
        
        # 시카 섹션 타이틀 교체 시도
        if cica_target in content:
            content = content.replace(cica_target, cica_replace)
            print("Cica Section Title Replaced.")

        # 트러블 패치 섹션 타이틀 교체 시도
        patch_target = "<h4>07. VIVA DERMA 마이크로니들 트러블 패치</h4>"
        patch_replace = """<h4>
                        <span class="lang-ko">07. VIVA DERMA 마이크로니들 트러블 패치</span>
                        <span class="lang-en">07. VIVA DERMA Micro-needle Trouble Patch</span>
                    </h4>"""
        if patch_target in content:
            content = content.replace(patch_target, patch_replace)
            print("Trouble Patch Title Replaced.")

        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(content)
        print("Master Repair Complete.")

    except Exception as e:
        print(f"Error: {e}")

final_master_repair()
