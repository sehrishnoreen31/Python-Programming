import qrcode

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


# # another qrcode
# qr_code = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=8,
#     border=5
# )
# qr_code.add_data('A qr code')
# qr_code.make(fit=True)
# qr_3 = qr_code.make_image(fill_color=(255,255,230), back_color='white')
# qr_3.save('qr_3.png')


