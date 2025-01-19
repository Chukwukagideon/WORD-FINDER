import chardet

word_to_find = input("Type word to find: ")

def detect_encoding(filename):
    """Function to detect the encoding using in the specified document"""
    with open(filename, "rb") as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result["encoding"]
        return encoding

# Get encoding used and store it
encoding_used = detect_encoding("spirit of iron.txt")


def book_reader(filename):
    """A simple function to read the contents of a file."""
    # handle errors that may arise from missing files.
    try:
        with open(filename, encoding=encoding_used) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print("Requested file not found.")
    else:
        return content


def word_occurrence(content, word_to_find):
    """A function to show all occurrence of the specified word without the context where it was used."""
    # check if the content is valid. If not, do nothing and exit the function.
    if content is None:
        pass
        return

    # count the number of times the specified word appeared
    print(f"The word {word_to_find} appears {content.lower().count(word_to_find.lower())} times.")

    # convert the content in the file into a list
    words = content.split()

    # show all occurrence of the requested word without their context
    for word in words:
        if word == word_to_find:
            print(word)


def word_finder(content, word_to_find):
    """A function to find specified words from a file and show the context in which it appears."""
    # check if the content is valid. If not, do nothing and exit the function.
    if content is None:
        pass
        return

    # splits the text into sentences based on the period and space delimiter and coverts it to a list.
    sentences = content.split(". ")
    occurrence = 0

    # Show all occurrences of the requested word within their context
    for sentence in sentences:
        if word_to_find.lower() in sentence.lower():
            occurrence += 1
            print(f"Appearances {occurrence} : {sentence}")
    print(f"\nTotal number of appearance: {occurrence}")


print()

read_book = book_reader("spirit of iron.txt")
word_occurrence(read_book, word_to_find)
print()

word_finder(read_book, word_to_find)


# things to do:

# add a function that gets the encoding of the document to be searched
# also ask the user for name of document. add a note that the document should be in
# the same location as the word finder code