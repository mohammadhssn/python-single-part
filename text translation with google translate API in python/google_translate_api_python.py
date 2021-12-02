"""
    text translation with google translate API in python

    'pip install googletrans'

        link = https://github.com/ssut/py-googletrans
"""

from googletrans import LANGUAGES, Translator

print(LANGUAGES)  # all language
gt = Translator()

translation = gt.translate('خوبید', 'en', 'fa')

print(translation.text)
