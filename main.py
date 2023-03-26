import pandas as pd


morse_df = pd.read_csv("morse_file.csv")


def encode():
    str_to_encode = input("Please input strings to convert to morse code :").upper()
    try:
        morse_output = ""
        for letter in str_to_encode:
            if letter == " ":
                morse_output += "/ "
            else:
                # morse_output += morse_df.morse[morse_df.alpha.iloc[letter]] + " "
                df_index = morse_df[morse_df['alpha'] == letter].index[0]
                morse_output += morse_df.morse.iloc[df_index] + " "
        print(morse_output)
    except IndexError:
        print("special character does not exist. only works with special characters [. , ? !]")
        encode()


def decode():
    try:
        str_to_decode = input("Please input strings to convert to morse code :").split(" ")
        alpha_output = ""
        for char in str_to_decode:
            if char == "/":
                alpha_output += "  "
            elif char =="" or char == "":
                pass
            else:
                df_index = morse_df[morse_df['morse'] == char].index[0]
                alpha_output += morse_df.alpha.iloc[df_index]
        print(alpha_output)
    except IndexError:
        print("invalid code or a character do not exist")
        decode()


def run():
    operation = input("Do you want to encode or decode? encode / decode: ").upper()

    if operation != "ENCODE" and operation != "DECODE":
        print("operation do not exists. Please try again")
        run()

    elif operation == "ENCODE":
        encode()

    else:
        decode()

    run_again = input("Do you want to run again? Y/N :").upper()
    if run_again == "Y":
        print("\n")
        run()
    else:
        print("Thank you for using my script. good bye")


run()
