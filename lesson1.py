

"""
Matnni Kodlash va Dekodlash (Encoding and Decoding):

Python tilida, matnni kodlash va dekodlash uchun quyidagi usullar keng qo'llaniladi:

Base64:

Kodlash: base64.b64encode(data)
Dekodlash: base64.b64decode(encoded_data)
Misol:
"""
import base64

text = "Hello, World!"
encoded_data = base64.b64encode(text.encode('utf-8'))
decoded_data = base64.b64decode(encoded_data).decode('utf-8')

print(f"Original Text: {text}")
print(f"Encoded Text: {encoded_data}")
print(f"Decoded Text: {decoded_data}")
