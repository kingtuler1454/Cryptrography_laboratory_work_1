# Реализовать программу шифрования для метода Вижинера с «самоключом»
# (в качестве буквы ключа используется предыдущая буква открытого текста).
# Реализовать программу дешифрования без знания ключа. Для определения ключа дешифрования
# реализовать атаку полного перебора (brute force attack).


def prepare_text(text):
    """Приводит текст к верхнему регистру и оставляет только буквы"""
    return ''.join(filter(str.isalpha, text.upper()))


def char_to_num(char):
    """Преобразует букву в число (A=0, B=1, ..., Z=25)"""
    return ord(char) - ord('A')


def num_to_char(num):
    """Преобразует число в букву (0=A, 1=B, ..., 25=Z)"""
    return chr(num + ord('A'))


def vigenere_self_key_encrypt(plaintext, initial_key):
    """
    Шифрование методом Виженера с самоключом
    """
    plaintext = prepare_text(plaintext)
    initial_key = prepare_text(initial_key)

    if not plaintext:
        return ""

    if not initial_key:
        raise ValueError("Начальный ключ не может быть пустым")

    ciphertext = []
    # Первая буква шифруется с начальным ключом
    p0 = char_to_num(plaintext[0])
    k0 = char_to_num(initial_key[0])
    c0 = (p0 + k0) % 26
    ciphertext.append(num_to_char(c0))

    # Остальные буквы шифруются с предыдущей буквой открытого текста как ключом
    for i in range(1, len(plaintext)):
        p_i = char_to_num(plaintext[i])
        k_i = char_to_num(plaintext[i - 1])  # Самоключ - предыдущая буква открытого текста
        c_i = (p_i + k_i) % 26
        ciphertext.append(num_to_char(c_i))

    return ''.join(ciphertext)


def vigenere_self_key_decrypt(ciphertext, initial_key):
    """
    Дешифрование методом Виженера с самоключом
    """
    ciphertext = prepare_text(ciphertext)
    initial_key = prepare_text(initial_key)

    if not ciphertext:
        return ""

    if not initial_key:
        raise ValueError("Начальный ключ не может быть пустым")

    plaintext = []
    # Первая буква расшифровывается с начальным ключом
    c0 = char_to_num(ciphertext[0])
    k0 = char_to_num(initial_key[0])
    p0 = (c0 - k0) % 26
    plaintext.append(num_to_char(p0))

    # Остальные буквы расшифровываются с предыдущей буквой открытого текста как ключом
    for i in range(1, len(ciphertext)):
        c_i = char_to_num(ciphertext[i])
        k_i = char_to_num(plaintext[i - 1])  # Самоключ - предыдущая буква открытого текста
        p_i = (c_i - k_i) % 26
        plaintext.append(num_to_char(p_i))

    return ''.join(plaintext)


def is_meaningful_text(text, dictionary):
    """
    Проверяет, является ли текст осмысленным (содержит слова из словаря)
    """
    words = text.split()
    if len(words) < 2:  # Слишком короткий текст для анализа
        return False

    meaningful_words = 0
    for word in words:
        if word in dictionary:
            meaningful_words += 1

    # Считаем текст осмысленным, если более 50% слов есть в словаре
    return meaningful_words / len(words) > 0.5


def brute_force_attack(ciphertext, dictionary_file="dictionary.txt"):
    """
    Атака полным перебором на шифр Виженера с самоключом
    """
    # Загружаем словарь для проверки осмысленности текста
    try:
        with open(dictionary_file, 'r', encoding='utf-8') as f:
            dictionary = set(word.strip().upper() for word in f.readlines())
    except FileNotFoundError:
        print(f"Словарь {dictionary_file} не найден. Используется базовый словарь.")
        dictionary = {"THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL",
                      "CAN", "HER", "WAS", "ONE", "OUR", "OUT", "DAY", "GET",
                      "HAS", "HIM", "HIS", "HOW", "MAN", "NEW", "NOW", "OLD",
                      "SEE", "TWO", "WAY", "WHO", "BOY", "DID", "ITS", "LET",
                      "PUT", "SAY", "SHE", "TOO", "USE"}  # Базовый набор слов

    ciphertext = prepare_text(ciphertext)
    possible_solutions = []

    # Перебираем все возможные начальные ключи (A-Z)
    for key_char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        try:
            decrypted = vigenere_self_key_decrypt(ciphertext, key_char)

            # Проверяем, является ли текст осмысленным
            if is_meaningful_text(decrypted, dictionary):
                possible_solutions.append((key_char, decrypted))
        except:
            continue

    return possible_solutions


def main():
    """
    Пример использования функций
    """
    print("=== Шифр Виженера с самоключом ===\n")

    # Пример шифрования
    plaintext = "HELLO WORLD"
    initial_key = "A"

    print(f"Открытый текст: {plaintext}")
    print(f"Начальный ключ: {initial_key}")

    ciphertext = vigenere_self_key_encrypt(plaintext, initial_key)
    print(f"Зашифрованный текст: {ciphertext}")

    # Пример дешифрования
    decrypted = vigenere_self_key_decrypt(ciphertext, initial_key)
    print(f"Расшифрованный текст: {decrypted}")

    print("\n=== Атака полным перебором ===")
    # Атака на зашифрованный текст
    solutions = brute_force_attack(ciphertext)

    if solutions:
        print("Найденные возможные решения:")
        for key, text in solutions:
            print(f"Ключ: {key}, Текст: {text}")
    else:
        print("Осмысленные решения не найдены.")


if __name__ == "__main__":
    main()