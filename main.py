import cv2
import sys

"""
PersonAi Cartoonface

personai_icartoonface_detval_00000.jpg
180,84,219,125
93,87,140,125
110,18,139,47
3,84,37,119
43,2,73,49

widerface
20--Family_Group/20_Family_Group_Family_Group_20_739.jpg
2
372 232 134 192 0 0 0 0 0 0
528 204 124 176 0 0 0 0 0 0
"""

if __name__ == "__main__":
    image_name = 'widerface.jpg'
    #  window_name = "Image"

    image = cv2.imread(image_name)
    print(image)
    if image is None:
        sys.exit("Could not read the image.")

    cv2.imshow("Display window", image)
    k = cv2.waitKey(0)
    if k == ord("s"):
        pass
               





