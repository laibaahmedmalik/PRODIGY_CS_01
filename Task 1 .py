def caesar_cipher(text, shift):
    result = ""

    
    for j in range(len(text)):
        char = text[j]

        
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        else:
            result += char

    return result

text = input("Enter : ")
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Encrypted text:", encrypted_text)

text = encrypted_text
shift = -3
decrypted_text = caesar_cipher(text, shift)
print("Enter : ", text)
print("Decrypted text:", decrypted_text)
