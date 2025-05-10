import numpy as np
import cv2
import sys

# Tính PSNR giữa ảnh gốc và ảnh sau tấn công
def psnr(original_img: np.ndarray, attacked_img: np.ndarray) -> float:
    mse = np.mean((original_img.astype(np.float32) - attacked_img.astype(np.float32)) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    return 10 * np.log10((max_pixel ** 2) / mse)

# input
try:
    stego_path = sys.argv[1]
    blur_path = sys.argv[2]
    
    img1 = cv2.imread(stego_path)
    img2 = cv2.imread(blur_path)

    psnr_value = psnr(img1, img2)
    print(f"PSNR: {psnr_value}")
except :
    print("Invalid!")
