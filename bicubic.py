# -*- coding: utf-8 -*-
"""
# @Time    : 2022/12/17 00:53
# @Author  : Bill
# @File    : bicubic.py
# @Comment : Null
"""
import os
import cv2

def main():
    lr_image_dir = ""
    hr_image_dir = ""
    scale = 2
    os.makedirs(hr_image_dir, exist_ok=True)

    supported_img_formats = (".bmp", ".dib", ".jpeg", ".jpg", ".jpe", ".jp2",
                             ".png", ".pbm", ".pgm", ".ppm", ".sr", ".ras", ".tif",
                             ".tiff")

    # Upsample LR images
    for filename in os.listdir(lr_image_dir):
        if not filename.endswith(supported_img_formats):
            continue
        name, ext = os.path.splitext(filename)
        # Read LR image
        lr_img = cv2.imread(os.path.join(lr_image_dir, filename))
        # Upsample image
        lr_image = cv2.resize(lr_img, (0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(os.path.join(hr_image_dir + filename.split('.')[0] + ext), lr_image)

if __name__ == "__main__":
    main()
