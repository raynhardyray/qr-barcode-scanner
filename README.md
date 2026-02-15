# QR-Barcode-Scanner

A lightweight **Python-application** that decodes **QR codes and barcodes** that you uploaded.

This project leverages:

- [OpenCV](https://opencv.org/) – Camera handling and computer vision
- [Pyzbar](https://pypi.org/project/pyzbar/) – QR code and barcode decoding
- [ttkbootstrap](https://ttkbootstrap.readthedocs.io/) – Modern themed Tkinter UI
- [Pillow](https://python-pillow.org/) – Image processing support
---

## Prerequisites
Before running the project, ensure you have:
- **Python 3.12** or earlier installed  
- A functional **webcam**

Check your Python version:
```bash
python --version
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/raynhardyray/qr-barcode-scanner.git
cd qr-barcode-scanner
```

### Install Dependencies
You can install manually:
```bash
pip install opencv-python pyzbar ttkbootstrap Pillow
```
Or using `requirements.txt`:
```bash
pip install -r requirements.txt
```
---

## Usage

Run the main script:
```bash
python main.py
```

### Scanning
- Upload image
- Click Scan Image
- The decoded data will appear in the GUI.
  
---
