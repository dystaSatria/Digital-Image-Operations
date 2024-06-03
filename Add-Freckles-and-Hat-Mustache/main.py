import cv2
from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

def detect_features(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    features = []
    
    for (x, y, w, h) in faces:
        face = img[y:y+h, x:x+w]
        roi_gray = gray[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        nose = nose_cascade.detectMultiScale(roi_gray, 1.3, 5)
        mouth = mouth_cascade.detectMultiScale(roi_gray, 1.3, 5)
        
        features.append({
            'face': (x, y, w, h),
            'eyes': eyes,
            'nose': nose,
            'mouth': mouth
        })
    return features
def add_freckles(img, features):
    for feature in features:
        x, y, w, h = feature['face']
        face = img[y:y+h, x:x+w]
        
        
        for i in range(50):  
            
            
            cx = np.random.randint(x + w//4, x + 3*w//4)
            cy = np.random.randint(y + h//3, y + 2*h//3)
            if 0 <= cx - x < w and 0 <= cy - y < h:  
                cv2.circle(face, (cx - x, cy - y), 1, (42, 42, 165), -1)
    return img



def add_hat_and_mustache(img, features):
    hat_img = cv2.imread('hat.png', -1)
    mustache_img = cv2.imread('mustache.png', -1)
    
    for feature in features:
        x, y, w, h = feature['face']
        
        
        hat_width = w
        hat_height = int(hat_width * hat_img.shape[0] / hat_img.shape[1])
        hat = cv2.resize(hat_img, (hat_width, hat_height))
        for i in range(hat_height):
            for j in range(hat_width):
                if hat[i, j][3] != 0:
                    img[y+i-int(0.4*h):y+i-int(0.4*h)+1, x+j:x+j+1] = hat[i, j, :3]
        
     
        if len(feature['mouth']) > 0:
            mx, my, mw, mh = feature['mouth'][0]
            mustache = cv2.resize(mustache_img, (mw, mh//2))
            for i in range(mh//2):
                for j in range(mw):
                    if mustache[i, j][3] != 0:
                        img[y+my+i+mh//2-int(0.1*h):y+my+i+mh//2-int(0.1*h)+1, x+mx+j:x+mx+j+1] = mustache[i, j, :3]
    
    return img

class FaceFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Filter Application")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 10), padding=10)
        
        self.frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.canvas = tk.Canvas(self.frame, width=600, height=400)
        self.canvas.grid(row=0, column=0, columnspan=3, pady=10)
        
        self.upload_button = ttk.Button(self.frame, text="Upload Image", command=self.upload_image, style="TButton")
        self.upload_button.grid(row=1, column=0, padx=10, pady=10)
        
        self.add_freckles_button = ttk.Button(self.frame, text="Add Freckles", command=self.add_freckles, style="TButton")
        self.add_freckles_button.grid(row=1, column=1, padx=10, pady=10)
        
        self.add_hat_and_mustache_button = ttk.Button(self.frame, text="Add Hat and Mustache", command=self.add_hat_and_mustache, style="TButton")
        self.add_hat_and_mustache_button.grid(row=1, column=2, padx=10, pady=10)
        
        self.image = None
        self.processed_image = None
    def __init__(self, root):
        self.root = root
        self.root.title("Face Filter Application")
        self.root.geometry("400x200")
        self.root.resizable(True, True)
        
        self.canvas = tk.Canvas(self.root, width=400, height=200)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.upload_button = ttk.Button(self.root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack()
        
        self.add_freckles_button = ttk.Button(self.root, text="Add Freckles", command=self.add_freckles)
        self.add_freckles_button.pack()
        
        self.add_hat_and_mustache_button = ttk.Button(self.root, text="Add Hat and Mustache", command=self.add_hat_and_mustache)
        self.add_hat_and_mustache_button.pack()
        
        self.image = None
        self.processed_image = None

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path)
            self.show_image(self.image)

    def show_image(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
        self.canvas.image = img_tk

    def add_freckles(self):
        if self.image is not None:
            features = detect_features(self.image)
            self.processed_image = add_freckles(self.image.copy(), features)
            self.show_image(self.processed_image)

    def add_hat_and_mustache(self):
        if self.image is not None:
            features = detect_features(self.image)
            self.processed_image = add_hat_and_mustache(self.image.copy(), features)
            self.show_image(self.processed_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceFilterApp(root)
    root.mainloop()
