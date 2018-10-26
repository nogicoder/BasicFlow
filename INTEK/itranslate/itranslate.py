def itranslate(dic, string):
    french_fries = string.split(" ")
    english_fries = []
    for fries in french_fries:
        for word in dic.keys():
            if fries not in dic.keys():
                raise KeyError("Missing word")
            else:
                if fries == word:
                    english_fries.append(dic[word])
    " ".join(english_fries)
    return english_fries


print(itranslate({"bonjour": "hello", "je": "I", "pere": "father", "suis": "am", "ton": "your"}, 'bonjour je suis ton daron'))
