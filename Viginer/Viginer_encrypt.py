def encrypt(text, alphabet):
    """
    Шифрует текст методом Виженера с самоключом
    Для первой буквы используется 'а' как предыдущая
    Пробелы и другие символы не прерывают цепочку ключей
    """
    if not text:
        return ""
 
    result = []
    last_plain_char = 'а'  # Начинаем с 'а' для первой буквы

    for i in range(len(text)):
        current_char = text[i]
        
        if current_char in alphabet:
            # Шифруем текущую букву с использованием последней буквы открытого текста
            char_index = alphabet.index(current_char)
            key_index = alphabet.index(last_plain_char)
            encrypted_index = (char_index + key_index) % len(alphabet)
            encrypted_char = alphabet[encrypted_index]
            
            result.append(encrypted_char)
            last_plain_char = current_char  # Запоминаем текущую букву открытого текста для следующего шага
        else:
            # Для не-алфавитных символов просто копируем их
            result.append(current_char)
            # НЕ обновляем last_plain_char - продолжаем использовать предыдущую букву

    return ''.join(result)