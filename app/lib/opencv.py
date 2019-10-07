import cv2
import numpy as np
from tilers import tiler_colors

TILER_SIZE = 30
TILERS_COUNT = 50
width_dimension = 20

def find_color(src):
  min_index = 0
  min_difference = 256.0
  for i in tiler_colors[0:TILERS_COUNT]:
    difference = (abs(src[0] - i[2]) + abs(src[1] - i[3]) + abs(src[2] - i[4])) / 3
    if difference == 0:
      return i[0]
    if difference < min_difference:
      min_index = i[0]
      min_difference = difference

  return tiler_colors[min_index]


img = cv2.imread("lena.jpg")
height = 1
height_dimension = img.shape[0] * width_dimension // img.shape[1]
new_width = width_dimension * TILER_SIZE
new_height = height_dimension * TILER_SIZE
print("shape:", img.shape)
print("new_shape:", new_height, new_width)
print("dimension:", height_dimension, width_dimension)
cv2.imshow("src", img)

#resize
img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
arr = np.array(img)
print(len(arr))
for h_index in range(0, height_dimension):
  for w_index in range(0, width_dimension):
    sub_arr = arr[h_index * TILER_SIZE: (h_index + 1) * TILER_SIZE, w_index * TILER_SIZE: (w_index + 1) * TILER_SIZE]
    aver_color = np.mean(np.reshape(sub_arr, (-1, 3)), axis=0)
    tiler_color_com = find_color(aver_color)
    if tiler_color_com[-1]:
      name = "./tilers/" + "-".join([str(x) for x in tiler_color_com[0:5]]) + ".jpg"
      tiler_arr = np.array(cv2.imread(name))
      arr[h_index * TILER_SIZE: (h_index + 1) * TILER_SIZE, w_index * TILER_SIZE: (w_index + 1) * TILER_SIZE] = tiler_arr
    else:
      arr[h_index * TILER_SIZE: (h_index + 1) * TILER_SIZE, w_index * TILER_SIZE: (w_index + 1) * TILER_SIZE] = tiler_color_com[2:5]
cv2.imshow("sd", arr)
cv2.waitKey()