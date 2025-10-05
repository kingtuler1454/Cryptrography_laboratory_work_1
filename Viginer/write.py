def write_file(filename, content):
    """Записывает содержимое в файл"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Файл успешно сохранен: {filename}")
        return True
    except Exception as e:
        print(f"Ошибка при записи файла {filename}: {e}")
        return False