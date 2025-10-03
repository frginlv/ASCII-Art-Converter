from PIL import Image 

ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "  # brightness from dark to light

def pixel_to_char(brightness: int) -> str:
    num_chars = len(ASCII_CHARS)  
    return ASCII_CHARS[int(brightness / 256 * num_chars)]
 
def image_to_ascii(input_path: str, new_width: int = 100) -> str:
    """Convert an image to ASCII art and return it as a string."""
    img = Image.open(input_path).convert("L")
    width, height = img.size 
    ratio = height / width * 0.55
    new_height = max(1, int(new_width * ratio))
    img = img.resize((new_width, new_height)) 

    ascii_art = ""
    for y in range(img.height):
        for x in range(img.width):
            brightness = img.getpixel((x, y))
            ascii_art += pixel_to_char(brightness)
        ascii_art += "\n"

    return ascii_art


