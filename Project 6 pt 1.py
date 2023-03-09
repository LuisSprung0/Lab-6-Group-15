global encoded_pass
encoded_pass = 0

def menu_Option(num):
    global password_inp
    global encoded_pass
    if num == 1:
        password_inp = int(input('Please enter your password to encode: '))
        encoded_pass = (password_inp*2)^2 + 6
        print('Your password has been encoded and stored!')

    elif num == 2:
        pass

    elif num == 3:
        quit


def main():
    print("Menu" 
          + "\n-------------" 
          + "\n1. Encode\n2. Decod\n3. Quit") 
    num = int(input('\nPlease enter an option: '))
    menu_Option(num)

if __name__ == '__main__':
    main()