# WordList_Creator

## Description
This Python script generates a wordlist based on user-defined inputs. Users can specify the type of characters to include in each position, such as uppercase letters, lowercase letters, numbers, special characters, or any custom combination. The generated wordlist is saved as a text file and can be used for purposes like password testing, brute-force attacks, or creating unique combinations of characters.

---

## Features
- **Customizable Positions:** Specify the type of character for each position.
- **Predefined Character Sets:**
  - `C_ALPHA`: Uppercase letters (A-Z)
  - `S_ALPHA`: Lowercase letters (a-z)
  - `NUMERIC`: Numbers (1-9)
  - `SPL_CHAR`: Special characters (@, #, ., _, -)
  - `UNKNOWN`: Includes all possible characters (A-Z, a-z, 1-9, @, #, ., _, -)
- **Fixed Characters:** Enter specific characters to be fixed in certain positions.
- **Permutations Generation:** Generates all possible combinations based on the user-defined inputs.
- **File Output:** Saves the wordlist to a text file named `wordlist.txt`.

---

## Usage Instructions
1. Run the script in a Python environment.
2. Follow the on-screen prompts:
   - Enter the number of positions for the wordlist.
   - For each position, input a character type (e.g., `C_ALPHA`, `NUMERIC`) or specific letters.
3. The script will generate a wordlist with all possible combinations based on your input.
4. The wordlist will be saved in a file named `wordlist.txt` in the same directory as the script.

---

## Advanced Tips
- **Partial Knowledge of Password:** If you know some parts of a password, you can enter specific characters for those positions. Example:
  - If you're unsure whether the first character is `S` or `s`, input `Ss` for that position.
  - The script will generate combinations for both.
- **Confusion Between Characters:** For a position where you are confused between multiple characters, input all possibilities together (e.g., `ABC` for uppercase options A, B, or C).

---

## Dependencies
- Python 3.x
- `itertools` module (built-in with Python)

---

## Output File
The generated wordlist will be saved as `wordlist.txt`. Ensure you have write permissions in the directory where the script is executed.

---

## Disclaimer
This script is intended for educational purposes only. Use it responsibly and ensure compliance with local laws and regulations. Unauthorized use of this script for unethical purposes is prohibited.

---
