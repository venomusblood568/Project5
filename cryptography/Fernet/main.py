#pip install cryptography 
from cryptography.fernet import Fernet

Key = Fernet.generate_key()

f = Fernet(Key)

text = input("enter the text you wanna encrypt: ")
# text.encode("utf-8") is for converting the str in bytes so it can be encrypted 
token = f.encrypt(text.encode("utf-8"))

print("text after encryption:",token)


decode_token = f.decrypt(token).decode("utf-8")

print("text after decryption:" ,decode_token)