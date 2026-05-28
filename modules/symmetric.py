import os
import base64

from utils.display import print_header, print_result, print_separator
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# ─────────────────────────────────────────────────────
# Symmetric LAB - Main Menu
# ─────────────────────────────────────────────────────
def symmetric_lab():
    # sub menu with all 9 features
    is_running = True
    while is_running:
        print_header("SYMMETRIC ENCRYPTION LAB")
        print("\n  Select a feature:")
        print("  1. Key Generator (128, 192, 256)")
        print("  2. AES Encrypt (CBC Mode)")
        print("  3. AES Decrypt (CBC Mode)")
        print("  4. ECB Mode Vs CBC Comparision")
        print("  5. AES Modes Explorer (ECB, CBC, CTR, GCM)")
        print("  6. File Encryption & Decryption")
        print("  7. CMAC Generation & Verification")
        print("  8. HMAC Generation & Verification")
        print("  9. Authenticated Encryption (AES-GCM with auth tag)")
        
        print("  0. Back to Main Menu")
        print_separator()

        choice = input("  Enter your choice: ")

        if choice == "1":
            key_generator()
        elif choice == "2":
            aes_cbc_encryption()
        elif choice in ["3", "4", "5", "6", "7", "8", "9"]:
            print("\n  This module is coming soon. Stay tuned.")
        elif choice == "0":
            is_running = False
        else:
            print("\n  Invalid choice. Try again.")

# ─────────────────────────────────────────────────────
# Feature 1 — Symmetric Key Generator
# ─────────────────────────────────────────────────────
def key_generator():
    print_header("SYMMETRIC KEY GENERATOR")
    print("  1. 128 bits")
    print("  2. 192 bits")
    print("  3. 256 bits")
    print("  0. Back to Main Menu")
    print_separator()
    keylength = input("  Select key size: ")

    key_options ={
        "1" : (16, 128),
        "2" : (24, 192),
        "3" : (32, 256)
    }

    if keylength in key_options:
        size_bytes, size_bits = key_options[keylength]
        key = os.urandom(size_bytes)
        print_result("Key Size", f"{size_bits} bits")
        print_result("Key (Hex)", key.hex())
        key_path = f"output/keys/symmetric_key_{size_bits}.key"
        with open(key_path, "wb") as f:
            f.write(key)
        print_result("Saved to", key_path)
    elif keylength == "0":
        return
    else:
        print("\n  Invalid choice. Try again.")

    print_separator() 

# ─────────────────────────────────────────────────────
# Feature 2 — AES - CBC Encryption
# ─────────────────────────────────────────────────────
def aes_cbc_encryption():
    print_header("AES CBC ENCRYPTION")
    plain_text = input("  Enter text to encrypt: ")

    print("  1. 128 bits")
    print("  2. 192 bits")
    print("  3. 256 bits")
    print("  0. Back to Main Menu")
    print_separator()

    key_choice = input("  Select key size: ")
    key_options = {
        "1": 128,
        "2": 192,
        "3": 256
    }

    # Load key from file
    if key_choice in key_options:
        key_bits = key_options[key_choice]
        try:
            with open(f"output/keys/symmetric_key_{key_bits}.key", "rb") as f:
                key = f.read()

        except FileNotFoundError:
            print(f"\n  Key not found. Please generate a {key_bits}-bit key first.")
            return
        # Generate IV 
        iv = os.urandom(16)
        iv_path = "output/keys/iv_key.key"
        with open(iv_path, "wb") as f:
            f.write(iv)

        # Create the padding object
        padder = padding.PKCS7(128).padder()
        # Actually Pad the plain text
        padded_text = padder.update(plain_text.encode()) + padder.finalize()

        # Create the cipher engine
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        # Get encryptor from cipher. cipher object can do both encrypt and decrypt
        encryptor = cipher.encryptor()

        # Encrypt
        cipher_text = encryptor.update(padded_text) + encryptor.finalize()

        # Base64 encode output 
        cipher_text_b64 = base64.b64encode(cipher_text).decode()

        # Display result 
        print_result("Original Text", plain_text)
        print_result("Encrypted (B64)", cipher_text_b64)
        print_result("IV (Hex)", iv.hex())
        print_result("Key Size", f"{key_bits} bits")
        print_result("Saved to", iv_path)

    elif key_choice == "0":
        return
    else:
        print("\n  Invalid choice. Try again.")
        return
    print_separator()
    print("\n  Note: Use IV and same key size in Feature 3 to decrypt.")
