import random
from news import get_website_content

def generate_trigram(corpus):
    trigrams = {}
    words = corpus.split()
    for i in range(len(words)-2):
        key = (words[i], words[i+1])
        value = words[i+2]
        if key in trigrams:
            trigrams[key].append(value)
        else:
            trigrams[key] = [value]
    return trigrams


def generate_text(trigrams, max_length=50):
    seed = random.choice(list(trigrams.keys()))
    text = list(seed)
    length = 0
    while length < max_length:
        if seed in trigrams:
            possible_words = trigrams[seed]
            next_word = random.choice(possible_words)
            text.append(next_word)
            seed = (seed[1], next_word)
            length += 1
        else:
            break
    return ' '.join(text)


corpus = get_website_content('https://zehabesha.com/')
trigrams = generate_trigram(corpus)
generated_text = generate_text(trigrams, max_length=10) 
print(generated_text)