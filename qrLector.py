import cv2

img = cv2.imread('qr1.png')
det = cv2.QRCodeDetector()
valorQRLeido, pts, st_code = det.detectAndDecode(img)

# Mostramos el valor del QR leído
print("El valor del QR leído es: ", valorQRLeido)