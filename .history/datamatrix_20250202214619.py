from zxing import BarCodeReader
import cv2
import numpy as np

def read_datamatrix(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not read image at {image_path}")
            return
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        temp_path = "temp_processed.png"
        cv2.imwrite(temp_path, binary)
        
        reader = BarCodeReader()
        
        result = reader.decode(image_path, possible_formats=['DATA_MATRIX'])
        if not result:
            result = reader.decode(temp_path, possible_formats=['DATA_MATRIX'])
        
        if result:
            print("Decoded content:", result.parsed)
        else:
            print("No Data Matrix code found in the image")
            
        import os
        if os.path.exists(temp_path):
            os.remove(temp_path)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    image_path = r"./datamatrix.png"  # Your image path
    read_datamatrix(image_path)
