import cv2

# Load the input image
input_image = cv2.imread("image.jpg")

# Apply mean filter with a kernel size of 5x5
mean_filtered = cv2.blur(input_image, (5, 5))

# Apply median filter with a kernel size of 5x5
median_filtered = cv2.medianBlur(input_image, 5)

# Apply Gaussian filter with a kernel size of 5x5 and sigma value of 1.5
gaussian_filtered = cv2.GaussianBlur(input_image, (5, 5), 1.5)

# Apply bilateral filter with a kernel size of 5x5, sigma color of 75, and sigma space of 75
bilateral_filtered = cv2.bilateralFilter(input_image, 5, 75, 75)

# Display the input and filtered images side by side
cv2.imshow("Input Image", input_image)
cv2.imshow("Mean Filtered Image", mean_filtered)
cv2.imshow("Median Filtered Image", median_filtered)
cv2.imshow("Gaussian Filtered Image", gaussian_filtered)
cv2.imshow("Bilateral Filtered Image", bilateral_filtered)
cv2.waitKey(0)
