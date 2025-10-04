from Viginer.viginer_decrypt import decrypt


def brute(cipher_text, alphabet):
    """
    Атака полным перебором для определения начального ключа
    """
    best_key = None
    best_score = 0

    for key_candidate in alphabet:
        try:
            # Пробуем дешифровать с текущим кандидатом ключа
            decrypted = decrypt(cipher_text, alphabet, key_candidate)


            print(f"Ключ '{key_candidate}': {decrypted[:50]}")



        except Exception as e:
            print(e)


