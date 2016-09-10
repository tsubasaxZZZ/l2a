from microsofttranslator import Translator

class TranslateBing:
    
    def __init__(self, logger):
        self.bing = Translator('l2a', '9W6zDb3DBJ77SCjWPOHZsp5y75j5gJvu0z0pjn9zdHk=')
        self.logger = logger.getChild(__name__)

    def translate(self, source, to_lang=None):
        self.logger.debug(source)
        if(not to_lang):
            to_lang = "ja" if self.bing.detect_language(source) == "en" else "en"
        return(self.bing.translate(source, to_lang))

if __name__ == "__main__":
    a = TranslateBing()
    a.en2ja("Hello")
