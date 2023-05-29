import cv2
import glob

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')

filenames = glob.glob("Picture/Face6.jpg")
filenames.sort()
images = [cv2.imread(img) for img in filenames]

for img in images:
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex, ey),(ex + ew,ey + eh),(0, 255, 0),2)

		mouth = mouth_cascade.detectMultiScale(roi_gray)
		for (ex, ey, ew, eh) in mouth:
			cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
			break

		noses = nose_cascade.detectMultiScale(roi_gray)
		for (ex, ey, ew, eh) in noses:
			cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
			break

	cv2.imwrite("Pic6.jpg", img)
	cv2.waitKey(0)

cv2.destroyAllWindows()
