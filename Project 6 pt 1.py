# Luis Sprung
# COP3502 Programming Fundamentals 1
# UFID: 91487486 

# Encoding and decoding functions #
def encode(password):
    enc_password = ""
    for char in password:
        enc_char = str((int(char) + 5) % 10)
        enc_password += enc_char
    return enc_password

def decode(enc_password):
    dec_password = ""
    for char in enc_password:
        dec_char = str((int(char) - 5) % 10)
        dec_password += dec_char
    return dec_password

# Main functioning code #
def main():
    print("Menu\n-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    
# Menu options #
    option = int(input("\nPlease enter an option: "))
    if option == 1:
        password = input("Please enter your 8-digit password to encode: ")
        print("Your encoded password is:", encode(password))
        print()
        main()

    elif option == 2:
        enc_password = input("Please enter your previously encoded 8-digit password: ")
        print("Your decoded password is:", decode(enc_password))
        print()
        main()

    elif option == 3:
        quit

    else:
        print("Invalid option, Try again.")
        main()

if __name__ == "__main__":
    main()