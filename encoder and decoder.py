#encoder and decoder
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)


# Function to encrypt the text
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shifted_char = chr(((ord(char) - 97 + shift) % 26) + 97) if char.islower() else chr(((ord(char) - 65 + shift) % 26) + 65)
            # Preserve the case of the character after encryption
            encrypted_text += shifted_char if char.islower() else shifted_char.upper()
        else:
            encrypted_text += char  # Preserve non-alphabetic characters
    print("\nEncrypted text:", encrypted_text)

def decrypt(text,shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            shifted_char = chr(((ord(char) - 97 - shift) % 26) + 97) if char.islower() else chr(((ord(char) - 65 - shift) % 26) + 65)
            # Preserve the case of the character after encryption
            decrypted_text += shifted_char if char.islower() else shifted_char.upper()
        else:
            decrypted_text += char  # Preserve non-alphabetic characters
    print("\nDecrypted text:", decrypted_text)
a=True
while a==True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    if direction=="encode":
        encrypt(text,shift)
    else:
        decrypt(text,shift)
    
    ans=input("\nDo you want to continue 'Yes' or 'No': ").lower()
    if ans=='yes':
        a=True
    else:
        a=False
        print("GoodBye")