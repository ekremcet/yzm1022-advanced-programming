"""
Lab Session 3B — Question 1: Text Analytics Processor
See README.md for requirements. Do NOT modify the test code below.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME: 
STUDENT ID: 
"""


# YOUR CODE HERE


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Text Analytics Processor ===")

    processor = TextProcessor()
    text = "The quick brown fox jumps over the lazy dog. The fox is quick."

    print(f"\nOriginal text: {text}")

    # Word counts
    counts = processor.word_count(text)
    print(f"\nWord counts:")
    print(counts)

    # Unique words
    unique = processor.unique_words(text)
    print(f"\nUnique words ({len(unique)} total):")
    print(sorted(unique))

    # Filter by length
    print(f"\nWords with 4+ characters:")
    long_words = list(processor.filter_by_length(text, 4))
    print(", ".join(long_words))

    # Top words
    top = processor.top_words(text, 3)
    print(f"\nTop 3 words by frequency:")
    for i, (word, count) in enumerate(top, 1):
        print(f"{i}. {word} ({count})")

    # File processing
    print(f"\nFile processing test:")
    content = processor.process_file("test.txt")
    print(f"File content: {content}")

    # Exception test
    print(f"\nException test:")
    try:
        processor.word_count("")
    except WordError as e:
        print(f"Error caught: {e}")