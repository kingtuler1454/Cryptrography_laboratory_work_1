def decrypt(ciphertext, alphabet, first_char_candidate=False):
    """
    Дешифрует текст, зашифрованный методом Виженера с самоключом
    Пробелы и другие символы не прерывают цепочку ключей
    """
    if not ciphertext:
        return ""
 
    decoded_chars = []
    last_decoded_char = 'а'  # Начинаем с предположения, что первая буква использовала ключ 'а'

    # Обрабатываем первый символ
    if first_char_candidate:
        decoded_chars.append(first_char_candidate)
        last_decoded_char = first_char_candidate
    else:
        first_encoded_char = ciphertext[0]
        if first_encoded_char in alphabet:
            encoded_pos = alphabet.index(first_encoded_char)
            key_pos = alphabet.index('а')
            decoded_pos = (encoded_pos - key_pos) % len(alphabet)
            decoded_char = alphabet[decoded_pos]
            decoded_chars.append(decoded_char)
            last_decoded_char = decoded_char
        else:
            decoded_chars.append(first_encoded_char)

    # Обрабатываем последующие символы
    for i in range(1, len(ciphertext)):
        current_encoded_char = ciphertext[i]
        
        if current_encoded_char in alphabet and last_decoded_char in alphabet:
            encoded_pos = alphabet.index(current_encoded_char)
            key_pos = alphabet.index(last_decoded_char)
            decoded_pos = (encoded_pos - key_pos) % len(alphabet)
            decoded_char = alphabet[decoded_pos]
            
            decoded_chars.append(decoded_char)
            last_decoded_char = decoded_char
        else:
            decoded_chars.append(current_encoded_char)
            # НЕ обновляем last_decoded_char для не-алфавитных символов

    return ''.join(decoded_chars)