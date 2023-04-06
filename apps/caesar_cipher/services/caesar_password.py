# from apps.caesar_cipher import models
import string


def crypto(text: str, key: int):
    obrazec_u = string.ascii_uppercase
    obrazec_l = string.ascii_lowercase
    obrazec_dig = string.digits
    obrazec_p = string.punctuation

    def find_letter(i, obrazec, key):
        index = obrazec.find(i)
        if_key = index + key

        if if_key > len(obrazec) or if_key < 0:
            if_key = if_key % len(obrazec)
        letter = obrazec[if_key]
        return letter

    newtext = []
    for i in text:
        if i in obrazec_u:
            obrazec = obrazec_u
            letter = find_letter(i, obrazec, key)

        elif i in obrazec_l:
            obrazec = obrazec_l
            letter = find_letter(i, obrazec, key)

        elif i in obrazec_dig:
            obrazec = obrazec_dig
            letter = find_letter(i, obrazec, key)

        elif i in obrazec_p:
            obrazec = obrazec_p
            letter = find_letter(i, obrazec, key)

        else:
            letter = i
        newtext.append(letter)
    return "".join(newtext)


def decrypto(text: str, key: int):
    obrazec_u = string.ascii_uppercase
    obrazec_l = string.ascii_lowercase
    obrazec_dig = string.digits
    obrazec_p = string.punctuation

    def find_letter(i, obrazec, key):
        index = obrazec.find(i)
        if_key = index - key

        if if_key > len(obrazec) or if_key < 0:
            if_key = if_key % len(obrazec)

        letter = obrazec[if_key]
        return letter

    newtext = []
    for i in text:
        if i in obrazec_u:
            obrazec = obrazec_u
            letter = find_letter(i, obrazec, key)

        elif i in obrazec_l:
            obrazec = obrazec_l
            letter = find_letter(i, obrazec, key)

        elif i in obrazec_dig:
            obrazec = obrazec_dig
            letter = find_letter(i, obrazec, key)

        elif i in obrazec_p:
            obrazec = obrazec_p
            letter = find_letter(i, obrazec, key)

        else:
            letter = i
        newtext.append(letter)
    return "".join(newtext)


crypto_result = crypto(text="fgf RTRY АПР", key=500)
print(crypto_result)
print(decrypto(text=crypto_result, key=500))
