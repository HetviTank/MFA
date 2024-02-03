import time
import pyotp
import qrcode

key = "your_key"
uri = pyotp.totp.TOTP(key).provisioning_uri(name="aexample.com", issuer_name="username")
print(uri)
qrcode.make(uri).save("qr.png")