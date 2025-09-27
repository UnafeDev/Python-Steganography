# 🖼️ Image Text Encoder & Decoder

Hide and reveal text within images with ease! This project uses **steganography** to encode text into images without visibly altering them. Perfect for secure messages, creative projects, or just experimenting with hidden data in images.  

---

## ⚡ How It Works
- **Encoding:**  
  - Converts your text into binary.  
  - Hides the binary data in the **least significant bits** of the image’s pixels.  
  - Saves a new image with the hidden message while keeping the original picture intact.  

- **Decoding:**  
  - Reads the modified image.  
  - Extracts the binary data from the pixels.  
  - Converts it back into readable text.  
  - Optionally saves the decoded text into a `.txt` file.  

- **Automatic folder creation:** Save paths automatically create folders to keep your files organized.  

---

## 🛠️ Features
- ✅ Encode text directly or from a `.txt` file.  
- ✅ Decode hidden messages and export them as `.txt`.  
- ✅ File dialogs for easy path selection—no manual typing needed.  
- ✅ Works with `.exe` builds (Windows) without crashing.  
- ✅ Almost invisible changes to the original image.  

---

## 💡 Practical Uses
- 🔒 **Secret messages**: Share hidden text securely.  
- 🎨 **Art projects**: Embed messages into artwork images.  
- 📝 **Notes storage**: Hide notes inside images for fun or organization.  
- 🧪 **Learning & experiments**: Study binary encoding and image manipulation.  

---

## 📦 How to Use (EXE)
1. Run `Encrypt.exe` to hide text in an image.  
2. Run `Decrypt.exe` to reveal and export the hidden text.  
3. Use file dialogs to select images and save locations.

## 📦Alternative (CMD)
1. Run `py Encode.py` to encode
2. Run `py Decode.py` to decode
---

Made By **UnafeDev**
