import random
import re
import pymorphy3

NULLSYMBOl = 'î'


def fotx(word):
    morph = pymorphy3.MorphAnalyzer()
    out = ""
    vowels = ["а", "у", "е", "о", "э", "я", "и", "ю", "ё", "ы",
              "А", "У", "Е", "О", "Э", "Я", "И", "Ю", "Ё", "Ы"]
    f = {"а": "я", "у": "ю", "е": "е", "о": "ё", "э": "е", "я": "я", "и": "и", "ю": "ю", "ё": "ё", "ы": "и",
         "А": "Я", "У": "Ю", "Е": "Е", "О": "Ё", "Э": "Е", "Я": "Я", "И": "И", "Ю": "Ю", "Ё": "Ё", "Ы": "И"}
    # здесь просто проверить если word - не русская буква
    if word == "я":
        out += "головка от хуя"
        return out
    if len(word) < 3:
        return word
    huegs = morph.parse(word)[0]
    if 'INTJ' in huegs.tag or \
            'PRCL' in huegs.tag or \
            'CONJ' in huegs.tag or \
            'PREP' in huegs.tag or \
            'NPRO' in huegs.tag or \
            'UNKN' in huegs.tag:
        return word
    ch = word[:3]
    mod = ""
    if ch[2] in vowels:
        mod = "ху" + f[ch[2]] + word[3:]
    elif ch[1] in vowels:
        mod = "ху" + f[ch[1]] + word[2:]
    elif ch[0] in vowels:
        mod = "ху" + f[ch[0]] + word[1:]
    else:
        mod = "хуи" + word[2:]
    if ch[0] not in vowels and ('Я' >= ch[0] >= 'А' or ch[0] == 'Ё'):
        mod = 'Х' + mod[1:]
    return mod


def makeOk(text):
    global NULLSYMBOl
    msg_text = text
    new_text = ""
    for i in msg_text:
        if i == ' ':
            new_text += ' ' + NULLSYMBOl + ' '
            continue
        if not bool(re.match('^[а-яА-Яё-ёЁ-Ё]*$', i)):
            new_text += ' ' + i + ' '
        else:
            new_text += i
    new_text = new_text.replace('\n', ' \n ')
    new_text = new_text.replace('\t', ' \t ')
    return new_text


def huizator(text, chance=100):
    global NULLSYMBOl
    if not text:
        return 'ЧЕ ЗА ХУЕТА'
    msg_text = makeOk(text)
    msg_text = msg_text.split(' ')
    out = ""
    for cur in msg_text:
        mod = cur
        if mod == '':
            continue
        if mod == NULLSYMBOl:
            out += ' '
            continue
        if not bool(re.match('^[а-яА-Яё-ёЁ-Ё]*$', mod)):
            out += mod
            continue
        valchance = random.randint(1, 100)
        if valchance <= chance:
            mod = fotx(cur)
        out += mod
    return out
