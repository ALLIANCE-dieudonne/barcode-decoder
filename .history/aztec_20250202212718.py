import cv2
import numpy as np
from zxing import BarCodeReader

def read_aztec_code(image_path):
    try:
        reader = BarCodeReader()
        
        result = reader.decode(image_path)
        
        if result is None:
            print("No Aztec code found in the image")
            return
        
        print(f"Decoded Text: {result.parsed}")
        print(f"Format: {result.format}")
        
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    image_path = r"./aztec.png"  # Update this path
    read_aztec_code(image_path)