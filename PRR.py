# Tính tỷ lệ ký tự phục hồi thành công
from stegano import lsb
import sys
import cv2

def extract_lsb(image_path):
    # Trích xuất tin
    try:
        extracted_msg = lsb.reveal(image_path)
    except:
        extracted_msg = ''
    # Chuyển chuỗi sang chuỗi bit
    return extracted_msg

def recovery_rate(original_text: str, extracted_text: str) -> float:
    min_len = min(len(original_text), len(extracted_text))
    correct = sum(1 for i in range(min_len) if original_text[i] == extracted_text[i])
    return correct / len(original_text) if len(original_text) > 0 else 0.0

try:
    stego_path = sys.argv[1]
    blur_path = sys.argv[2]

    img1 = cv2.imread(stego_path)
    img2 = cv2.imread(blur_path)

    text1=extract_lsb(stego_path)
    text2=extract_lsb(blur_path)
    print("PRR: ",recovery_rate(text1,text2))
except :
    print("Invalid!")