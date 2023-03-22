# Sallie Zhou

# Lab Partner is Joanna Mijares

def encode(password):
    encoded_password = []
    final_encode = ""
    for digit in password:
        encoded_digit = int(digit) + 3
        encoded_password.append(encoded_digit)
    final_encode = "".join(str(digit) for digit in encoded_password)
    return final_encode


def decode(final_encode):
    decoded_password = []
    final_decode = ""
    for digit in final_encode:
        decoded_digit = int(digit) - 3
        decoded_password.append(decoded_digit)
    final_decode = "".join(str(digit) for digit in decoded_password)
    return final_decode


a = True

while a:

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    menu_option = int(input("Please enter an option: "))

    if menu_option == 1:
        password = input("Please enter your password to encode: ")
        final_encode = encode(password)
        print()

    elif menu_option == 2:
        final_decode = decode(final_encode)
        print(f"The encoded password is {final_encode}, and the original password is {final_decode}.")
        print()

    elif menu_option == 3:
        break
