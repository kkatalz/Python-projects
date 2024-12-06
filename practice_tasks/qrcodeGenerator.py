import qrcode

def generateQRCode(site, fileName):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(site)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(fileName)
    print(f"QR code saved as {fileName}")

def main():
    # https://codewithmosh.com is the website
    website = input("Enter the website: ").strip()
    fileName = input("Enter the file name: ").strip()
    generateQRCode(website, fileName)

main()
