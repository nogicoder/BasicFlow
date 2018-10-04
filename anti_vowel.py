def anti_vowel(text):
  for i in text:
    if i in ("aeuioAEUIO"):
        text = text.replace(i, "")
  return text
