import random
import string

chars = string.punctuation + string.digits + string.ascii_letters + " "
chars = list(chars)
choise=input("type e or encrypt or d to decrypt: ").lower()

#encrypt
if choise == "e":
    random.seed(input("enter a password: "))
    plain_text=input("enter a massage to encrypt: ")
    key = chars.copy()
    random.shuffle(key)
    print()
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]
    print(f"original massage: {plain_text}")
    print(f"encrypted message: {cipher_text}")

#decrypt
elif choise == "d":
    random.seed(input("enter a password: "))
    cipher_text=input("enter a massage to decrypt: ")
    key = chars.copy()
    random.shuffle(key)
    print()
    plain_text = ""
    for letter in cipher_text:
       index=key.index(letter)
       plain_text += chars[index]
    print(f"encrypted message: {cipher_text}")
    print(f"decrypted message: {plain_text}")