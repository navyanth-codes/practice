def generate(string,key):
    key=list(key)
    if string == key:
        return key
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i%len(key)])
    return ''.join(key)
def cipher_text(string,key):
    cipher_text=[]
    for i in range(len(string)):
        x=(ord(string[i])+ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ''.join(cipher_text)
def original_text(cipher_text,key):
    original_text=[]
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i])-ord(key[i])) % 26
        x += ord('A')
        original_text.append(chr(x))
    return ''.join(original_text)
if __name__ == "__main__" :
    string = input("enter the text :").upper()
    keyword = input("enter the key word").upper()
    key=generate(string,keyword)
    cipher_text=cipher_text(string,key)
    print("ciphertext :",cipher_text)
    print("originaltext:",original_text(cipher_text,key))       