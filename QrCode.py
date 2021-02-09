import pyqrcode
import png
from pyqrcode import QRCode

QRstring = "https://chat.whatsapp.com/LRNSHkJWs3G3gwB4IfCLco"
url = pyqrcode.create(QRstring)
url.png('pqr.png' , scale=8)