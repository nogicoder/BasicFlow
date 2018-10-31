def censor(text, word):
    """create stars
  newword = word
  for j in newword:
        newword = newword.replace(j, '*')"""

  text = text.split(" ")
  for (i, item) in enumerate (text): #loop through the list and replace only matched item by refering to the index
    if text[i] == word:
      text[i] = newword
  text = " ".join(text)
  return text


def censor(text, word):
    stars = '*' * len(word) #create stars - follow the number of characters instead of replacing each character

    words = text.split()
    count = 0
    for i in words:
        if i == word:
            words[count] = stars #loop through the list and replace only matched item by refering to the index through a counting variable instead of enumerate property
        count += 1
    words =' '.join(words)
    return result
