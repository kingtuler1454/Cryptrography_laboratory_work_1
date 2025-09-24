def viginer_encrypt(text,alphabet):
    result_text=[]
    index_last_symbol=0

    for number_symbol,symbol in enumerate(text):
        index_text_symbol=alphabet.index(symbol)
        chifer_index_symbol=(index_text_symbol +index_last_symbol) %len(alphabet)
        result_text.append(alphabet[chifer_index_symbol])
        index_last_symbol=index_text_symbol
    print(result_text)

# # Проверка
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# text = "HELLO"