import cv2 
import numpy as np
import matplotlib.pyplot as plt

man = cv2.imread('super-man.jpg')
man_rgb = cv2.cvtColor(man, cv2.COLOR_BGR2RGB)
plt.imshow(man_rgb)
plt.show()

sky = cv2.imread('sky.jpg')
sky_rgb = cv2.cvtColor(sky, cv2.COLOR_BGR2RGB)
plt.imshow(sky_rgb)
plt.show()

sky = cv2.resize(sky, (man.shape[1], man.shape[0]))
sky_rgb = cv2.cvtColor(sky, cv2.COLOR_BGR2RGB)
plt.imshow(sky_rgb)
plt.show()

man = cv2.resize(man, None, fx = 1, fy = 1)
sky = cv2.resize(sky, None, fx = 1, fy = 1)
# I gave 1 for values becuase my pics are same size

man_hsv = cv2.cvtColor(man, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(man_hsv)


rows, cols, _ = man.shape
for i in range(rows):
    for j in range(cols):
        if 35<H[i,j]<80 and 30<S[i,j] and 80<V[i,j]:
            man[i,j] = sky[i,j]


cv2.imwrite('result.jpg', man)

