import numpy as np
import cv2
import sys
from skimage.metrics import structural_similarity as ssim

# Tính SSIM giữa 2 ảnh
def calc_ssim(img1: np.ndarray, img2: np.ndarray) -> float:
    # Chuyển về grayscale nếu ảnh có 3 kênh
    if len(img1.shape) == 3:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    if len(img2.shape) == 3:
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    return ssim(img1, img2)


# input
try:
    stego_path = sys.argv[1]
    blur_path = sys.argv[2]
    
    img1 = cv2.imread(stego_path)
    img2 = cv2.imread(blur_path)

    ssim_value = calc_ssim(img1, img2)
    print(f"SSIM: {ssim_value}")

except :
    print("Invalid!")