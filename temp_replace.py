import os

path = r'C:\수익화웹싸이트 첫걸음\eden_mask.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

old_str = 'image updated/eden_mask_hydration_new.jpg'
new_str = 'image updated/eden_mask_hydration_text_down.jpg'

if old_str in text:
    new_text = text.replace(old_str, new_str)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced successfully")
else:
    print("Not found")
