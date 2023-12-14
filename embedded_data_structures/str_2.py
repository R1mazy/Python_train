text_obr = input()
text = input()

text = text.lower()
words = set(text.split())
word_k = {}

text_obr = text_obr.lower()
words_obr = set(text_obr.split())
word_k_obr = {}

unique_words = words.difference(words_obr)
unique_percent = len(unique_words) / len(words) * 100

print(len(words) - len(unique_words))
print(f"{int(unique_percent)}%")
