def word_counter():
    text = input("Enter a string: ")
    word_count = len(text.split())
    char_count = len(text)
    print(f"Words: {word_count}, Characters: {char_count}")

word_counter()
