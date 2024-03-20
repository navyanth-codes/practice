def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
def encrypt(plain_text, pb, qb, eb):
    n = pb * qb
    phi_n = (pb - 1) * (qb - 1)
    db = modinv(eb, phi_n)
    encrypted_text = [(char ** eb) % n for char in plain_text]
    return encrypted_text, db, n
def decrypt(encrypted_text, db, n):
    decrypted_text = [(char ** db) % n for char in encrypted_text]
    return decrypted_text
letter_to_number = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,'t': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
plain_text = input("Enter the plain text: ").lower()
pb = int(input("Enter the large prime number pb: "))
qb = int(input("Enter the large prime number qb: "))
eb = int(input("Enter the private key eb: "))
plain_text_numbers = [letter_to_number[char] for char in plain_text]
encrypted_text, db, n = encrypt(plain_text_numbers, pb, qb, eb)
print("Encrypted text:", encrypted_text)
print("Bob's private key (db):", db)
decrypted_text = decrypt(encrypted_text, db, n)
number_to_letter = {v: k for k, v in letter_to_number.items()}
decrypted_text_letters = [number_to_letter[num] for num in decrypted_text]
decrypted_text_str = ''.join(decrypted_text_letters)
print("Decrypted text:", decrypted_text_str)