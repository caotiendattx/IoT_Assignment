import uuid
import qrcode

def get_mac_address():
    mac = uuid.getnode()
    mac_address = ':'.join(['{:02x}'.format((mac >> elements) & 0xff) for elements in range(0,12,2)])
    return mac_address

def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('./assets/MAC_Address_QR.png')
