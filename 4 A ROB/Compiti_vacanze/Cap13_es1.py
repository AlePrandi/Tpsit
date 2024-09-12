import string

def process_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.lower()
            line = line.translate(str.maketrans('', '', string.punctuation))
            words = line.split()
            words = [word.strip(string.whitespace) for word in words]
            print(words)

def main():
    file_path = 'Odissea_gutenberg.txt'
    process_text(file_path)

if __name__ == "__main__":
    main()
