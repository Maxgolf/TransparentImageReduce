import os
from PIL import Image

# === Settings ===
INPUT_FOLDER = 'input_images'
OUTPUT_FOLDER = 'output_images'
THRESHOLD = 60            # Green detection sensitivity
SCALE_FACTOR = 0.5        # Resize to 50% of original size

# === Setup ===
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def is_green(pixel, threshold=THRESHOLD):
    r, g, b = pixel[:3]
    return g > r + threshold and g > b + threshold

# === Main Processing Loop ===
for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith(('.webp', '.png', '.jpg', '.jpeg')):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_filename = os.path.splitext(filename)[0] + '.webp'
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)

        # Open image
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()

        # Remove green background
        newData = [(0, 0, 0, 0) if is_green(p) else p for p in datas]
        img.putdata(newData)

        # Resize image
        new_size = (int(img.width * SCALE_FACTOR), int(img.height * SCALE_FACTOR))
        img = img.resize(new_size, Image.Resampling.LANCZOS)

        # Save as transparent webp
        img.save(output_path, "WEBP", lossless=True)
        print(f"Processed: {filename} -> {output_filename}")