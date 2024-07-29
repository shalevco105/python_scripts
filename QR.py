import qrcode

# Define the vCard data
vcard_data = """
BEGIN:VCARD
VERSION:3.0
N:שלו כהן מורה פרטי
TEL:(+972) 524744470
END:VCARD
"""
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add vCard data to the QRCode object
qr.add_data(vcard_data)
qr.make(fit=True)

# Generate the image of the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("simple_contact_qr3.png")

print("Simpler QR code generated and saved as simple_contact_qr.png")