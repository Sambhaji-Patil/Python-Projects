import qrcode

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
data = 'https://www.linkedin.com/in/sambhaji-patil05/'  # Add the link of the website (path of the webpage)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('test.png')
