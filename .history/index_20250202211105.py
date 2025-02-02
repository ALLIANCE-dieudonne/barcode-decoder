from pyzbar.pyzbar import decode
from PIL import Image
import cv2

def decode_barcode(image_path):
    image = Image.open(image_path)
    
    barcodes = decode(image)
    
    for barcode in barcodes:
        # Get the barcode data as a string
        barcode_data = barcode.data.decode('utf-8')
        # Get the barcode type
        barcode_type = barcode.type
        
        print(f"Found {barcode_type} barcode: {barcode_data}")

    return barcodes

# Example usage
if __name__ == "__main__":
    # Replace with your image path
    image_path = "./barcode.png"
    results = decode_barcode(image_path)
    
    if not results:
        print("No barcode found in the image")