text = input()

words = text.split()
word_k = {}

for word in words:
    if word in word_k:
        word_k[word] += 1
    else:
        word_k[word] = 1

print("В вашем тексте", len(word_k), "различных слов")
for word, count in word_k.items():
    print("Слово", word, "встретилось в вашем тексте", count, "раз")