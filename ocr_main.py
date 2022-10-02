import pytesseract
import argparse
import cv2
# construct the argument parser and parse the arguments}
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# use Tesseract to OCR the image
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
text = pytesseract.image_to_string(image)
print(text)