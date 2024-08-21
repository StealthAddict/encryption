import vigenere
import a1z26
import nihilist



# HELPERS


def invalid_input():
    print("\nInvalid input. Try again")

"""
    enc_dec returns a number according to
    the user's desired experience.
"""
def enc_dec():
    # TODO: change this to be a string of inputs, -e/-d -f/-m -f/-c
    print("ENCRYPTION & INPUT TYPE")
    print("\tE = Encrypt | D = Decrypt\n\n\t(#) E/D | Input  | Output\n\t-------------------------")
    print("""\t(0)  E  | File   | File \n\t(1)  E  | File   | Console 
    \t(2)  E  | Manual | File \n\t(3)  E  | Manual | Console 
    \t(4)  D  | File   | File \n\t(5)  D  | File   | Console 
    \t(6)  D  | Manual | File \n\t(7)  D  | Manual | Console """)
    return input()


def handle_input_output():
    # I/O choice
    res = enc_dec()
    if res == '-1':
        return 0
    
    # Return file if file input requested
    usr_inp = ""
    if res == '0' or res == '1' or res == '4' or res == '5':    # File Input
        usr_inp = None

        while usr_inp == None:
            f_read = input("\nINPUT FILE TO READ: ")
            try: 
                usr_inp = open(f_read, 'r')
            except FileNotFoundError:
                invalid_input()
        usr_inp = usr_inp.read()
    elif res == '2' or res == '3' or res == '6' or res == '7':  # Manual Input
        usr_inp = input("\nINPUT: ")

    # Return file if file output requested
    usr_outp = None
    if res == '0' or res == '2' or res == '4' or res == '6':    # File Output
        while usr_outp == None:
            f_write = input("INPUT FILE TO WRITE: ")
            try:
                usr_outp = open(f_write, 'w')
            except FileNotFoundError:
                invalid_input()

    return res, usr_inp, usr_outp


def vigenere_choice():

    print("\n--- VIGENERE CIPHER ---\n")
    res, usr_inp, usr_outp = handle_input_output()

    # Perform (en/de)cryption actions
    key = input("KEY: ")

    cipher = vigenere.Vigenere(key, usr_inp)
    
    if res == '0' or res == '1' or res == '2' or res == '3':
        if usr_outp == None:
            print("ENCRYPTED TEXT:\n", cipher.encrypt())
        else:
            usr_outp.write(cipher.encrypt())
        
    elif res == '4' or res == '5' or res == '6' or res == '7':
        if usr_outp == None:
            print("DECRYPTED TEXT:\n", cipher.decrypt())
        else:
            usr_outp.write(cipher.decrypt())

    return 0


def a1z26_choice():
    print('\n--- A1Z26 ---\n')
    res, usr_inp, usr_outp = handle_input_output()

    # request salt
    salt = input("SALT (optional): ")

    cipher = a1z26.A1Z26(salt)

    # Perform 'cryption actions    
    if res == '0' or res == '1' or res == '2' or res == '3':
        cipher_encrypted = cipher.encrypt(usr_inp)
        if usr_outp == None:
            print("ENCRYPTED TEXT:\n", cipher_encrypted)
        else:
            usr_outp.write(cipher_encrypted)
        
    elif res == '4' or res == '5' or res == '6' or res == '7':
        cipher_decrypted = cipher.decrypt(usr_inp)
        if usr_outp == None:
            print("DECRYPTED TEXT:\n", cipher_decrypted)
        else:
            usr_outp.write(cipher_decrypted)

    return 0

def nihilist_choice():
    print('\n--- NIHILIST CIPHER ---\n')
    res, usr_inp, usr_outp = handle_input_output()

    # Request keys
    poly_key = input("POLYBIUS KEY (optional): ")
    nihil_key = input("KEY: ")

    cipher = nihilist.Nihilist(poly_key, nihil_key)

    # Perform 'cryption actions    
    if res == '0' or res == '1' or res == '2' or res == '3':
        cipher_encrypted = cipher.encrypt(usr_inp)
        if usr_outp == None:
            print("ENCRYPTED TEXT:\n", cipher_encrypted)
        else:
            usr_outp.write(cipher_encrypted)
        
    elif res == '4' or res == '5' or res == '6' or res == '7':
        cipher_decrypted = cipher.decrypt(usr_inp)
        if usr_outp == None:
            print("DECRYPTED TEXT:\n", cipher_decrypted)
        else:
            usr_outp.write(cipher_decrypted)


# MAIN
def main():
    menu = """\nChoose your encryption method:
    \tAscii (a)\n\tA1Z26 (z)\n\tNihilist (n)\n\tVigenere (v)\n"""

    enc_choice = input(menu).lower()
    print("\n")

    while True:

        if enc_choice == 'q':
            break
        elif enc_choice == 'v':
            vigenere_choice()
        elif enc_choice == 'a':
            # Ascii
            print("Not implemented.\n")
        elif enc_choice == 'z':
            a1z26_choice()
        elif enc_choice == 'n':
            nihilist_choice()

            

        enc_choice = input(menu).lower()

        


# MAIN CALLER
if __name__ == "__main__":
    main()