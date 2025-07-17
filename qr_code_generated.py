import qrcode
data = input("Enter a text or URL: ")
file_name = input("Enter your file name: ")
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(file_name)
print(f"QR Code save as {file_name}")