def decrypt(ciphertext, alphabet, first_char_candidate=False):
    """
    Дешифрует текст, зашифрованный методом Виженера с самоключом
    Неалфавитные символы остаются без изменений
    """
    if not ciphertext:
        return ""

    decoded_chars = []

    # Обрабатываем первый символ
    first_encoded_char = first_char_candidate if first_char_candidate else ciphertext[0]

    if first_encoded_char in alphabet:
        encoded_pos = alphabet.index(first_encoded_char)
        key_pos = alphabet.index('а')
        decoded_pos = (encoded_pos - key_pos) % len(alphabet)
        decoded_chars.append(alphabet[decoded_pos])
    else:
        decoded_chars.append(first_encoded_char)

    # Обрабатываем последующие символы
    for position in range(1, len(ciphertext)):
        current_encoded_char = ciphertext[position]
        previous_decoded_char = decoded_chars[position - 1]  # предыдущая расшифрованная буква

        if current_encoded_char in alphabet and previous_decoded_char in alphabet:
            encoded_pos = alphabet.index(current_encoded_char)
            key_pos = alphabet.index(previous_decoded_char)
            decoded_pos = (encoded_pos - key_pos) % len(alphabet)
            decoded_chars.append(alphabet[decoded_pos])
        else:
            decoded_chars.append(current_encoded_char)

    return ''.join(decoded_chars)