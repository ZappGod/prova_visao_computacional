import cv2
import os

# caminho das imagens
imgs = "./img"
# Tamanho para redimensionar as imagens
img_size = (128, 128)

# caminhar pelo arquivo pegando as imagens
for img in os.listdir(imgs):
    caminho_imgs = os.path.join(imgs, img)
    
    img = cv2.imread(caminho_imgs, cv2.IMREAD_GRAYSCALE)
    
    img = cv2.resize(img, img_size)
    
    img = cv2.GaussianBlur(img, (5, 5), 0)
    
    img = cv2.equalizeHist(img)