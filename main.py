from pathlib import Path

supported_extensions = [".jpg", ".jpeg", ".png"]

image_path = input("Enter Image Path: ")
image_path = Path(image_path)

if not image_path.exists():
    print("Can't find image. Please ensure that you entered valid image path")
elif not image_path.is_file():
    print("Path is not a file. Please ensure that you entered valid image path")
elif (image_path.suffix.lower()) not in supported_extensions:
    print("Unsupported image format. Please ensure that you entered valid image path")
else:
    print("Valid image file")
