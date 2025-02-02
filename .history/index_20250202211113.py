from pyzbar.pyzbar import decode
from PIL import Image
import cv2

def decode_barcode(image_path):
    image = Image.open(image_path)
    
    barcodes = decode(image)
    
    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        
        print(f"Found {barcode_type} barcode: {barcode_data}")

    return barcodes

if __name__ == "__main__":
    image_path = "./barcode.png"
    results = decode_barcode(image_path)
    
    if not results:
        print("No barcode found in the image")