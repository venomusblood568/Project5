# Import necessary libraries
import bcrypt
from cryptography.fernet import Fernet

# Function to generate a key for encryption and hash the password for comparison
def generate_key(password):
    # Generate a Fernet key for encryption
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    # Hash the password using bcrypt before saving it
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    # Save the key to a file for future use
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key, password_hash

# Function to load the encryption key from the file
def load_key():
    return open("key.key", "rb").read()

# Function to encrypt a message using the provided key
def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

# Function to decrypt an encrypted message using the provided key
def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

# Generate or load the encryption key and hashed password from user input
key, password_hash = generate_key(input("Enter the special password for encryption: "))

# Get the message from the user and encrypt it using the key
message = input("Enter the message to encrypt: ")
encrypted_message = encrypt_message(message, key)

# Get the password attempt for decryption from the user
password_attempt = input("Enter the special password for decryption: ")

# Check if the password attempt matches the stored password hash
if bcrypt.checkpw(password_attempt.encode(), password_hash):
    # If the password is correct, decrypt the message and print it
    decrypted_message = decrypt_message(encrypted_message, key)
    print("Decrypted message:", decrypted_message)
else:
    # If the password is incorrect, print an error message
    print("Incorrect password. Try again.")
