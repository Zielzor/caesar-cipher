import ceaser_cipher_data as ccd

print(ccd.logo)
alphabet = ccd.alphabet


def encrypt(text, shift):
    encrypted_text = ""
    for t in text:
        if t in alphabet:
            encrypted_text += alphabet[alphabet.index(t) + 1]
        else:
            encrypted_text += t

    print(encrypted_text)


def decrypt(de_string, shift):
    decrypted_text = ""
    for ds in de_string:
        if ds in alphabet:
            decrypted_text += alphabet[alphabet.index(ds) - 1]
        else:
            decrypted_text += ds

    print(decrypted_text)

run = True
while run == True:
    text = str(input("Enter message \n:>"))
    text = text.lower()
    shift = int(input("Enter shift number \n:>"))

    if shift > len(ccd.alphabet):
        print("Shift out of range")
        shift = int(input("Enter shift number \n:>"))
    else:
        pass

    direction = str(input("You wish to encrypt or decrypt? \n:>"))
    direction = direction.lower()

    if direction == "encrypt" or direction == "e":
        encrypt(text, shift)
    elif direction == "decrypt" or direction == "d":
        decrypt(text, shift)

    continuity = str(input("Do you wish to continue? Y/N \n:>"))
    continuity = continuity.lower()
    if continuity != "Y":
    	run = False
        


