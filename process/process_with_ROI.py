import cv2
import numpy as np
import pytesseract
from pytesseract import Output



# Carrega a imagem
img = cv2.imread('dataset/fiesta-noite(1).jpeg')

# Converte a imagem para tons de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplica a detecção de bordas usando o algoritmo Canny
edged = cv2.Canny(gray, 30, 200)

# Encontra os contornos na imagem
contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Ordena os contornos de acordo com a área, do maior para o menor
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

# Itera sobre os contornos e identifica o retângulo que envolve a placa do carro
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    
    # A placa do carro tem geralmente quatro lados
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(contour)
        roi = img[y:y+h, x:x+w]  # Extrai a ROI
        
        # Desenha o retângulo ao redor da placa
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        break  # Para a iteração quando a placa for encontrada

# Exibe a imagem com a ROI identificada
cv2.imshow("ROI", roi)


myconfig = r"--psm 6 --oem 3"

width, height, _ = roi.shape
# print(width,height)

data = pytesseract.image_to_data(roi, config=myconfig, output_type=Output.DICT)
print(data['conf'])
print(data['text'])
boxes = len(data['text'])

for i in range(boxes):
    if float(data['conf'][i]) > 60:
        (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        imgB = cv2.rectangle(roi, (x,y), (x+width, y+height), (0,255,0), 2)
        imgB = cv2.putText(imgB, data['text'][i], (x, y+height+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2, cv2.LINE_AA)

cv2.imshow("img", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()