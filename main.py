from pathlib import Path
from PIL import Image, UnidentifiedImageError, ImageEnhance

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
        print("Unsupported image format. Please try again")
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
        image_mode = image.mode

        if image_mode == "L":
            return image_path            

        grayscale_image = image.convert("L")
        
        grayscale_image.save(output_path)
    
    print(f"Grayscale image saved to {output_path}")
    return output_path

def enhance_contrast(image_path):
    image_path = Path(image_path)

    if image_path.stem.endswith("_contrast"):
        return image_path

    base_stem = image_path.stem.removesuffix("_grayscale")

    output_path = image_path.parent / f"{base_stem}_contrast{image_path.suffix.lower()}"

    if output_path.exists():
        return output_path

    with Image.open(image_path) as image:
        enhancer = ImageEnhance.Contrast(image)

        enhanced_image = enhancer.enhance(2.0)

        enhanced_image.save(output_path)
    print(f"Enhanced image saved to {output_path}")
    return output_path

def show_image_info(image_path):
    with Image.open(image_path) as image:
        image_format = image.format
        image_mode = image.mode
        width, height = image.size

        print(f"Image Information\nImage Name: {Path(image_path).name}\nImage Format: {image_format}\n\
            Image Size: {width} x {height}\nImage Mode: {image_mode}")

image_path = input("Enter Image Path: ")

if validate_image(image_path):    
    show_image_info(image_path)

    processed_image_path = convert_to_grayscale(image_path)
    processed_image_path = enhance_contrast(processed_image_path)