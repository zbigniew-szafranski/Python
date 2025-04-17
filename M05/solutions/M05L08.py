### 🔴 Ćwiczenie

# Zerknij na rozwiązanie ćwiczenia M04L08. Znajduje się tam trochę powtórzonego kodu.
# 1. Użyj funkcji, aby uniknąć duplikacji kodu.
# 2. Popraw kod tak, aby miał funkcję main().
# 3. Czy widzisz jakieś bloki kodu zaczynające się od komentarza podsumowującego, co robi dany blok? Jeśli tak, to jak możesz zwiększyć czytelność kodu poprzez wprowadzenie nowych funkcji?
import glob


def preprocess_review(review):
    return review.lower().replace('</br', ' ').split()


def count_words(path_pattern):
    words_count = {}
    files = glob.glob(path_pattern)
    for file in files:
        with open(file) as stream:
            content = stream.read()
            words = preprocess_review(content)
            for word in set(words):
                words_count[word] = words_count.get(word, 0)+1
    return words_count

def compute_sentiment(words, words_count_pos, words_count_neg, debug=False):
    sentence_sentiment = 0
    for word in words:
        positive = words_count_pos.get(word, 0)
        negative = words_count_neg.get(word, 0)
        comments_all = positive + negative

        if comments_all ==0:
            word_sentiment = 0.0
        else:
            word_sentiment = (positive-negative)/comments_all
        if debug:
            print(f"Słowo '{word}' ma sentyment: {word_sentiment}")
            sentence_sentiment+=word_sentiment
    for r in range(10):
        print('-', end="")
    print()
    sentence_sentiment /=len(words)
    return sentence_sentiment


def print_sentiment(sentiment):
    if sentiment > 0:
        label = 'positive'
    else:
        label = 'negative'
    print("This sentence is", label, 'sentiment=', sentiment)

def main():
    words_count_pos = count_words('M03/data/aclImdb/train/pos/*.txt')
    words_count_neg = count_words('M03/data/aclImdb/train/neg/*.txt')

    sentence = input("Write a comment, ONLY English please: ").lower()
    words = preprocess_review(sentence)
    sentiment = compute_sentiment(words, words_count_pos, words_count_neg, debug=True)
    print_sentiment(sentiment)

if __name__ == "__main__":
    main()