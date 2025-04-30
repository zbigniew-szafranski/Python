### 🔴 Ćwiczenie

# Mając podaną listę plików znajdź tylko te, które mają rozszerzenie ".txt".

# Uwaga - zakładamy, że mamy już pewną listę plików, więc nie możemy użyć funkcji glob.glob.

# Rozszerzenie pliku możesz sprawdzić znacznie szybciej, niż robiliśmy to do tej pory. W końcu wystarczy sprawdzić, czy napis kończy się na ".txt". Jak to zrobisz? Poszukaj. :)

# Napisz testy!


def extension(files):
    return [f for f in files if f.endswith(".txt")]

def main():
    files = ['pierwszy.txt', 'drugi.txt', 'ten powinien być usunięty.zip']
    filtered = extension(files)
    print(filtered)

if __name__ == "__main__":
    main()