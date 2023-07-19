#######################################
#FERNANDO E. AMADO-PUPO UFID 3225-2864#
#######################################




def encode(pwd):
    out = ""
    for dig in pwd:
        out += str((int(dig)+3)%10)
    return out


#Eric Fontes code
def decode(pwd):
    return ""

def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def main():

    toggle = True
    password = ""
    while toggle:
        print_menu()

        option = int(input("Please enter an option: "))

        if option == 1:

            password = encode(input("Please enter your password to encode: "))

            print("Your password has been encoded and stored")

        elif option == 2:

            tmp = password
            password = decode(password)

            print(f"The encoded password is {tmp}, and the original password is {password}")

            del tmp

        elif option == 3:
            break

        #debug option
        elif option  == 4:
            print(password)

        print()


main()



