from pathlib import Path

image_path = input("Enter Image Path: ")
image_path = Path(image_path)

if image_path.exists():
    print("Image found")
else:
    print("Can't find image. Please ensure that you entered valid image path")