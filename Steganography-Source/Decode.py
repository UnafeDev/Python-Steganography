from PIL import Image
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def decode_text_from_image(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = img.load()

    binary_text = ""
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_text += str(r & 1)

    # Convert binary to text
    chars = []
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        if byte == '11111111':
            next_byte = binary_text[i+8:i+16]
            if next_byte == '11111110':
                break
        chars.append(chr(int(byte, 2)))
    
    return ''.join(chars)


if __name__ == "__main__":
    Tk().withdraw()

    encoded_image_path = askopenfilename(title="Select encoded image", filetypes=[("PNG files","*.png"),("All files","*.*")])
    if not encoded_image_path:
        print("No image selected. Exiting.")
        exit()

    decoded_text = decode_text_from_image(encoded_image_path)
    print("Decoded text:", decoded_text)

    # Ask where to save the decoded text
    output_text_path = asksaveasfilename(title="Save decoded text as", defaultextension=".txt",
                                         filetypes=[("Text files","*.txt"),("All files","*.*")])
    if not output_text_path:
        print("No save location selected. Exiting.")
        exit()

    # Create folder if it doesn't exist
    folder = os.path.dirname(output_text_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    # Save the decoded text
    try:
        with open(output_text_path, 'w', encoding='utf-8') as f:
            f.write(decoded_text)
        print(f"Decoded text saved to {output_text_path}")
    except Exception as e:
        print(f"Error saving text: {e}")
