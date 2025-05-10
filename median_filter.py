import cv2
import sys

def median_filter(stego_input, blurred_output):
    # Làm mờ ảnh bằng Median Blur
    img = cv2.imread(stego_input)
    blurred_img = cv2.medianBlur(img, 3)  # kernel size = 3
    cv2.imwrite(blurred_output, blurred_img)
    print("Blurred stego image with Gaussian blur.")

# input
try:
    stego_path = sys.argv[1]
    img1 = cv2.imread(stego_path)
    blur_path = sys.argv[2]
    median_filter(stego_path,blur_path)
except :
    print("Invalid!")
