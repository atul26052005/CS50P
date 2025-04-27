import sys
import os
from PIL import Image, ImageOps

def main():
    # Ensure exactly two command-line arguments are provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Validate file extensions
    valid_extensions = (".jpg", ".jpeg", ".png")
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Error: Only JPEG or PNG files are allowed.")

    if input_ext != output_ext:
        sys.exit("Error: Input and output file extensions must match.")

    # Process image
    try:
        overlay_shirt(input_path, output_path)
    except FileNotFoundError:
        sys.exit(f"Error: File '{input_path}' not found.")

def overlay_shirt(input_path, output_path):
    """Overlays shirt.png onto input image after resizing and cropping it."""
    try:
        # Open the input image
        image = Image.open(input_path)

        # Open the shirt image
        shirt = Image.open("shirt.png")
        shirt_size = shirt.size  # Get size (width, height)

        # Resize and crop the input image to match the shirt size
        image = ImageOps.fit(image, shirt_size)

        # Overlay the shirt
        image.paste(shirt, shirt)

        # Save the output image
        image.save(output_path)
    except FileNotFoundError:
        sys.exit("Error: 'shirt.png' file not found.")

if __name__ == "__main__":
    main()
