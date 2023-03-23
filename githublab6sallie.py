# Sallie Zhou

# Lab Partner is Joanna Mijares

# method that encodes the password
def encode(password):
    # initializing list
    encoded_password = []
    # initializing string
    final_encode = ""
    # loops through given password
    for digit in password:
        # adds three to each number
        encoded_digit = int(digit) + 3
        # appends the new digit to the end of the list
        encoded_password.append(encoded_digit)
    # turns list of new password into a string using the join function
    final_encode = "".join(str(digit) for digit in encoded_password)
    return final_encode


# method that decodes the password
def decode(final_encode):
    decoded_password = []
    final_decode = ""
    # loops through each number in the encoded password, subtracts three, and appends it to the initialized list
    for digit in final_encode:
        decoded_digit = int(digit) - 3
        decoded_password.append(decoded_digit)
    # turns list into string
    final_decode = "".join(str(digit) for digit in decoded_password)
    return final_decode


a = True
# loops through the menu and menu options
while a:

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    # asks user for password input
    menu_option = int(input("Please enter an option: "))

    if menu_option == 1:
        password = input("Please enter your password to encode: ")
        # uses encode method to store new password as final_encode
        final_encode = encode(password)
        print()

    elif menu_option == 2:
        # uses decode method to store decoded password as final_decode
        final_decode = decode(final_encode)
        print(f"The encoded password is {final_encode}, and the original password is {final_decode}.")
        print()
    # quits the program
    elif menu_option == 3:
        break
