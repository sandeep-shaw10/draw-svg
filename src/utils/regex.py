import regex as re
from utils.svg import extractTag
from utils.file import appendFile, writeFile


def makeTag(tagName):
    return f'(<\s*{tagName}\s*).+?(\s*\/\s*\>)'


# Extract valid svg tagSvg
def extractSVG(data, filePath):
    tagSvg = ['path','circle','polygon','polyline','rect','line']

    cmdRegex = ''
    for i in range(0,len(tagSvg)):
        if(i == len(tagSvg)-1):
            cmdRegex += makeTag(tagSvg[i])
        else:
            cmdRegex += f'{makeTag(tagSvg[i])}|'

    patterns = re.search(cmdRegex,data)
    if patterns:
        for pattern in re.finditer(cmdRegex,data):
            tag = re.search('(?<=\<)\w+', pattern[0])
            [data_tag, data_attr] = extractTag(tag[0], pattern[0])
            writeFile(f'{data_tag}={data_attr}', filePath)


# Validify SVG and get width and height
def extractDim(val, filePath, WIDTH=200, HEIGHT=200):

    val = re.sub('<!--.*-->', '', val)      # remove comment
    #replace none
    valid = re.search('(?<=\<\s*svg\s*.*\s*\>\s*).*?(?=\s*\<\s*\/\s*svg\s*\>)',val)

    DIMENSION = { "width": WIDTH, "height": HEIGHT }
    
    if valid:
        width = re.search('(?<=\<\s*svg\s*.*\s+width\s*=\s*[\"\']\s*)\d*?(?=\s*(px|em|pt|rem|)[\"\'])',val)
        height = re.search('(?<=\<\s*svg\s*.*\s+height\s*=\s*[\"\']\s*)\d*?(?=\s*(px|em|pt|rem|)[\"\'])',val)
        if(width and height):
            DIMENSION["width"], DIMENSION["height"] = width[0], height[0]
        elif(width):
            DIMENSION["width"] = width 
        elif(height):
            DIMENSION["height"] = height
        else:
            pass
        appendFile(f'[Svg Draw v1.0,{DIMENSION["width"]},{DIMENSION["height"]},False]', filePath)
        extractSVG(valid[0], filePath)
    else:
        raise Exception("Failed to extract SVG")
