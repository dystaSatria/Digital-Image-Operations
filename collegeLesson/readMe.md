# Cheatsheet

* ## Morphological Transformations

Morfolojik dönüşümler, görüntü işlemede ve bilgisayarlı görü işlemede kullanılan bir dizi işlemdir. Bu işlemler, bir görüntünün şeklini ve yapısını değiştirerek gürültüleri kaldırmaya, özellikleri geliştirmeye ve nesneleri segmente etmeye yardımcı olur.
 
* ##### AŞINDIRMA(Erode)
* ##### YAYMA(dilate)  
* ##### Açma (Opening)
* ##### Kapama (Closing)
* ##### Morfolojik Gradyan

```python
import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the structuring element
kernel = np.ones((3,3), np.uint8)

# Perform erosion and dilation operations
erosion = cv2.erode(img, kernel, iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)

# Perform opening and closing operations
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Compute the gradient of the image
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Display the original and transformed images
cv2.imshow('Original Image', img)
cv2.imshow('Eroded Image', erosion)
cv2.imshow('Dilated Image', dilation)
cv2.imshow('Opened Image', opening)
cv2.imshow('Closed Image', closing)
cv2.imshow('Gradient Image', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()

```


* ## Kenar Bulma

<a data-flickr-embed="true" href="https://www.flickr.com/photos/197661703@N05/52868369621/in/dateposted-public/" title="Screenshot (563)"><img src="https://live.staticflickr.com/65535/52868369621_0ae88abf2d.jpg" width="500" height="253" alt="Screenshot (563)"/></a>

* ##### Canny Operatörü

4 aşamalı bir algoritmadır:

* ###### 1.Gürültü giderme: Kenar algılaması görüntüdeki gürültüye duyarlı olduğundan, ilk adım görüntüdeki gürültüyü 5x5 Gauss filtre ile kaldırmaktır.
* ###### 2.Görüntünün yeğinlikgradyanınınbulunması:Yumuşatılan görüntü daha sonra yatay yönde (Gx) ve dikey yönde (Gy) ilk türevi elde etmek için hem yatay hem de dikey yönde bir Sobelkerneliile filtrelenir. 
* ###### 3.Kenar noktaların çıkarılması: Non-maximumSuppression : Gradyanbüyüklüğü ve yönü belirlenmesi sonrası, kenarı teşkil etmeyen istenmeyen pikselleri kaldırmak için tam bir görüntü taraması yapılır. Bunun için, her pikselde, pikselin, gradyanyönünde komşuları arasında yerel bir maksimum olup olmadığı kontrol edilir. Piksel lokal maksimum ise bir sonraki aşamaya geçer, değilse 0 değeri atanır(suppression).
* ###### 4.Bağlama ve eşikleme: Hysteresis : Bu aşamada, hangi kenarların hangilerinin gerçekten kenar, hangilerinin olmadığına karar verilir. Bunun için minValve maxValolmak üzere iki eşik değeri kullanılır.

<a data-flickr-embed="true" href="https://www.flickr.com/photos/197661703@N05/52868661969/in/dateposted-public/" title="Screenshot (565)"><img src="https://live.staticflickr.com/65535/52868661969_4f5af8478d.jpg" width="500" height="312" alt="Screenshot (565)"/></a><script async src="//embedr.flickr.com/assets/client-code.js" charset="utf-8"></script>

