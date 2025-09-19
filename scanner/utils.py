import cv2
from tkinter import filedialog
from pyzbar.pyzbar import decode
from PIL import Image, ImageTk

def openFile():
    filePath = filedialog.askopenfilename(
        title="Open an Image File",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    return filePath

def scanFile(path):
    try:
        image = cv2.imread(path)
        
        if image is None:
            print(f"Warning: Could not read image from path: {path}")
            return []
            
        barcodes = decode(image)
        return barcodes
    
    except Exception as e:
        print(f"An error occurred during scanning: {e}")
        return []

def imageConvertToTk(path, size):
    img = Image.open(path).resize(size)
    return ImageTk.PhotoImage(img)
