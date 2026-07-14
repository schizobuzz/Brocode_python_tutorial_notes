import random
import string

#   Defines the list of chars and the secret key used to decipher
chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()
random.shuffle(key) #Because of this the key is shuffled every time the program is ran aka no decryption after the key is lost

#   ENCRYPTION
def encryption():
    plaintext = input("Enter a message to encrypt: ")
    ciphertext = ""

    for letter in plaintext:
        index = chars.index(letter)
        ciphertext += key[index]

    print(f"Your ciphertext is: {ciphertext}")

#   DECRYPTION
def decryption():
    ciphertext = input("Enter a message to decrypt: ")
    plaintext = ""

    for letter in ciphertext:
        index = key.index(letter)
        plaintext += chars[index]

    print(f"Your plaintext is: {plaintext}")

def main():
    is_running = True

    while is_running:
        print("\n################")
        print("Cipher Program.")
        print("################")
        print("1) to encrypt")
        print("2) to decrypt")
        print("q) to quit \n")
        choice = input("Enter your option: ")
        print()

        match choice:
            case '1':
                encryption()
            case '2':
                decryption()
            case 'q':
                print("Exiting...Have a great day :) \n")
                is_running = False
            case _:
                print("Please enter a valid choice.")
                continue

        # if choice == '1':
        #     encryption()
        # elif choice == '2':
        #     decryption()
        # elif choice == 'q':
        #     print("Exiting...Have a great day :) \n")
        #     is_running = False
        # else:
        #     print("Please enter a valid choice.")
        #     continue

if __name__ == '__main__':
    main()