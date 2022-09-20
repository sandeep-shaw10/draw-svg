import regex as re
from utils.maths.random import randomKey


RE_CHECK = '\<\s*text.+?\>.*?\<\s*\/\s*text\s*\>'
RE_ATTR = '<\s*text.+?>'
RE_DATA = '(?<=\<\s*text\s*.*\s*\>\s*).*?(?=\s*\<\s*\/\s*text\s*\>)'
MOVE = False
ALIGN = 'left'

def initText():
    return [MOVE, ALIGN]


def modifyText(data):
    exist = re.search(RE_CHECK, data)
    if exist:
        for text in re.finditer(RE_CHECK, data):
            attr = re.search(RE_ATTR, text[0])
            dataVal = re.search(RE_DATA, text[0])
            key = randomKey()
            val = attr[0].replace('>', f' data=\"{key}\" />')
            val = val.replace(key, dataVal[0])
            data = data.replace(text[0],val)
        return data
    else:
        return data


'''
<text x="65" y="55" class="Rrrrr" font-size="40" fill="red" font-family="serif" font-style="italic">
    Grumpy!
</text>
'''

'''
<text x="65" y="55" class="Rrrrr" font-size="40" fill="red" font-family="serif" font-style="italic" data="Grumpy!"/>
'''
