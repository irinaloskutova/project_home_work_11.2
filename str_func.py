def upper_word(word):
    """функция возвращает слово/фразу большими буквами"""
    return word.upper()



def little_word(word):
    """функция возвращает слово/фразу маленькими буквами"""
    return word.lower() 



def title_word(word):
    """функция возвращает в слове/ во фразе первую букву большой"""
    return word.title()



i = input()
print(upper_word(i))
