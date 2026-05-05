"""
Lab Session 3B — Question 1: Text Analytics Processor
See README.md for requirements. Do NOT modify the test code below.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME: Solution
STUDENT ID: 000000
"""


class WordError(Exception):
    """Raised when text is empty or None"""
    pass


class TextProcessor:
    def word_count(self, text):
        if not text:
            raise WordError("Text cannot be empty or None")
        
        words = text.lower().split()
        # Remove punctuation for proper word counting
        clean_words = [word.rstrip('.,!?;:') for word in words]
        return {word: clean_words.count(word) for word in set(clean_words)}
    
    def unique_words(self, text):
        if not text:
            raise WordError("Text cannot be empty or None")
        
        words = text.lower().split()
        # Remove punctuation for unique word count
        return {word.rstrip('.,!?;:') for word in words}
    
    def filter_by_length(self, text, min_len):
        if not text:
            raise WordError("Text cannot be empty or None")
        
        words = text.split()
        for word in words:
            if len(word) >= min_len:
                yield word
    
    def top_words(self, text, n=5):
        if not text:
            raise WordError("Text cannot be empty or None")
        
        word_counts = self.word_count(text)
        return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:n]
    
    def process_file(self, filename):
        # Write to file, then read it back
        test_content = "Hello world from file!"
        
        with open(filename, 'w') as f:
            f.write(test_content)
        
        with open(filename, 'r') as f:
            return f.read()


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