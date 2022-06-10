import string


# If empty_key
def is_key_empty(key):
    if key == '':
        return True
    else:
        return False


# If letters not in A-Z
def is_letters_not_okay(text):
    for letter in text:
        if ord(letter) >= 65 and ord(letter) <= 90:
            pass
        elif ord(letter) == 32:
            pass
        else:
            return True
    return False


# Generating table
def generate_table():
    result = string.ascii_uppercase
    tablica = []
    for row in range(26):
        nr = row
        row_1 = []
        for i in range(26):
            if nr < 26:
                row_1.append(result[nr])
            else:
                nr = 0
                row_1.append(result[nr])
            nr += 1
        tablica.append(row_1)
    return tablica


# Generating password
def generate_password(text, key):
    if is_key_empty(key):
        raise ValueError("Empty key")
    elif is_letters_not_okay(key):
        raise ValueError("Key must be in A-Z")
    elif is_letters_not_okay(text):
        raise ValueError("Text must be in A-Z")
    else:
        encrypted_code = []
        nr_of_letter_in_key = 0
        for letter in text:
            if letter == ' ':
                encrypted_code.append(" ")
            else:
                if nr_of_letter_in_key > len(key) - 1:
                    nr_of_letter_in_key = 0
                    encrypted_code.append(key[nr_of_letter_in_key])
                    nr_of_letter_in_key += 1
                else:
                    encrypted_code.append(key[nr_of_letter_in_key])
                    nr_of_letter_in_key += 1
        return encrypted_code


# Encrypting
def encrypt_vigenere(key, plaintext):
    if is_key_empty(key):
        raise ValueError("Empty key")
    elif is_letters_not_okay(key):
        raise ValueError("Key must be in A-Z")
    elif is_letters_not_okay(plaintext):
        raise ValueError("Plaintext must be in A-Z")
    else:
        table = generate_table()
        alphabet = table[0]
        password = generate_password(plaintext, key)
        encrypted_text = []
        nr_of_letter = 0
        for letter in plaintext:
            if letter == " ":
                encrypted_text.append(" ")
            else:
                for i in range(26):
                    if alphabet[i] == letter:
                        column = i
                        for j in range(26):
                            if table[j][0] == password[nr_of_letter]:
                                row = j
                                break
                encrypted_text.append(table[column][row])
            nr_of_letter += 1
        return "".join(encrypted_text)


# Decrypting
def decrypt_vigenere(key, ciphertext):
    if is_key_empty(key):
        raise ValueError("Empty key")
    elif is_letters_not_okay(key):
        raise ValueError("Key must be in A-Z")
    elif is_letters_not_okay(ciphertext):
        raise ValueError("Ciphertext must be in A-Z")
    else:
        table = generate_table()
        password = generate_password(ciphertext, key)
        alphabet = table[0]
        decrypted_text = []
        nr_of_letter_in_password = 0
        for letter in ciphertext:
            password_1 = password[nr_of_letter_in_password]
            bool_value_1 = True
            bool_value_2 = True
            column = 0
            row = 0
            if letter == " ":
                decrypted_text.append(" ")
            else:
                while bool_value_1:
                    if password_1 == table[row][0]:
                        bool_value_1 = False
                    else:
                        row += 1
                        bool_value_1 = True
                while bool_value_2:
                    if table[row][column] == letter:
                        decrypted_text.append(alphabet[column])
                        bool_value_2 = False
                    else:
                        column += 1
                        bool_value_2 = True
            nr_of_letter_in_password += 1
        return "".join(decrypted_text)


print(encrypt_vigenere('TRUMP', 'KACPER MA KOTA'))
