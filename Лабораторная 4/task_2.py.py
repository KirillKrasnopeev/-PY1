def get_count_char(str_):
    str_ = str_.lower()
    num_str = [str_[i] for i in range(len(str_))]
    return {num_str[i]: num_str.count(num_str[i])
        for i in range(len(num_str))
        if (num_str[i].isalpha() and num_str[i] != num_str[i+1])}

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
