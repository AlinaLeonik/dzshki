import sys

rus_alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
eng_alphabet_lower = "abcdefghijklmnopqrstuvwxyz"

# я рассматриваю только случаи,
# когда ключ на том же языке что слово,
# но понимаю что можно допилить


def encrypt(some_str: str, keyword="ключ") -> str:
    new_key = ""
    for i in range(len(some_str)):
        new_key += keyword[i % len(keyword)]

    new_str = ""
    for i, letter in enumerate(some_str):
        if letter.lower() in rus_alphabet_lower:
            alphabet = rus_alphabet_lower
        elif letter.lower() in eng_alphabet_lower:
            alphabet = eng_alphabet_lower
        else:
            new_str += letter
            continue

        # эти две строки(выше) наверное было бы логично вынести
        # из if но оставить в цикле, тк они в обоих ифах повторяются
        # но что-то мне не хочется прописывать случай в котором
        # не буква а знак

        is_upper = letter.isupper()
        letter_lower = letter.lower()

        letter_index = alphabet.find(letter_lower)
        new_key_index = alphabet.find(new_key[i])
        new_index = (letter_index + new_key_index) % len(alphabet)
        new_letter = alphabet[new_index]
        new_letter = new_letter.upper() if is_upper else new_letter

        new_str += new_letter
    return new_str


def decrypt(some_str: str, keyword="ключ") -> str:
    new_key = ""
    for i in range(len(some_str)):
        new_key += keyword[i % len(keyword)]

    new_str = ""
    for i, letter in enumerate(some_str):
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
        new_key_index = alphabet.find(new_key[i])
        new_index = (letter_index - new_key_index) % len(alphabet)
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
    keyword = input("Enter key value (or 0 to use default keyword = ключ): ")
    if keyword != "0":
        result = decrypt(some_str, keyword)
    else:
        result = decrypt(some_str)
    print(f"Decrypted message: {result}")
else:
    keyword = input("Enter key value (or 0 to use default keyword = ключ): ")
    if keyword != "0":
        result = encrypt(some_str, keyword)
    else:
        result = encrypt(some_str)
    print(f"Encrypted message: {result}")
