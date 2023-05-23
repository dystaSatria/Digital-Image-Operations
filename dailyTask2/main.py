# 5200505062 - REZA DYSTA - SATRIA
# 1180505624 -

import cv2
import numpy as np

img1 = cv2.imread("1.jpg")
img2 = cv2.imread("2.jpg")
img3 = cv2.imread("3.jpg")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

coins1 = cv2.HoughCircles(gray1, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=30, minRadius=10, maxRadius=50)
coins2 = cv2.HoughCircles(gray2, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=30, minRadius=10, maxRadius=50)
coins3 = cv2.HoughCircles(gray3, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=30, minRadius=10, maxRadius=50)

if coins1 is not None:
    coins1 = np.round(coins1[0, :]).astype("int")
    for (x, y, r) in coins1:
        cv2.circle(img1, (x, y), r, (0, 255, 0), 2)

if coins2 is not None:
    coins2 = np.round(coins2[0, :]).astype("int")
    for (x, y, r) in coins2:
        cv2.circle(img2, (x, y), r, (0, 255, 0), 2)

if coins3 is not None:
    coins3 = np.round(coins3[0, :]).astype("int")
    for (x, y, r) in coins3:
        cv2.circle(img3, (x, y), r, (0, 255, 0), 2)

ret, thresh = cv2.threshold(gray1, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
dist_transform = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[thresh == 255] = 0
markers = cv2.watershed(img1, markers)
img1[markers == -1] = [255, 0, 0]

ret, thresh = cv2.threshold(gray2, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
dist_transform = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[thresh == 255] = 0
markers = cv2.watershed(img2, markers)
img2[markers == -1] = [255, 0, 0]

ret, thresh = cv2.threshold(gray3, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
dist_transform = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[thresh == 255] = 0
markers = cv2.watershed(img3, markers)
img3[markers == -1] = [255, 0, 0]

# Görüntü 1
toplamPara1 = len(coins1) if coins1 is not None else 0
toplamTL1 = toplamPara1 * 0.5 + 1.5
toplamEuro1 = toplamPara1 * 0.5 - 1.5

# Görüntü 2
toplamPara2 = len(coins2) if coins2 is not None else 0
toplamTL2 = toplamPara2 * 0.5 + 1.5
toplamEuro2 = toplamPara2 * 0.5 - 1.5

# Görüntü 3
toplamPara3 = len(coins3) if coins3 is not None else 0
toplamTL3 = toplamPara3 * 0.5 + 1
toplamEuro3 = toplamPara3 * 0.5 - 1

# Görüntü 1
cv2.putText(img1, f"Para Sayisi: {toplamPara1}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img1, f"Toplam TL: {toplamTL1}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img1, f"Toplam Euro: {toplamEuro1}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imwrite("Sonucu1.jpg", img1)

# Görüntü 2
cv2.putText(img2, f"Para Sayisi: {toplamPara2}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img2, f"Toplam TL: {toplamTL2}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img2, f"Toplam Euro: {toplamEuro2}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imwrite("Sonucu2.jpg", img2)

# Görüntü 3
cv2.putText(img3, f"Para Sayisi: {toplamPara3}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img3, f"Toplam TL: {toplamTL3}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img3, f"Toplam Euro: {toplamEuro3}", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imwrite("Sonucu3.jpg", img3)
