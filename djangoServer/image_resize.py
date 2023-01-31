import os
import glob
import os.path

import cv2

files = glob.glob('data/test/*.jpg')
# src = cv2.imread('data/test/sample.jpg')
# img_upsize = cv2.resize(src, (0, 0), fx=1.2, fy=1.2, interpolation=cv2.INTER_LINEAR)
# cv2.imwrite('data/save/sample_upsize.jpg', img_upsize)
# img_resize = img_upsize[256:1280, 48:816]
# cv2.imwrite('data/save/sample_resize.jpg', img_resize)

for file in files:
    src = cv2.imread(file)
    title, ext = os.path.splitext(file)
    path1, path2, fname = title.split("/")
    print(fname, ext)
    img_upsize = cv2.resize(src, (0, 0), fx=1.2, fy=1.2, interpolation=cv2.INTER_LINEAR)
    img_resize = img_upsize[256:1280, 48:816]
    print(f'data/item_image_resize/{fname}_resize{ext}')
    cv2.imwrite(f'data/item_image_resize/{fname}_resize{ext}', img_resize)


