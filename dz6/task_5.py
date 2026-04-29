import sys

# возможно я трошки перемудрила тк выглядит громозко
# но ничего лучше я не придумала

rus_alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
eng_alphabet_lower = "abcdefghijklmnopqrstuvwxyz"


def encrypt(some_str: str, shift=3) -> str:
    new_str = ""
    for letter in some_str:
        if letter.lower() in rus_alphabet_lower:
            alphabet = rus_alphabet_lower
        elif letter.lower() in eng_alphabet_lower:
            alphabet = eng_alphabet_lower
        else:
            new_str += letter
            continue

        is_upper = letter.isupper()
        letter_lower = letter.lower()

        letter_index = alphabet.find(letter_lower)
        new_index = (letter_index + shift) % len(alphabet)
        new_letter = alphabet[new_index]
        new_letter = new_letter.upper() if is_upper else new_letter

        new_str += new_letter
    return new_str


def decrypt(some_str: str, shift=3) -> str:
    new_str = ""
    for letter in some_str:
        if letter.lower() in rus_alphabet_lower:
            alphabet = rus_alphabet_lower
        elif letter.lower() in eng_alphabet_lower:
            alphabet = eng_alphabet_lower
        else:
            new_str += letter
            continue

        is_upper = letter.isupper()
        letter_lower = letter.lower()

        letter_index = alphabet.find(letter_lower)
        new_index = (letter_index - shift) % len(alphabet)
        new_letter = alphabet[new_index]
        new_letter = new_letter.upper() if is_upper else new_letter

        new_str += new_letter
    return new_str


encrypt_or_decrypt = int(
    input("Choose an option: enter 1 to DECRYPT, or 0 to ENCRYPT: ")
)
if encrypt_or_decrypt not in [0, 1]:
    print("ERROR: Invalid input! Please enter only 0 or 1.")
    sys.exit()

some_str = input("Enter your message: ")

if encrypt_or_decrypt:
    shift = int(input("Enter shift value (or 0 to use default shift = 3): "))
    if shift != 0:
        result = decrypt(some_str, shift)
    else:
        result = decrypt(some_str)
    print(f"Decrypted message: {result}")
else:
    shift = int(input("Enter shift value (or 0 to use default shift = 3): "))
    if shift != 0:
        result = encrypt(some_str, shift)
    else:
        result = encrypt(some_str)
    print(f"Encrypted message: {result}")

# на уроке ты показал поэтому ну уже будет
# не честно менять что-то, делала до урока
