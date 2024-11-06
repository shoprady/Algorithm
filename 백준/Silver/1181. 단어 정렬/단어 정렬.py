n = int(input())
words = {}
for _ in range(n):
    word = input()
    words[word] = len(word)
    
words = dict(sorted(words.items(), key=lambda x: (x[1], x[0])))
for word in words:
    print(word)