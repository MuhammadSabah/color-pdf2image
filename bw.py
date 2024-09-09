import cv2
from pdf2image import convert_from_path
from PIL import Image
import numpy as np

# Path to the PDF file
pdf_path = 'Color.pdf'
# Directory to save the images
image_output_dir = 'output/'

# Convert PDF to images
images = convert_from_path(pdf_path, dpi=300)  # dpi=300 ensures high quality

for i, image in enumerate(images):
    # Save the colored image
    colored_image_path = f"{image_output_dir}page_{i+1}.png"
    image.save(colored_image_path, 'PNG')

    # Convert to black and white using adaptive thresholding
    image_np = np.array(image)
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

    # Apply median blur to reduce noise
    median_blurred = cv2.medianBlur(gray_image, 3)
    # Apply Gaussian blur to further reduce noise
    blurred_image = cv2.GaussianBlur(median_blurred, (5, 5), 0)

    # Apply adaptive thresholding
    bw_image = cv2.adaptiveThreshold(
        blurred_image,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # Convert back to PIL Image and save
    bw_image_pil = Image.fromarray(bw_image)
    bw_image_path = f"{image_output_dir}page_{i+1}_bw.png"
    bw_image_pil.save(bw_image_path, 'PNG')

print("Conversion complete!")
