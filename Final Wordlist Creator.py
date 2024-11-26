art="""
     █     █░ ▒█████   ██▀███  ▓█████▄  ██▓     ██▓  ██████ ▄▄▄█████▓    ▄████▄   ██▀███  ▓█████  ▄▄▄      ▄▄▄█████▓ ▒█████   ██▀███  
    ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌▓██▒    ▓██▒▒██    ▒ ▓  ██▒ ▓▒   ▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀ ▒████▄    ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
    ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌▒██░    ▒██▒░ ▓██▄   ▒ ▓██░ ▒░   ▒▓█    ▄ ▓██ ░▄█ ▒▒███   ▒██  ▀█▄  ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
    ░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌▒██░    ░██░  ▒   ██▒░ ▓██▓ ░    ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄ ░██▄▄▄▄██ ░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
    ░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓ ░██████▒░██░▒██████▒▒  ▒██▒ ░    ▒ ▓███▀ ░░██▓ ▒██▒░▒████▒ ▓█   ▓██▒  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
    ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░      ░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒   ▓▒█░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
      ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ ░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░    ░         ░  ▒     ░▒ ░ ▒░ ░ ░  ░  ▒   ▒▒ ░    ░      ░ ▒ ▒░   ░▒ ░ ▒░
      ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░   ░ ░    ▒ ░░  ░  ░    ░         ░          ░░   ░    ░     ░   ▒     ░      ░ ░ ░ ▒    ░░   ░ 
        ░        ░ ░     ░        ░        ░  ░ ░        ░              ░ ░         ░        ░  ░      ░  ░             ░ ░     ░     
                                ░                                       ░                                                             
"""

print(art)


import itertools
import time

# Define the possible values for each type
CHAR_SETS = {
    "C_ALPHA": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",  # Uppercase letters
    "S_ALPHA": "abcdefghijklmnopqrstuvwxyz",  # Lowercase letters
    "NUMERIC": "1234567890",  # Numeric digits
    "SPL_CHAR": "@#._-",  # Special characters
    "UNKNOWN": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#._-"
}

def generate_wordlist(positions):
    """
    Generate all possible combinations based on the input positions.
    :param positions: List of strings, each being a letter or a function like 'C_ALPHA'.
    :return: A list of all possible combinations of the given input.
    """
    # Generate the list of possible characters at each position
    char_options = []
    for pos in positions:
        if pos in CHAR_SETS:
            char_options.append(CHAR_SETS[pos])  # Add the corresponding character set
        else:
            char_options.append(pos)  # If it's a letter, just add it as-is

    # Generate all permutations/combinations
    return [''.join(comb) for comb in itertools.product(*char_options)]

def save_wordlist(wordlist, filename="wordlist.txt"):
    """
    Save the generated wordlist to a text file.
    :param wordlist: List of generated words.
    :param filename: Name of the file where the wordlist should be saved.
    """
    with open(filename, 'w') as file:
        for word in wordlist:
            file.write(word + '\n')
    time.sleep(1)
    print("\n\n    File Created Successfully")
    time.sleep(0.5)
    print(f"    Wordlist saved to {filename}")

def startup_messages():
    messages = [
        "    Initializing...",
        "Loading resources...",
        "Starting script..."
    ]
    
    # Loop through the messages and display them with a 1-second delay
    for message in messages:
        time.sleep(1.5)
        print(message, end="   ", flush=True)
        time.sleep(1)

    for i in range(3, 0, -1):
        print(f"{i}..", end="  ", flush=True)
        time.sleep(1)  # Wait for 1 second
        


def main():
    startup_messages()
    print("""

    This script generates a wordlist based on user-defined inputs. You can specify each position 
    in the wordlist as a letter or use one of the following functions to specify a range of values:
    
    - 'C_ALPHA': Any uppercase letter (A-Z)
    - 'S_ALPHA': Any lowercase letter (a-z)
    - 'NUMERIC': Any number (1-9)
    - 'SPL_CHAR': Any special character (@, #, $, _, -, etc.)
    - 'UNKNOWN': All possible character [ (A-Z),(a-z),(1-9),(@, #, $, _, -, etc.) ]
    - Enter any character you want to be fixed
    """)
    abt = input("\n    Press Enter to begin or type 'abt' for more info: ")  # Pause to let user read the description

    if abt=='abt':
        time.sleep(1.5)
        print("""
        The program will generate all possible permutations based on these inputs and save the results 
        to a text file. You can use the generated wordlist for various purposes such as password testing, 
        brute-force attacks, or any other scenario where you need a list of possible word combinations,
        if you know any character in password who can ENTER THAT CHARACTER, then it will be there at his
        place.

        TIP:- If you guessed a character in password, but unsure or confused between some characters for
              that space you can write all of them in one space.
              Example- If you are confused between S or s for which one should be at first place;
                       you can write Ss so this script generate permutations for both.
    
        Usage:
        1. Enter the number of positions for the wordlist.
        2. For each position, input either a specific letter or a function (e.g., C_ALPHA, NUMERIC).
        3. The program will generate a wordlist and save it to a file called "wordlist.txt".
    
        Example:
        - If you enter 'C_ALPHA' for one position, 'NUMERIC' for another, and 'SPL_CHAR' for the last, 
        the program will generate a wordlist containing all combinations of uppercase letters, numbers, 
        and special characters.
        """)
        input("    Press Enter to begin: ")     # Pause to let user read the about section
    
    time.sleep(1.5)

    # Get the number of positions from the user
    x = int(input("\n    Enter the number of spaces for the wordlist: "))

    # Get the input for each position
    positions = []
    for i in range(x):
        user_input = input(f"\n    Enter letter or function for position {i + 1}: ").strip()
        positions.append(user_input)

    # Generate the wordlist
    wordlist = generate_wordlist(positions)

    time.sleep(1.5)
    print("\n    Generating Please wait...")
    time.sleep(1)
    for i in range(4, 0, -1):
        if i==4:
            print("    ", end="", flush=True)
        print(f"{i}...", end="  ", flush=True)
        time.sleep(1)  # Wait for 1 second
        
    
    
    # Save the wordlist to a file
    save_wordlist(wordlist)

if __name__ == "__main__":
    main()
    
time.sleep(1)
input("\n    Press any key to exit... ")
