#! python3
# bulletPointAdder.py - クリップボードの各行に
# 点を打って、Wikipediaの箇条書きにする

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)
