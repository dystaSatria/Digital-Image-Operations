# Final Summary 

## Adaptif Esikleme 

```python
cv2.AdaptiveThreshold(src, dst, maxValue, adaptive_method=CV_ADAPTIVE_THRESH_MEAN_C, thresholdType=CV_THRESH_BINARY, blockSize=3, param1=5)

```

## otsunun ikilestirmesi(Binarization)
* Kami menggunakan nilai yang dipilih secara acak sebagai nilai ambang batas global. Tapi dengan Otsu Yontemiyle gerek kalmaz.
* Otsu metodu, goruntu histogramindan optimal bir global eşik değeri beliler.

## Şablon Eşleştirme
* Şablon Eşleştirme (Template Matching) -> görüntü üzerinde bir şablonu aramak için kullanılır. (nyari objek di gambar.)
* çok fazla başarılı değildir. kalo nyari apel di kotak buah harus nyari gambar mask apel dulu buat di cari di gambarnya.
* Görüntü üzerinde aranacak şablon(yama-patch) dikdörtgen. Yoksa maske uygulanarak 
* 

