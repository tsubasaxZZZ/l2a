from microsofttranslator import Translator

class TranslateBing:
    
    def __init__(self):
        self.bing = Translator('l2a', '9W6zDb3DBJ77SCjWPOHZsp5y75j5gJvu0z0pjn9zdHk=')

    def translate(self, source, lang=None):
        return(self.bing.translate(source, "ja"))

if __name__ == "__main__":
    a = TranslateBing()
    a.en2ja("Hello")
