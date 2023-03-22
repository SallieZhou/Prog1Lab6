# Sallie Zhou

def encode(password):
    encoded_password = []
    final_encode = ""
    for digit in password:
        encoded_digit = int(digit) + 3
        encoded_password.append(encoded_digit)
    final_encode = "".join(str(digit) for digit in encoded_password)
    return final_encode


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
        encode(password)
