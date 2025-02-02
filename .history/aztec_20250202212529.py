import cv2
import numpy as np
from zxing import BarCodeReader

def read_aztec_code(image_path):
    try:
        # Initialize the reader
        reader = BarCodeReader()
        
        # Read and decode the Aztec code
        result = reader.decode(image_path)
        
        if result is None:
            print("No Aztec code found in the image")
            return
        
        # Display results
        print(f"Decoded Text: {result.parsed}")
        print(f"Format: {result.format}")
        
        # Display the image
        image = cv2.imread(image_path)
        if image is not None:
            cv2.imshow("Aztec Code", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    image_path = r"path/to/your/aztec_code.png"  # Update this path
    read_aztec_code(image_path)