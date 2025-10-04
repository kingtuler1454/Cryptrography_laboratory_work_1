# Реализовать программу шифрования для метода Вижинера с «самоключом»
# (в качестве буквы ключа используется предыдущая буква открытого текста).
# Реализовать программу дешифрования без знания ключа. Для определения ключа дешифрования
# реализовать атаку полного перебора (brute force attack).
from Viginer.Viginer_encrypt import encrypt
from Viginer.brute import brute
from Viginer.viginer_decrypt import decrypt


def main():
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    test_text = "приветмир"
    print(f"Исходный текст: {test_text}")

    encrypted = encrypt(test_text, alphabet)
    print(f"Зашифрованный:  {encrypted}")

    decrypted = decrypt(encrypted, alphabet)
    print(f"Расшифрованный: {decrypted}")
    input('brute--')
    brute(encrypted ,alphabet)


if __name__ == "__main__":
    main()


