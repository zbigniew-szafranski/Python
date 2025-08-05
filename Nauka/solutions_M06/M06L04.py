### 🔴 Ćwiczenie

# Masz listę komentarzy. Każdy komentarz reprezentujesz jako listę słów.

# Zbuduj listę zawierającą wszystkie słowa ze wszystkich recenzji. Chodzi o płaską, tzn. nie poza-gnieżdżaną listę. Taka lista może być później używana dalej.

# Napisz testy!



def get_unique_words(comments):
    """
    Extract unique words from a nested list of strings.

    This function takes a nested list of strings and extracts unique words
    from all the inner lists, omitting empty strings.

    Args:
        comments (list[list[str]]): A nested list where each inner list contains
        strings representing words or phrases.

    Returns:
        list[str]: A list containing unique non-empty words extracted from the
        input, without any duplicates.
    """
    return list({el for row in comments for el in row if el})

def main():
    comments = [
        ['pierwszy', 'komentarz'],
        ['drugi', 'komentarz'],
        ['trzeci', 'komentarz'],
        ['czwarty', 'komentarz'],
        ['', '']
    ]
    print(f'comments = {comments}')
    words = get_unique_words(comments)
    print(f'words = {words}')


if __name__ == "__main__":
    main()