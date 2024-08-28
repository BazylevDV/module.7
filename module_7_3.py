import re


class WordsFinder:
    def __init__(self, *file_names):
        """
        Инициализатор класса WordsFinder.
        Принимает произвольное количество имен файлов и сохраняет их в атрибут file_names.
        Также вызывает метод get_all_words для заполнения атрибута all_words.
        """
        self.file_names = file_names
        self.all_words = self.get_all_words()

    def get_all_words(self):
        """
        Метод для сбора всех слов из файлов.
        Возвращает словарь, где ключи - имена файлов, а значения - списки слов в нижнем регистре.
        """
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                text = re.sub(r'\n', ' ', text)  # Замена переносов строк на пробелы
                text = re.sub(r'[,\.=!?;:\s-]+', ' ', text)  # Удаление пунктуации и замена на пробел
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        """
        Метод для поиска первого вхождения слова в каждом файле.
        Возвращает словарь, где ключи - имена файлов, а значения - позиции первого вхождения слова.
        """
        word = word.lower()
        result = {}
        for file_name, words in self.all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1  # +1 для нумерации с 1
        return result

    def count(self, word):
        """
        Метод для подсчета количества вхождений слова в каждом файле.
        Возвращает словарь, где ключи - имена файлов, а значения - количество вхождений слова.
        """
        word = word.lower()
        result = {}
        for file_name, words in self.all_words.items():
            result[file_name] = words.count(word)
        return result


# Пример использования
if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))     # 3 слово по счёту
    print(finder2.count('teXT'))    # 4 слова teXT в тексте всего