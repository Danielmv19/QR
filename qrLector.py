from pyzbar import pyzbar
from PIL import Image

image = Image.open('qr1.png')
qr_code = pyzbar.decode(image)[0]

# convert into string
data = qr_code.data.decode('utf8').encode('shift-jis').decode('utf-8')
print("El mensaje es: ", data)