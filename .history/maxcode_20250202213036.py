import cv2
import numpy as np
from zxing import BarCodeReader

def read_maxicode(image_path):
    try:
        # Initialize the barcode reader
        reader = BarCodeReader()
        
        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not read image at {image_path}")
            return
            
        # Attempt to decode MaxiCode
        result = reader.decode(image_path, possible_formats=['MAXICODE'])
        
        if result is None:
            print("No MaxiCode found in the image")
            return
            
        # Display the results
        print("MaxiCode Detected!")
        print(f"Decoded Text: {result.parsed}")
        print(f"Format: {result.format}")
        print(f"Raw Bytes: {result.raw}")
        
        # Display the image
        cv2.imshow("MaxiCode Reader", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Enhanced version with image preprocessing
def read_maxicode_enhanced(image_path):
    try:
        # Initialize the reader
        reader = BarCodeReader()
        
        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not read image at {image_path}")
            return
            
        # Preprocess the image
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply adaptive thresholding
        thresh = cv2.adaptiveThreshold(
            gray, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            91, 11
        )
        
        # Save preprocessed image temporarily
        temp_path = "temp_processed.png"
        cv2.imwrite(temp_path, thresh)
        
        # Try to decode the original image
        result = reader.decode(image_path, possible_formats=['MAXICODE'])
        
        # If original fails, try the preprocessed image
        if result is None:
            result = reader.decode(temp_path, possible_formats=['MAXICODE'])
            
        if result is None:
            print("No MaxiCode found in the image")
            return
            
        # Display results
        print("MaxiCode Detected!")
        print(f"Decoded Text: {result.parsed}")
        print(f"Format: {result.format}")
        
        # Display both original and processed images
        cv2.imshow("Original Image", image)
        cv2.imshow("Processed Image", thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Clean up temporary file
        import os
        if os.path.exists(temp_path):
            os.remove(temp_path)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Version with additional preprocessing options
def preprocess_image(image):
    """Apply various preprocessing techniques to improve MaxiCode detection"""
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        91, 11
    )
    
    # Apply morphological operations
    kernel = np.ones((3,3), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    return morph

def read_maxicode_advanced(image_path):
    try:
        # Initialize reader
        reader = BarCodeReader()
        
        # Read image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error: Could not read image at {image_path}")
            return
            
        # Create a list of preprocessed images
        processed_images = []
        
        # Original image
        processed_images.append(("Original", image))
        
        # Preprocessed versions
        processed = preprocess_image(image)
        processed_images.append(("Preprocessed", processed))
        
        # Try different contrast and brightness adjustments
        contrast_img = cv2.convertScaleAbs(image, alpha=1.5, beta=0)
        processed_images.append(("Contrast Enhanced", contrast_img))
        
        # Try decoding with each version
        for name, img in processed_images:
            # Save temporary image
            temp_path = f"temp_{name}.png"
            cv2.imwrite(temp_path, img)
            
            # Attempt to decode
            result = reader.decode(temp_path, possible_formats=['MAXICODE'])
            
            # Clean up temporary file
            import os
            if os.path.exists(temp_path):
                os.remove(temp_path)
            
            if result is not None:
                print(f"MaxiCode detected using {name} image!")
                print(f"Decoded Text: {result.parsed}")
                print(f"Format: {result.format}")
                
                # Display the successful image
                cv2.imshow(f"Successful Image ({name})", img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                return
        
        print("No MaxiCode could be detected in any version of the image")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    image_path = r"path/to/your/maxicode.png"  # Update this path
    
    print("Attempting basic decode...")
    read_maxicode(image_path)
    
    print("\nAttempting enhanced decode...")
    read_maxicode_enhanced(image_path)
    
    print("\nAttempting advanced decode...")
    read_maxicode_advanced(image_path)