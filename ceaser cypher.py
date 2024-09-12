alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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
restart = True

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



while restart:
 def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in original_text:
                output_text += letter
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cipher_text}")



 def decrypt(original_text,shift_amount):
    cipher_text = ""
    for letter in original_text :
        if letter not in original_text:
                output_text += letter

        shifted_position = alphabet.index(letter)- shift_amount
        cipher_text += alphabet[shifted_position]
        print(f"Here is the decoded result: {cipher_text}")
        if shifted_position >= 27:
            new_shifted_position = shifted_position-26
            cipher_text += alphabet[new_shifted_position]

 def ceaser():
    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    if direction == "decode":
        decrypt(original_text=text, shift_amount=shift)
    

    ceaser()

 
