import cv2
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Decode QR code
    qr_codes = decode(image)
    
    # Process each QR code found
    for qr in qr_codes:
        # Get the QR code data
        qr_data = qr.data.decode('utf-8')
        qr_type = qr.type
        
        # Draw rectangle around QR code
        points = qr.polygon
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            cv2.polylines(image, [hull], True, (0, 255, 0), 2)
        else:
            cv2.polylines(image, [np.array(points, dtype=np.int32)], True, (0, 255, 0), 2)
        
        # Print the data
        print(f"Type: {qr_type}")
        print(f"Data: {qr_data}")
    
    # Display the image
    cv2.imshow("QR Code Reader", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    # Replace with your QR code image path
    image_path = "./qrcode.py"
    read_qr_code(image_path)