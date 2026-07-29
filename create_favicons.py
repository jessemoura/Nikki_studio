from PIL import Image
import os

source_path = r'c:\Users\Jesse\OneDrive\Desktop\Nikki Studio\dist\img\Favicon.png'
dist_dir = r'c:\Users\Jesse\OneDrive\Desktop\Nikki Studio\dist'

if not os.path.exists(source_path):
    print(f"File not found: {source_path}")
    exit(1)

try:
    with Image.open(source_path) as img:
        # Create 32x32
        img_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
        img_32.save(os.path.join(dist_dir, 'favicon-32x32.png'))
        
        # Create 16x16
        img_16 = img.resize((16, 16), Image.Resampling.LANCZOS)
        img_16.save(os.path.join(dist_dir, 'favicon-16x16.png'))
        
        # Create Apple Touch Icon (180x180)
        img_180 = img.resize((180, 180), Image.Resampling.LANCZOS)
        img_180.save(os.path.join(dist_dir, 'apple-touch-icon.png'))
        
        print("Favicons created successfully!")
except Exception as e:
    print(f"Error: {e}")
