import os
from PIL import Image

try:
    import rembg
except ImportError:
    print("rembg not yet installed. Please wait for the pip process to finish.")
    exit(1)

image_dir = r"c:\Users\Jesse\OneDrive\Desktop\Nikki Studio\dist\img"
print(f"Starting background removal in {image_dir}")

for filename in os.listdir(image_dir):
    if filename.startswith("nikki-studio-") and filename.endswith(".jpeg"):
        input_path = os.path.join(image_dir, filename)
        output_filename = filename.replace(".jpeg", ".png")
        output_path = os.path.join(image_dir, output_filename)
        
        if os.path.exists(output_path):
            print(f"Skipping {filename} - PNG already exists.")
            continue
            
        print(f"Processing {filename}...")
        
        # Load image
        input_image = Image.open(input_path)
        
        # Remove background
        output_image = rembg.remove(input_image)
        
        # Save as PNG
        output_image.save(output_path, "PNG")
        print(f"Saved to {output_filename}")
        
print("All done!")
