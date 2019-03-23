import pyperclip, sys, random

 

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
          #'QWERTYUIOPASDFGHJKLZXCVBNM
def main():

    myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'   
    myKey = 'QWERTYUIOPASDFGHJKLZXCVBNM'

    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'



    



    if myMode == 'encrypt':

        translated = encryptMessage(myKey, myMessage)

    elif myMode == 'decrypt':
        print("yes") 
        translated = decryptMessage(myKey, myMessage)

    print('Using key ' ,myKey)

    print('The  message is:' ,myMode)
    print(translated)

    pyperclip.copy(translated)

    print()

    print('This message has been copied to the clipboard.')








def encryptMessage(key, message):

    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):

    return translateMessage(key, message, 'decrypt')





def translateMessage(key, message, mode):

    translated = ''

    charsA = LETTERS

    charsB = key
    #print("y",charsB)
    if mode == 'decrypt':
        charsA, charsB = charsB, charsA
        #print("z",charsA)
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    return translated



#return translated



if __name__ == '__main__':

    main()
