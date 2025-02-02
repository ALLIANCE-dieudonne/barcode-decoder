import cv2
import numpy as np
from pylibdmtx.pylibdmtx import decode

def read_aztec_code(image_path):
    try:
        # Read the image
        image = cv2.imread(image_path)
        
        if image is None:
            print(f"Error: Could not read image at {image_path}")
            return
        
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Decode Aztec code
        aztec_codes = decode(gray)
        
        if not aztec_codes:
            print("No Aztec codes found in the image")
            return
        
        # Process results
        for aztec in aztec_codes:
            # Decode the data
            data = aztec.data.decode('utf-8')
            print(f"Decoded Data: {data}")
            
            # Draw rectangle around the code (if rect information is available)
            if hasattr(aztec, 'rect'):
                x, y, w, h = aztec.rect
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display the image
        cv2.imshow("Aztec Code Reader", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    image_path = r"path/to/your/aztec_code.png"  # Update this path
    read_aztec_code(image_path)