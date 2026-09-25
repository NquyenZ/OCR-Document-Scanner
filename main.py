from pathlib import Path
from PIL import Image, UnidentifiedImageError

SUPPORTED_EXTENSIONS = [".jpg", ".jpeg", ".png"]

def validate_image(image_path):
    image_path = Path(image_path)
    
    if not image_path.exists():
        print("Can't find image. Please ensure that you entered valid image path")
        return False

    if not image_path.is_file():
        print("Path is not a file. Please ensure that you entered valid image path")
        return False

    if image_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        print("Unsupported image format. Please ensure that you entered valid image path")
        return False

    try:
        with Image.open(image_path) as image:
            image.verify()
    except UnidentifiedImageError:
        print("Invalid or corrupted image file. Please try again")
        return False
    return True

def convert_to_grayscale(image_path):
    image_path = Path(image_path)

    output_path = image_path.parent / f"{image_path.stem}_grayscale{image_path.suffix.lower()}"

    with Image.open(image_path) as image:
        image_mode = image.mode or "Unknown"

        if image_mode != "L":
            grayscale_image = image.convert("L")

            grayscale_image.save(output_path)
        else:
            return image_path
    
    print(f"Grayscale image saved to {output_path}")
    return output_path

def show_image_info(image_path):
    with Image.open(image_path) as image:
        image_format = image.format or "Unknown"
        image_mode = image.mode or "Unknown"
        width, height = image.size

        print(f"Image Information\nImage Name: {Path(image_path).name}\nImage Format: {image_format}\n\
            Image Size: {width} x {height}\nImage Mode: {image_mode}")

image_path = input("Enter Image Path: ")

if validate_image(image_path):    
    show_image_info(image_path)

    grayscaled_image = convert_to_grayscale(image_path)