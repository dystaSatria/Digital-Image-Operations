# Final Summary 

## Threshold (9th Week)

### Adaptif Esikleme 

```python
cv2.AdaptiveThreshold(src, dst, maxValue, adaptive_method=CV_ADAPTIVE_THRESH_MEAN_C, thresholdType=CV_THRESH_BINARY, blockSize=3, param1=5)

```

### otsunun ikilestirmesi(Binarization)
* Kami menggunakan nilai yang dipilih secara acak sebagai nilai ambang batas global. Tapi dengan Otsu Yontemiyle gerek kalmaz.
* Otsu metodu, goruntu histogramindan optimal bir global eşik değeri beliler.

### Şablon Eşleştirme
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
<br>
<br>
<br>
<br>
<br>

## Bilgi Cikarma(10th Week)
### Sınır Çizgileri (Contours)
* Sınır çizgilerini tespit etmek için ise OpenCVde findContours() fonksiyonunu kullanılabilir
* Kontürler, aynı renk veya yoğunluğa birleştiren bir eğri olarak açıklanabilir.
* Konturlar şekil analizi ve nesne algılama ve tanıma için kullandi.
* Daha doğru sonuçlar için ```ikili(binary) görüntüler``` kullanılmalıdır. O yuzden kontur bulmadan once ```esikleme ``` veya ```Canny``` bulma algortimasi uygulanacak.
* Kontur bulmak icin de arka plani ```siyah``` yada ```beyaz``` olmasi lazim.  

### findContours() fonksiyonu 
* Bu fonksyonu 3 arguman olmasi lazim : Kaynak goruntu, Kontur alma Metotu, Kontur yaklasim metot.
* 
```python
countors,hierracy = cv.findCoutours(image,mode,method[,countors[,hierarrcy[,offset]]] )

```
* Ciktisi kontorler ve hiyerasidir.
* Kontorler -> python listesi olarak dondurur. (x,y) koordinatlari iceren bir Numpy dizisidir.
* Hiyerasi -> toplojisi hakkinda bilgi istege bagli cikti vektorudur. icice bulanan kontor durumlarda kullanabilir.
* Islem uygulama mode :
<a data-flickr-embed="true" href="https://www.flickr.com/photos/197661703@N05/52953609410/in/dateposted-public/" title="Screenshot (603)"><img src="https://live.staticflickr.com/65535/52953609410_222392b79c_o.png" width="1075" height="256" alt="Screenshot (603)"/></a>
* Kontur kestirim Mode :
<a data-flickr-embed="true" href="https://www.flickr.com/photos/197661703@N05/52953381814/in/dateposted-public/" title="Screenshot (605)"><img src="https://live.staticflickr.com/65535/52953381814_c06d56e8a0_o.png" width="1055" height="220" alt="Screenshot (605)"/></a>
* (x, y) koordinat noktaları şeklinde saklanır. 
* CHAIN_APPROX_NONE iletirseniz , tüm sınır noktaları saklanır. Ornek dikdortgen sinir cizerken 734 nokta icerir.
* CHAIN_APPROX_SIMPLE bunu yapar. Tüm gereksiz noktaları kaldırır ve konturu sıkıştırır, böylece bellek tasarrufu sağlar.Ornek dikdortgen sinir cizerken sadece 4 nokta gosterilmektedir.
* Sinir Cizgi buluduktan sonra ```drawContours``` kullanabilirsiniz
```python
image = cv.drawCountours(image,countours,contourldx,color[,thickness[,lineType,[,hierarcy[,maxLevel[,offset]]]]])
```
* 
```python 
img = cv.drawCountours(img,countours,-1, (0,255,0),3) 
``` 
 -1 demek kontoru cizmek. Tum konturlari cizmek icin -1 kullanir. 3 demek renk kaliniktir.
 
 
 ### hsvSeg.pdf
 * Renk aralığı ile Bölütleme openCVde ```cv2.inRange()``` kullanilir.
 * Rengi bolutlemek icin istenilen rengin acik-koyu islem yapmak gerekir.

 ### renkUzay.pdf
* Renk uzayları renkleri tanımlamak için kullanılan matematiksel modellerdir.
* Renk uzayları 3D olarak tasarlanır. Cunku Renkmetri olustururan grassmanin birinci kanuna gore rengi icin 3 degisken gerekir.
* 20 den fazla renk uzayi bulunmaktadir bugunki.
* renk uzayına doğrusal ya da doğrusal olmayan yöntemlerle dönüşüm yapılabilmelidir
* Renk uzayları cihaz bagimli ve bagimsiz renk uzaylari iki gruba ayrilir.
* cihaz bagimli ozelliklerine bagli olarak uretilir.
* cihaz bagimsiz renk uzaylari CIE tarafindan ve butun renkler renk olcumunu saglayan renkmetride kullanilan uzaydir.
* RGB Renk uzayi 2 -> 0-255 ; siyah (0,0,0); beyaz (255,255,255)
* red (255,0,0); cyan(0,255,255); green (0,255,0); Magenta (255,0,255); gray(128,128,128) ; blue(0,0,255); yellow (255,255,0)
* CMYK Renk Uzayı -> Cyan, Magenta, Yellow, and Key (black).
* ```CMYK renk uzayı çıkarmalı``` ```renk karışım yöntemi yardımıyla``` birim küpte kullanilir.
*  Camgöbeği, galibarda, sarı ve siyah renk uzayının eksenleridir.
* Çıkarmalı denmesinin sebebi beyaz ışıktan kırmızı, yeşil, mavi renklerini cikarmasini dolayidir. beyaz-isik-kirmizi(cyan).beyaz-isik-yesil(magenta). beyaz-isik-mavi(yellow).
* Siyah rengi bu 3 renk ile oluşturmak çok maliyetli o yuzden siyah mürekkep ayrıca yazıcılarda bulunur.
* YCbCr/ / YUV Renk Uzayı ->  yeğinlik(parlaklık) değerinin renk değerlerinden ayrılması hedeflenmiştir cunku RGB yetersiz.
* YCbCr Renk Uzayı digital videolarda kullanilir. Y(Parlaklık(Luminance)luminance/parlaklik sinyal).Cr(chroma blue minus luma/chrominance renk bilgi). Cb(Chroma red minus luma/ chrominance renk bilgi).
* Y, 8 bitliklik 16-235 aralığında tanımlanmaktadır. Cb ve Cr 16-240 arasinda tanamlanmaktadir.
* HSV Renk Uzayı inSAN gorme en yakin renk uzaydir. HSV Hue, Saturation, Value yani renk özü, doygunluk ve parlaklık olarak adlandırılmıştır.
* Renk özü (Hue) -> rengin baskın dalga uzunluğunu belirler.
*  Doygunluk(Saturation), rengin "canlılığını" belirler.
* Yüksek doygunluk -> canli renk . düşük olasılık -> gri tonlarına.

### waterched.pdf
* Görüntü Bölütleme -dijital bir görüntüyü birden çok bölüme(parca,segment) ayirma islemidir.
* daha fazla analiz icin nesneleri goruntuden cikmamizi yardimci oluruz.
* bolutleme dogrulugu gorntu analiz basarli yada basarisizligi belirler.
* görüntü segmentasyonu, görüntüdeki ilgilenilen her nesne için bize o nesne hakkında daha fazla bilgi sağlayan piksel bazında bir maske oluşturmaktadı.
* Waterched algoritma ile bolutleme en populer yontemlerdir.

   
