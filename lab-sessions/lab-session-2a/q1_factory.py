"""
Lab Session 2 — Question 1: Document Factory (30 pts)
See README.md for requirements. Do NOT modify the test code below.
"""


# YOUR CODE HERE


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Document Factory ===")

    creators = [
        (PDFCreator(), "Annual Report", "report"),
        (WordCreator(), "Meeting Notes", "notes"),
        (HTMLCreator(), "Web Page", "page"),
    ]

    for creator, content, filename in creators:
        prefix = creator.create_document().extension.upper()
        print(f"{prefix}: {creator.generate(content)}")

    print()
    for creator, content, filename in creators:
        doc = creator.create_document()
        print(f"{doc.extension.upper()} saved to: {doc.save(filename)}")
