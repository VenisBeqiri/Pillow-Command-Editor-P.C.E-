from PIL import Image, ImageFilter, ImageEnhance
import sys

def load_image(path):
    try:
        return Image.open(path)
    except IOError:
        print("Unable to open image.")
        sys.exit(1)

def save_image(image, path):
    image.save(path)
    print(f"Saved image to {path}")

def apply_filter(image, filter_type):
    filters = {
        "BLUR": ImageFilter.BLUR,
        "CONTOUR": ImageFilter.CONTOUR,
        "DETAIL": ImageFilter.DETAIL,
        "SHARPEN": ImageFilter.SHARPEN
    }
    chosen_filter = filters.get(filter_type.upper())
    if chosen_filter:
        return image.filter(chosen_filter)
    print("Filter not recognized.")
    return image

def adjust_brightness(image, level):
    return ImageEnhance.Brightness(image).enhance(level)

def adjust_contrast(image, level):
    return ImageEnhance.Contrast(image).enhance(level)

def mirror_image(image, direction):
    if direction == "horizontal":
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    elif direction == "vertical":
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    print("Invalid direction.")
    return image

def display_menu():
    print("\nOptions:")
    options = [
        "1. Apply Blur", "2. Apply Contour", "3. Apply Detail", 
        "4. Apply Sharpen", "5. Adjust Brightness", 
        "6. Adjust Contrast", "7. Mirror Image", 
        "8. Save Image", "9. Quit"
    ]
    print("\n".join(options))

def main():
    path = input("Image path: ")
    image = load_image(path)
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            image = apply_filter(image, "BLUR")
            print("Blur applied.")
        elif choice == "2":
            image = apply_filter(image, "CONTOUR")
            print("Contour applied.")
        elif choice == "3":
            image = apply_filter(image, "DETAIL")
            print("Detail applied.")
        elif choice == "4":
            image = apply_filter(image, "SHARPEN")
            print("Sharpen applied.")
        elif choice == "5":
            try:
                level = float(input("Brightness level (0.0 - 2.0): "))
                image = adjust_brightness(image, level)
                print("Brightness adjusted.")
            except ValueError:
                print("Invalid level.")
        elif choice == "6":
            try:
                level = float(input("Contrast level (0.0 - 2.0): "))
                image = adjust_contrast(image, level)
                print("Contrast adjusted.")
            except ValueError:
                print("Invalid level.")
        elif choice == "7":
            direction = input("Mirror direction (horizontal/vertical): ").strip().lower()
            image = mirror_image(image, direction)
            print(f"Image mirrored {direction}.")
        elif choice == "8":
            save_path = input("Save path (include file extension): ")
            save_image(image, save_path)
        elif choice == "9":
            print("Exiting.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
