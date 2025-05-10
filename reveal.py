from stegano import lsb
import sys
import cv2
def extract_lsb(stego_path):
    # Trích xuất tin\
    try:
        extracted_msg = lsb.reveal(stego_path)
        print("Tin trích xuất: ", extracted_msg)
    except:
        print("Không thể trích xuất tin giấu")

# input
try:
    stego_path = sys.argv[1]
    img1 = cv2.imread(stego_path)

    extract_lsb(stego_path)
except:
    print("Ảnh không tồn tại")