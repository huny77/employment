words = input()
filtered_words = list(filter(lambda x:x in 'aeiou', words))
print(len(filtered_words))