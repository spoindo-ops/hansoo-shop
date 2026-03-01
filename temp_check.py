import sys
from PIL import Image

try:
    img = Image.open(r"c:\수익화웹싸이트 첫걸음\image updated\Gemini_Generated_Image_8nxm5u8nxm5u8nxm.png").convert("L")
    w, h = img.size
    print(f"Size: {w}x{h}")
    
    # scan for very dark pixels (lum < 50)
    dark_pixels = []
    for y in range(0, h, 10):
        for x in range(0, w, 10):
            lum = img.getpixel((x, y))
            if lum < 50:
                dark_pixels.append((x, y))
    
    print(f"Found {len(dark_pixels)} dark pixels")
    # print some representative bounds if clumped
    # simple box finding: 
    if len(dark_pixels) > 0:
        print(f"Min X: {min(p[0] for p in dark_pixels)}")
        print(f"Max X: {max(p[0] for p in dark_pixels)}")
        print(f"Min Y: {min(p[1] for p in dark_pixels)}")
        print(f"Max Y: {max(p[1] for p in dark_pixels)}")

except Exception as e:
    print(f'Error: {e}')
