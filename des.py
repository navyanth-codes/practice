# Initial permutation table
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Final permutation table
FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

# Expansion table
E = [32, 1, 2, 3, 4, 5, 4, 5,
     6, 7, 8, 9, 8, 9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27,
     28, 29, 28, 29, 30, 31, 32, 1]

# S-boxes (substitution boxes)
S_BOX = [
    [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

# Permutation table for each round
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# Final permutation for keys
KP = [57, 49, 41, 33, 25, 17, 9, 1,
      58, 50, 42, 34, 26, 18, 10, 2,
      59, 51, 43, 35, 27, 19, 11, 3,
      60, 52, 44, 36, 63, 55, 47, 39,
      31, 23, 15, 7, 62, 54, 46, 38,
      30, 22, 14, 6, 61, 53, 45, 37,
      29, 21, 13, 5, 28, 20, 12, 4]

# Compression permutation for keys
CP = [14, 17, 11, 24, 1, 5, 3, 28,
      15, 6, 21, 10, 23, 19, 12, 4,
      26, 8, 16, 7, 27, 20, 13, 2,
      41, 52, 31, 37, 47, 55, 30, 40,
      51, 45, 33, 48, 44, 49, 39, 56,
      34, 53, 46, 42, 50, 36, 29, 32]

# Shifts for each round
SHIFT = [1, 1, 2, 2, 2, 2, 2, 2,
         1, 2, 2, 2, 2, 2, 2, 1]


# Initial permutation of the plaintext
def initial_permutation(plain_text):
    permuted_text = ""
    for i in IP:
        permuted_text += plain_text[i - 1]
    return permuted_text


# Final permutation of the ciphertext
def final_permutation(cipher_text):
    permuted_text = ""
    for i in FP:
        permuted_text += cipher_text[i - 1]
    return permuted_text


# Expansion permutation
def expansion_permutation(right_half):
    expanded_text = ""
    for i in E:
        expanded_text += right_half[i - 1]
    return expanded_text


# XOR operation
def xor(text1, text2):
    result = ""
    for i in range(len(text1)):
        result += str(int(text1[i]) ^ int(text2[i]))
    return result


# S-box substitution
def sbox_substitution(expanded_text):
    substituted_text = ""
    for i in range(8):
        row = int(expanded_text[i * 6] + expanded_text[i * 6 + 5], 2)
        col = int(expanded_text[i * 6 + 1:i * 6 + 5], 2)
        val = S_BOX[i][row][col]
        substituted_text += format(val, '04b')
    return substituted_text


# Permutation
def permutation(substituted_text):
    permuted_text = ""
    for i in P:
        permuted_text += substituted_text[i - 1]
    return permuted_text


# Key permutation
def key_permutation(key):
    permuted_key = ""
    for i in KP:
        permuted_key += key[i - 1]
    return permuted_key


# Compression permutation for keys
def compression_permutation(key):
    compressed_key = ""
    for i in CP:
        compressed_key += key[i - 1]
    return compressed_key


# Shift left operation
def shift_left(key, n):
    return key[n:] + key[:n]


# Generate subkeys
def generate_subkeys(key):
    key = key_permutation(key)
    subkeys = []
    left = key[:28]
    right = key[28:]
    for i in SHIFT:
        left = shift_left(left, i)
        right = shift_left(right, i)
        subkey = compression_permutation(left + right)
        subkeys.append(subkey)
    return subkeys


# DES encryption
def des_encrypt(plain_text, key):
    plain_text = initial_permutation(plain_text)
    subkeys = generate_subkeys(key)
    left_half = plain_text[:32]
    right_half = plain_text[32:]
    for i in range(16):
        expanded_text = expansion_permutation(right_half)
        xor_result = xor(expanded_text, subkeys[i])
        print(f"\nFor Round {i + 1}:")
        print(f"K + E(R) = {xor_result}\n")
        substituted_text = sbox_substitution(xor_result)
        print(f"S-Box output = {substituted_text}\n")
        permuted_text = permutation(substituted_text)
        temp = left_half
        left_half = right_half
        right_half = xor(temp, permuted_text)
        print(f"L + (f) = {right_half}\n")
        print(f"Round {i + 1} final output: {bin_to_hex(right_half + left_half)}")
    cipher_text = final_permutation(right_half + left_half)
    return cipher_text


# Convert hexadecimal to binary
def hex_to_bin(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(64)

# Convert binary to hexadecimal
def bin_to_hex(bin_string):
    return hex(int(bin_string, 2))[2:].zfill(16)


# Main function
if __name__ == "__main__":
    plain_text = input("Enter plaintext in hexadecimal: ")
    key = input("Enter key in hexadecimal: ")
    plain_text_binary = hex_to_bin(plain_text)
    key_binary = hex_to_bin(key)
    print("\n\nEncryption:")
    cipher_text_binary = des_encrypt(plain_text_binary, key_binary)
    cipher_text_hex = bin_to_hex(cipher_text_binary)
    print(f"Cipher text (hex):{cipher_text_hex.upper()}")
