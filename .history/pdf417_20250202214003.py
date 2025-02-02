from zxing import BarCodeReader

def read_pdf417(image_path):
    try:
        # Initialize the reader
        reader = BarCodeReader()
        
        # Decode the PDF417 barcode
        result = reader.decode(image_path, possible_formats=['PDF_417'])
        
        # Print result
        if result:
            print("Decoded content:", result.parsed)
        else:
            print("No PDF417 barcode found in the image")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    image_path = r"path/to/your/pdf417.png"  # Update this path
    read_pdf417(image_path)