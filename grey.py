from pdf2image import convert_from_path
from PIL import Image

# Path to the PDF file
pdf_path = 'Color.pdf'
# Directory to save the images
image_output_dir = 'output-gray/'

# Convert PDF to images
images = convert_from_path(pdf_path, dpi=300)  # dpi=300 ensures high quality

for i, image in enumerate(images):
    # Save the colored image
    colored_image_path = f"{image_output_dir}page_{i+1}.png"
    image.save(colored_image_path, 'PNG')

    # Convert to black and white
    bw_image = image.convert('L')
    # Save the black and white image
    bw_image_path = f"{image_output_dir}page_{i+1}_bw.png"
    bw_image.save(bw_image_path, 'PNG')

print("Conversion complete!")
