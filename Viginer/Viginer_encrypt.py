def encrypt(text, alphabet):
    """
    Шифрует текст методом Виженера с самоключом
    Для первой буквы используется 'а' как предыдущая
    """
    if not text:
        return ""

    result = []

    # Обрабатываем первую букву - используем 'а' как предыдущую
    first_char = text[0]
    if first_char in alphabet:
        char_index = alphabet.index(first_char)
        key_index = alphabet.index('а')
        encrypted_index = (char_index + key_index) % len(alphabet)
        result.append(alphabet[encrypted_index])
    else:
        result.append(first_char)

    # Обрабатываем остальные буквы
    for i in range(1, len(text)):
        current_char = text[i]
        previous_char = text[i - 1]  # предыдущая буква исходного текста

        if current_char in alphabet and previous_char in alphabet:
            char_index = alphabet.index(current_char)
            key_index = alphabet.index(previous_char)
            encrypted_index = (char_index + key_index) % len(alphabet)
            result.append(alphabet[encrypted_index])
        else:
            result.append(current_char)

    return ''.join(result)