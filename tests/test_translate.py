# coding: utf-8

#from translates import translate
#from translates import *
from translates.translate import Translate
from translates.translatebing import TranslateBing
from nose.tools import *

from logging import getLogger,StreamHandler,DEBUG,Formatter

class TestTranslate:
    def setup(self):
        formatter = Formatter('%(asctime)s - %(name)s.%(funcName)s():%(lineno)s - %(levelname)s - %(message)s')

        handler = StreamHandler()
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)

        self.logger = getLogger(__name__)
        self.logger.setLevel(DEBUG)
        self.logger.addHandler(handler)

    def test_translatebing_en2ja(self):
        bing = TranslateBing(self.logger)

        t = bing.translate("Hello")
        print(t)
        assert(t == "こんにちは")

        t = bing.translate("こんにちは")
        print(t)
        assert(t == "Hello")

        t = bing.translate("こんにちは", "en")
        print(t)
        assert(t == "Hello")

        t = bing.translate("Hello", "ja")
        print(t)
        assert(t == "こんにちは")


        
        
