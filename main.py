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
    #  image_name = 'cartoon.jpg'
    image_name = 'widerface.jpg'


    #  180,84,219,125
    #  93,87,140,125
    #  110,18,139,47
    #  3,84,37,119
    #  43,2,73,49


    image = cv2.imread(image_name)
    print(image)

    if image is None:
        sys.exit("Could not read the image.")

    thickness = 2
    color = (255, 0, 0)

    #  start_point, end_point = (180,84), (219,125)
    #  image = cv2.rectangle(image, start_point, end_point, color, thickness)

    #  start_point, end_point = (93,87),(140,125)
    #  image = cv2.rectangle(image, start_point, end_point, color, thickness)

    start_point, end_point = (372,232),(134,192)
    image = cv2.rectangle(image, start_point, end_point, color, thickness)

    #  start_point, end_point = (528,204),(124,176)
    #  image = cv2.rectangle(image, start_point, end_point, color, thickness)

    cv2.imshow("Display window", image)
    k = cv2.waitKey(0)
    if k == ord("s"):
        pass


               





