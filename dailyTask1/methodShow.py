import cv2
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import filedialog

# Function to read images and display results
def process_image():
    # Open the selected image file using the dialog box
    filename = filedialog.askopenfilename(initialdir="/", title="Select Image File",
                                          filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"), ("All Files", "*.*")))
    # Read images using OpenCV
    img = cv2.imread(filename)
    
    kernel_size = int(e1.get())

    kernel_mean = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
    filtered_mean = cv2.filter2D(img, -1, kernel_mean)
    filtered_median = cv2.medianBlur(img, kernel_size)
    filtered_gaussian = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
    filtered_bilateral = cv2.bilateralFilter(img, kernel_size, 75, 75)

    plt.subplot(2, 3, 1), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 2), plt.imshow(filtered_mean), plt.title('Mean Filter')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 3), plt.imshow(filtered_median), plt.title('Median Filter')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 4), plt.imshow(filtered_gaussian), plt.title('Gaussian Filter')
    plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 5), plt.imshow(filtered_bilateral), plt.title('Bilateral Filter')
    plt.xticks([]), plt.yticks([])
    plt.show()


def exit_program():
    window.destroy()

window = Tk()
window.title("4 yumuşatma(filtreleme) gostermesi")

btn_browse = Button(window, text="Gozat", command=process_image)
btn_browse.pack(pady=10)

lbl1 = Label(window, text="Kernel Size:")
lbl1.pack(padx=100,pady=50)
e1 = Entry(window)
e1.insert(END, '3')
e1.pack(padx=100,pady=50)

btn_exit = Button(window, text="Exit", command=exit_program)
btn_exit.pack(padx=20,pady=10)

window.mainloop()

