text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
words = text.split()
new_words = []

for word in words:
    if word.endswith(',') or word.endswith('.'):
        sign = word[-1]
        clean_word = word[:-1]
        new_word = clean_word + 'ing' + sign
    else:
        new_word = word + 'ing'

    new_words.append(new_word)

end = ' '.join(new_words)

print(end)
