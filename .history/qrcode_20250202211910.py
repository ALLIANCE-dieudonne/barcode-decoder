import cv2
from pyzbar.pyzbar import decode
import os

def read_qr_code(image_path):
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist")
        return
    
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error: Could not read the image at {image_path}")
        return
    
    qr_codes = decode(image)
    
    if not qr_codes:
        print("No QR codes found in the image")
        return
    
    for qr in qr_codes:
        qr_data = qr.data.decode('utf-8')
        qr_type = qr.type
        
        print(f"Type: {qr_type}")
        print(f"Data: {qr_data}")
    
    

# Example usage
if __name__ == "__main__":
    # Make sure to use the correct path to your image
    # Use raw string (r"path") or forward slashes for Windows paths
    image_path = r"./qrcode.png"  # Update this path
    read_qr_code(image_path)