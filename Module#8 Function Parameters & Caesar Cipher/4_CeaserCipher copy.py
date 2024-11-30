alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt (text,shift):
    cipherText=""
    for i in text:
        position=alphabet.index(i)
        newPosition=position+shift
        cipherText+=alphabet[newPosition]
    print(f"The Encoded text is {cipherText}")

def decrypt (text,shift):
    cipherText=""
    shift=shift*-1
    for i in text:
        position=alphabet.index(i)
        newPosition=position+shift
        cipherText+=alphabet[newPosition]
    print(f"The Decoded text is {cipherText}")

# def cipher (text,shift,direction):
    # if(direction=="decode"):
    #     shift*=-1
    # cipherText=""
    # for i in text:
    #     position=alphabet.index(i)
    #     newPosition=position+shift
    #     cipherText+=alphabet[newPosition]
    # print(f"Here's the {direction}d result: {cipherText}")

endOfProgram=False
while(endOfProgram==False):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if(shift>25):
        shift=shift%25
    if(direction=='encode'):
        encrypt(text,shift)
    elif(direction=='decode'):
        decrypt (text,shift)
    # cipher(text,shift,direction)
    continuation=input("Do you want to continue? Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if(continuation=="no"):
        endOfProgram=True
        print(f"Goodbye!")
