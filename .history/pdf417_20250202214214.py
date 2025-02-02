from zxing import BarCodeReader
import cv2
import numpy as np

def read_pdf417(image_path):
    try:
        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not read image at {image_path}")
            return
        
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply thresholding to get binary image
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Save preprocessed image temporarily
        temp_path = "temp_processed.png"
        cv2.imwrite(temp_path, binary)
        
        # Initialize the reader
        reader = BarCodeReader()
        
        # Try to decode both original and processed image
        result = reader.decode(image_path, possible_formats=['PDF_417'])
        if not result:
            result = reader.decode(temp_path, possible_formats=['PDF_417'])
        
        # Print result
        if result:
            print("Decoded content:", result.parsed)
        else:
            print("No PDF417 barcode found in the image")
            
        # Clean up temporary file
        import os
        if os.path.exists(temp_path):
            os.remove(temp_path)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    image_path = r"./pdf417.png"  # Your current path
    read_pdf417(image_path)