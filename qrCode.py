#to create the QRCode
import qrcode

img = qrcode.make("TESTE")
img.save("mycode.png")
