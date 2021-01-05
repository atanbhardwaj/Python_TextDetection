import cv2
import numpy as np
import requests
import io
import json

img = cv2.imread("textimage.png")
print(img.shape)
scale_percent = 50
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized_img = cv2.resize(img, dim)

# ocr

url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".png", resized_img, [1, 90])
file_bytes = io.BytesIO(compressedimage)


result = requests.post(
    url_api, files={"textimage.png": file_bytes}, data={"apikey": "apikey"}
)

result = result.content.decode()
result = json.loads(result)
text_detected = result.get("ParsedResults")[0].get("ParsedText")
print(text_detected)


cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()