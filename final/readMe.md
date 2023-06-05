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
* Nasil Calisir: Eşleşen alanı tanımlamak için , şablon görüntüsünü kaydırarak kaynak görüntüyle karşılaştırmamız gerekir sonra Şablon görüntüsünü giriş görüntüsünün üzerine kaydırır giriş görüntüsünün o bölümünü şablon ile karşılaştırır. her seferinde 1 px hareket ettirilir. Soldan sağa, yukarıdan aşağıya. ne kadar iyi yada kötü olduğunu gösterecek bir metrik(ölçü) tanımlanır. I üzerinde T’nin her konumu için R sonucu saklanir. En parlak yer, en yüksek eşleşmeyi gösterir
* TM_CCORR_NORMED -> R sonucu gostermektedir.
* Şablon eşleştirme için matchTemplate() fonksiyonu kullanılır 
```python
result = cv.matchTemplate(image, templ, method[, result[,mask]])
```
* TM_SQDIFF kullanıldığında minimum değer
* TM_CCORR ve TM_CCOEFF -> maximum deger

<a data-flickr-embed="true" href="https://www.flickr.com/photos/197661703@N05/52952674020/in/dateposted-public/" title="Screenshot (601)"><img src="https://live.staticflickr.com/65535/52952674020_9187beee69_o.png" width="596" height="479" alt="Screenshot (601)"/></a>
<a data-flickr-embed="true" href="https://www.flickr.com/photos/197661703@N05/52952674000/in/dateposted-public/" title="Screenshot (600)"><img src="https://live.staticflickr.com/65535/52952674000_b32031147b_o.png" width="590" height="529" alt="Screenshot (600)"/></a>
* Kalo ngitung bola make threshold() soalnya bola lingkaran jadi harus di filter mask dulu baru bisa ditemuin.

