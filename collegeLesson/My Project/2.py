import cv2
import numpy as np
import matplotlib.pyplot as plt

threshold = 50

face = cv2.imread('Picture/kiz1.jpg')
hair_mask = np.where(face[:, :, 0] < threshold, 255, 0).astype(np.uint8)


coloredRedHairPicture = np.copy(face)
coloredGreenHairPicture = np.copy(face)
coloredYellowHairPicture = np.copy(face)
coloredPurpleHairPicture = np.copy(face)


redHair = [0, 0, 255]  
greenHair = [0, 255, 0]
yellowHair = [0,255,255]
purpleHair = [128, 0, 128]

coloredRedHairPicture[hair_mask == 255] = redHair
coloredGreenHairPicture[hair_mask == 255] = greenHair
coloredYellowHairPicture[hair_mask == 255] = yellowHair
coloredPurpleHairPicture[hair_mask == 255] = purpleHair

fig, ax = plt.subplots(1, 5, figsize=(12, 6))
ax[0].imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
ax[0].set_title('Asil Saci')
ax[1].imshow(cv2.cvtColor(coloredRedHairPicture, cv2.COLOR_BGR2RGB))
ax[1].set_title('Kirmizi Saci')
ax[2].imshow(cv2.cvtColor(coloredGreenHairPicture, cv2.COLOR_BGR2RGB))
ax[2].set_title('Yesil Saci')
ax[3].imshow(cv2.cvtColor(coloredYellowHairPicture, cv2.COLOR_BGR2RGB))
ax[3].set_title('Sari Saci')
ax[4].imshow(cv2.cvtColor(coloredPurpleHairPicture, cv2.COLOR_BGR2RGB))
ax[4].set_title('Mor Saci')
plt.show()
