#opencv module for image processing
import cv2
import hmac
import hashlib
import time
import urllib

im_rgb = cv2.imread('black_and_white.jpg')
im_gray = cv2.cvtColor(im_rgb, cv2.COLOR_BGR2GRAY)
# first the image you sent me is not ideal bw image.so to convert it bw image..1. rgb image -> gray image 2. gray image->bw image to do this, you have to determine threshold value. as you know pixel value is 0~255 so 127 is middle value of it.so this line will convert image to bw image with 127 threthold value.
thresh = 127
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
dim = (10, 10)
# resize image
im_bw = cv2.resize(im_bw, dim, interpolation = cv2.INTER_AREA)
img_str = ""
cv2.imwrite("resize.png", im_bw)
for i in range(0, 10):
    for j in range(0, 10):
        if im_bw[j][i] == 0:
            img_str += "1"
        elif im_bw[j][i] == 255:
            img_str += "0"

print(img_str)
#this is the string retrived from image.
secret = str(int(time.time() * 1000))
print(secret)
#creating a random string with time function to input to hmac ramdom key
generation
secret_key = hmac.new(b'random_key', secret.encode('utf-8'), hashlib.sha256).hexdigest()

#storing it into a file.
file1 = open("RandomKey.key", "w")
file1.writelines(secret_key)
file1.close()

#extracting key using ranom key generated and str
image_key = hmac.new(secret_key.encode('utf-8'), img_str.encode('utf-8'), hashlib.sha256).hexdigest()
print(image_key)

storing the image key in file
file1 = open("ImageKey.key", "w")
file1.writelines(image_key)
file1.close()