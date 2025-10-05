# Реализовать программу шифрования для метода Вижинера с «самоключом»
# (в качестве буквы ключа используется предыдущая буква открытого текста).
# Реализовать программу дешифрования без знания ключа. Для определения ключа дешифрования
# реализовать атаку полного перебора (brute force attack).
from Viginer.Viginer_encrypt import encrypt
from Viginer.brute import brute
from Viginer.read import read_file
from Viginer.viginer_decrypt import decrypt
from Viginer.write import write_file


def main():
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    test_text = read_file('исходныйтекст.txt')

    encrypted = encrypt(test_text, alphabet)
    write_file('зашифрованныйтекст.txt',encrypted)

    decrypted = decrypt(encrypted, alphabet)
    write_file('расшифрованныйтекст.txt',decrypted)

    brute(encrypted ,alphabet)


if __name__ == "__main__":
    main()


