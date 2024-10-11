import secrets
import qrcode

from io import BytesIO

def create_unique_key():
    return secrets.token_hex()



def qr(name:str):
    data = f"https://front-rho-gules.vercel.app/page/{name}"
    img = qrcode.make(data)
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    return buffer
