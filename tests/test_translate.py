# coding: utf-8

#from translates import translate
#from translates import *
from translates.translate import Translate
from translates.translatebing import TranslateBing
from nose.tools import *

class TestTranslate:
    def test_translatebing_en2ja(self):
        bing = TranslateBing()
        t = bing.translate("Hello")
        print(t)
        assert(t == "こんにちは")
