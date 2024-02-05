import pandas as pd
import os
from time import sleep


def main():
    while True:
        morse_df = pd.read_csv("morse_file.csv")
        clear_screen()
    
        operation = get_string("Do you want to encode or decode? encode / decode: ")

        
        if operation == None:
            print("Thank you for using my script. good bye")
            break
        elif operation.upper() == "ENCODE":
            print(encode(morse_df))

        elif operation.upper() == "DECODE":
            print(decode(morse_df))

        else:
            print("operation do not exists. Please try again")
            

        run_again = get_string("type Y and enter to run again :")
        if run_again == None:
            print("Thank you for using my script. good bye")
            break
        elif run_again.upper() != "Y":
            print("Thank you for using my script. good bye\n\nprogram exiting....")
            
            sleep(3)

            break




def get_string(question):
    try:
        user_input = input(question)
    except (EOFError, KeyboardInterrupt) :
        print("cancelling operation...")
        sleep(2)
        return None
    else:
        return user_input

def clear_screen():
    # Check the operating system
    if os.name == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':   # Windows
        os.system('cls')
    # else:
    #     print("Unsupported operating system")

def encode(morse_df):
    while True:
        str_to_encode = get_string("Please input strings to convert to morse code :")
        if str_to_encode == None:
            return "operation canceled..."

        try:
            morse_output = ""
            current_char = ""
            for letter in str_to_encode.upper():
                if letter == " ":
                    morse_output += "/ "
                else:
                    # morse_output += morse_df.morse[morse_df.alpha.iloc[letter]] + " "
                    current_char = letter
                    df_index = morse_df[morse_df['alpha'] == letter].index[0]
                    morse_output += morse_df.morse.iloc[df_index] + " "
            
        except IndexError:
            print(f"special character {current_char} does not exist. only works with special characters [. , ? !]")
        
        else:
            return morse_output


def decode(morse_df):
    while True:
        try:
            str_to_decode = get_string("Please input strings to convert to morse code :")
            if str_to_decode == None:
                return "Operation cancelled"
            
            else:
                str_to_decode = str_to_decode.split(" ")


            alpha_output = ""
            for char in str_to_decode:
                if char == "/":
                    alpha_output += "  "
                # elif char =="" or char == "":
                #     pass
                else:
                    df_index = morse_df[morse_df['morse'] == char].index[0]
                    alpha_output += morse_df.alpha.iloc[df_index]
            
        
        except IndexError:
            print("invalid code or a character do not exist")
        
        else:
            return alpha_output
        


if __name__ == "__main__":
    main()