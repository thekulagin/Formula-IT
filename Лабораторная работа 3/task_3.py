# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()
    letters = {}

    for char in text:
        if char.isalpha():
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1

    return letters


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters):
    letters_frequency = {}
    letters_amount = 0

    for letter_count in letters.values():
        letters_amount += letter_count

    for letter in letters.items():
        letters_frequency[letter[0]] = letter[1] / letters_amount

    return letters_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

frequency = calculate_frequency(count_letters(main_str))
for letter in frequency.items():
    print(f"{letter[0]}: {letter[1]:.2f}")