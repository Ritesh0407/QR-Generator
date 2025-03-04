import qrcode as qr
from PIL import Image
qrr=qr.QRCode(version=1,
              error_correction=qr.constants.ERROR_CORRECT_H,
              box_size=10,border=4,)
qrr.add_data("https://www.instagram.com/tushar_swain_/")
qrr.make(fit=True)
img=qrr.make_image(fill_color="orange",back_color="blue")
img.save("land.png")
