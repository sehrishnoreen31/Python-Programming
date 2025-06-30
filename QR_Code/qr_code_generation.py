import qrcode
import qrcode.constants

# Text to QR Code
qr_1 = qrcode.make('This is a qr code')
print(type(qr_1))
qr_1.save('qr_1.png')

# using QRCode class
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data('This code is generated with QRCode class')
qr.make(fit=True)
qr_2 = qr.make_image(fill_color=(230, 100, 255), back_color='white')
qr_2.save('qr_2.png')


