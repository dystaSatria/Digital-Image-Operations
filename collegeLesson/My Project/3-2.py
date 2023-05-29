import cv2

img = cv2.imread("Picture\Fam3.jpeg")
glasses = cv2.imread('glasses-removebg-preview.png')
hat = cv2.imread('hat-removebg-preview.png')
face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = face_classifier.detectMultiScale(gray, 1.1, 5)
for (x, y, w, h) in face:
    if h > 0 and w > 0:
        h, w = int(0.3 * h), int(0.77 * w)
        y += 35
        x -= -20
        img_roi = img[y:y + h, x:x + w]

        glasses_small = cv2.resize(glasses, (w, h), interpolation=cv2.INTER_AREA)
        gray_mask = cv2.cvtColor(glasses_small, cv2.COLOR_BGR2GRAY)

        ret, mask = cv2.threshold(gray_mask, 244, 255, cv2.THRESH_BINARY_INV)
        mask_inv = cv2.bitwise_not(mask)
        masked_face = cv2.bitwise_and(glasses_small, glasses_small, mask)
        masked_frame = cv2.bitwise_and(img_roi, img_roi, mask_inv)
        img[y:y + h, x:x + w] = cv2.add(masked_face, masked_frame)

        h, w = int(2 * h), int(1.6 * w)
        y += -85
        x -= 20
        img_roi = img[y:y + h, x:x + w]

        glasses_small = cv2.resize(hat, (w, h), interpolation=cv2.INTER_AREA)
        gray_mask = cv2.cvtColor(glasses_small, cv2.COLOR_BGR2GRAY)

        ret, mask = cv2.threshold(gray_mask, 244, 255, cv2.THRESH_BINARY_INV)
        mask_inv = cv2.bitwise_not(mask)
        masked_face = cv2.bitwise_and(glasses_small, glasses_small, mask)
        masked_frame = cv2.bitwise_and(img_roi, img_roi, mask_inv)
        img[y:y + h, x:x + w] = cv2.add(masked_face, masked_frame)


cv2.imshow("img", img)
cv2.imwrite("Fam3.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
