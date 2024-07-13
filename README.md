# QR Code and Barcode Scanner

This project is a simple QR code and barcode scanner using OpenCV and PyZbar in Python. It supports input from a webcam, image file, or video file. When a QR code or barcode is detected, the data is printed, and if it contains a URL, the URL is automatically opened in the web browser.

## Features
- Scan QR codes and barcodes from a live webcam feed.
- Scan QR codes and barcodes from an image file.
- Scan QR codes and barcodes from a video file.
- Automatically open URLs contained in the QR codes or barcodes.

## Prerequisites
- Python 3.x
- OpenCV
- PyZbar

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/qr-barcode-scanner.git
    cd qr-barcode-scanner
    ```

2. Install the required packages:
    ```bash
    pip install opencv-python pyzbar
    ```

## Usage
1. Run the script:
    ```bash
    python scanner.py
    ```

2. Select the input type:
    - Enter `0` for camera (webcam).
    - Enter `1` for an image file.
    - Enter `2` for a video file.

3. If you selected an image or video file, you will be prompted to enter the path to the file.

4. The scanner will start, and it will print the type and data of any detected QR code or barcode. If the data contains a URL, it will be opened in the default web browser.

### Example
```bash
Enter the input type (0 for camera, 1 for image, 2 for video): 1
Enter the path to your image or video: path/to/your/image.jpg
Type: QRCODE, Data: https://www.example.com
