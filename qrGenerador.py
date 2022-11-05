import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.clear()
data = "hola k hace"
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="#000000", back_color="white")
img.save('qr1.png')