# Tính tỷ lệ bit lỗi giữa tin gốc và tin trích xuất

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
    bits = ''.join(format(ord(c), '08b') for c in extracted_msg)
    return bits


def bit_error_rate(original_bits: str, extracted_bits: str) -> float:
    min_len = min(len(original_bits), len(extracted_bits))
    errors = sum(1 for i in range(min_len) if original_bits[i] != extracted_bits[i])
    return errors / min_len if min_len > 0 else 1.0

try:
    stego_path = sys.argv[1]
    blur_path = sys.argv[2]

    img1 = cv2.imread(stego_path)
    img2 = cv2.imread(blur_path)

    text1=extract_lsb(stego_path)
    text2=extract_lsb(blur_path)
    print("BER: ",bit_error_rate(text1,text2))
    
except :
    print("Invalid!")
