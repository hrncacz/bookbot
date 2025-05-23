import re


def count_words(text_to_count):
    return len(text_to_count.split())


def count_letters(text_to_count):
    dic = {}
    for ch in text_to_count.lower():
        if ch.isalpha() and ch in dic:
            dic[ch] += 1
        elif ch.isalpha() and ch not in dic:
            dic[ch] = 1
    sortedDic = {}
    while len(dic) > 0:
        maxV = max(dic, key=dic.get)
        sortedDic[maxV] = dic[maxV]
        dic.pop(maxV)

    return sortedDic
