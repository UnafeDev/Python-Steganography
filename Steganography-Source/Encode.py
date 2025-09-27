from PIL import Image
import os
from tkinter import Tk, simpledialog
from tkinter.filedialog import askopenfilename, asksaveasfilename

def encode_text_into_image(input_image_path, output_image_path, text):
    # Ensure the output file has a .png extension
    if not output_image_path.lower().endswith('.png'):
        output_image_path += '.png'

    # Create folder if it doesn't exist
    folder = os.path.dirname(output_image_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    # Open the image
    img = Image.open(input_image_path)
    img = img.convert('RGB')
    pixels = img.load()
    
    # Convert text to binary
    binary_text = ''.join([format(ord(c), '08b') for c in text])
    binary_text += '1111111111111110'  # Delimiter to mark end of text

    width, height = img.size
    idx = 0

    for y in range(height):
        for x in range(width):
            if idx < len(binary_text):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary_text[idx])
                pixels[x, y] = (r, g, b)
                idx += 1

    try:
        img.save(output_image_path, format="PNG")
        print(f"Text encoded and saved to {output_image_path}")
    except Exception as e:
        print(f"Error saving image: {e}")


if __name__ == "__main__":
    Tk().withdraw()

    input_path = askopenfilename(title="Select input image", filetypes=[("PNG files","*.png"),("All files","*.*")])
    if not input_path:
        print("No input image selected. Exiting.")
        exit()

    output_path = asksaveasfilename(title="Save encoded image as", defaultextension=".png",
                                    filetypes=[("PNG files","*.png"),("All files","*.*")])
    if not output_path:
        print("No output path selected. Exiting.")
        exit()

    text_input = simpledialog.askstring("Text input", "Enter text directly or path to a .txt file:")
    if not text_input:
        print("No text provided. Exiting.")
        exit()

    if os.path.isfile(text_input):
        with open(text_input, 'r', encoding='utf-8') as f:
            text_to_hide = f.read()
    else:
        text_to_hide = text_input

    encode_text_into_image(input_path, output_path, text_to_hide)
