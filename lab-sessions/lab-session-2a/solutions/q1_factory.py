"""Lab Session 2 — Q1 Solution: Document Factory"""
from abc import ABC, abstractmethod


class Document(ABC):
    @abstractmethod
    def create(self) -> str:
        pass

    @abstractmethod
    def save(self, filename: str) -> str:
        pass

    @property
    @abstractmethod
    def extension(self) -> str:
        pass


class PDFDocument(Document):
    def create(self): return "Creating PDF document"
    def save(self, filename): return f"{filename}.{self.extension}"
    @property
    def extension(self): return "pdf"


class WordDocument(Document):
    def create(self): return "Creating Word document"
    def save(self, filename): return f"{filename}.{self.extension}"
    @property
    def extension(self): return "docx"


class HTMLDocument(Document):
    def create(self): return "Creating HTML document"
    def save(self, filename): return f"{filename}.{self.extension}"
    @property
    def extension(self): return "html"


class DocumentCreator(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        pass

    def generate(self, content: str) -> str:
        doc = self.create_document()
        return f"{doc.create()} with content: {content}"


class PDFCreator(DocumentCreator):
    def create_document(self): return PDFDocument()

class WordCreator(DocumentCreator):
    def create_document(self): return WordDocument()

class HTMLCreator(DocumentCreator):
    def create_document(self): return HTMLDocument()


if __name__ == "__main__":
    print("=== Document Factory ===")
    creators = [(PDFCreator(), "Annual Report", "report"),
                (WordCreator(), "Meeting Notes", "notes"),
                (HTMLCreator(), "Web Page", "page")]
    for creator, content, filename in creators:
        prefix = creator.create_document().extension.upper()
        print(f"{prefix}: {creator.generate(content)}")
    print()
    for creator, content, filename in creators:
        doc = creator.create_document()
        print(f"{doc.extension.upper()} saved to: {doc.save(filename)}")
