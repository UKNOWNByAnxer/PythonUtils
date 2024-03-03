def analyzer_text(text):
    # Characters count (including spaces)
    num_characters = len(text)

    # Word counting
    words = text.split()
    num_words = len(words)

    # Line counting
    lines = text.split('\n')
    num_lines = len(lines)

    # Paragraph count (separated by blank lines)
    paragraphs = text.split('\n\n')
    num_paragraphs = len(paragraphs)

    return {
        "Number of characters": num_characters,
        "Number of words": num_words,
        "Number of lines": num_lines,
        "Number of paragraphs": num_paragraphs
    }

def main():
    archive = input("Enter the name of the text file with extension:\n")
    try:
        with open(archive, 'r') as file:
            text = file.read()
        result = analyzer_text(text)
        print("\nText analysis:")
        for clave, valor in result.items():
            print(f"{clave}: {valor}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
    input('\n')