from zxing import BarCodeReader

def read_maxicode(image_path):
    try:
        # Initialize the reader
        reader = BarCodeReader()
        
        # Decode the MaxiCode
        result = reader.decode(image_path, possible_formats=['MAXICODE'])
        
        # Print result
        if result:
            print("Decoded content:", result.parsed)
        else:
            print("No MaxiCode found in the image")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    image_path = r"path/to/your/maxcode.png"  # Update this path
    read_maxicode(image_path)