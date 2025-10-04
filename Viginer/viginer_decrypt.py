def decrypt(encrypted_text, alphabet,key_candidate=False):
    """
    Дешифрует текст, зашифрованный методом Виженера с самоключом
    """
    if not encrypted_text:
        return ""

    result = []

    # Первая буква - используем 'а' как ключ
    first_encrypted =key_candidate if key_candidate else encrypted_text[0]
    encrypted_index = alphabet.index(first_encrypted)
    key_index = alphabet.index('а')
    decrypted_index = (encrypted_index - key_index) % len(alphabet)
    result.append(alphabet[decrypted_index])

    # Остальные буквы
    for i in range(1, len(encrypted_text)):
        current_encrypted = encrypted_text[i]
        # Используем предыдущую РАСШИФРОВАННУЮ букву как ключ
        previous_decrypted = result[i-1]

        encrypted_index = alphabet.index(current_encrypted)
        key_index = alphabet.index(previous_decrypted)
        decrypted_index = (encrypted_index - key_index) % len(alphabet)
        result.append(alphabet[decrypted_index])

    return ''.join(result)

