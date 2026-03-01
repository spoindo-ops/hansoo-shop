import easyocr
import cv2

reader = easyocr.Reader(['ko'])
img_path = r"c:\수익화웹싸이트 첫걸음\image updated\Gemini_Generated_Image_8nxm5u8nxm5u8nxm.png"
result = reader.readtext(img_path)

for (bbox, text, prob) in result:
    print(f"Text: {text}, BBox: {bbox}")
