import cv2


input_image = cv2.imread("image.jpg")

mean_filtered = cv2.blur(input_image, (5, 5))


median_filtered = cv2.medianBlur(input_image, 5)


gaussian_filtered = cv2.GaussianBlur(input_image, (5, 5), 1.5)

bilateral_filtered = cv2.bilateralFilter(input_image, 5, 75, 75)


cv2.imshow("Input Image", input_image)
cv2.imshow("Mean Filtered Image", mean_filtered)
cv2.imshow("Median Filtered Image", median_filtered)
cv2.imshow("Gaussian Filtered Image", gaussian_filtered)
cv2.imshow("Bilateral Filtered Image", bilateral_filtered)
cv2.waitKey(0)
