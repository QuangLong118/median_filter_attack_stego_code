from stegano import lsb
import sys

def embeded_lsb(input_path,stego_path,secret_message):
    secret_image = lsb.hide(input_path, secret_message)
    secret_image.save(stego_path)
    print("[+] Đã giấu tin thành công vào ảnh (sử dụng stegano).")


# input
try:
    input_path = sys.argv[1]
    stego_path = sys.argv[2]
    
    secret_message = sys.argv[3]
    embeded_lsb(input_path,stego_path,secret_message)
except :
    print("Đầu vào không hợp lệ!")