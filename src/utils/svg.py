import regex as re
from utils.file import appendFile


def generatorEngine(tag, attrs, data, value):
    for attr, dataType in attrs.items():
        if(dataType == int):
            num = re.search(f'(?<=\s*{attr}\s*=\s*\")\d*?.\d*?(?=\")',value)
            if num:
                data[attr] = int(num[0])
        elif(dataType == float):
            num = re.search(f'(?<=\s*{attr}\s*=\s*\")\d*?.\d*?(?=\")',value)
            if num:
                data[attr] = float(num[0])
        elif(dataType == str):
            word = re.search(f'(?<=[^a-zA-Z]{attr}\s*=\s*\").*?(?=\")',value)
            if word:
                data[attr] = str(word[0])
        else:
            raise Exception(f'Data Type of attribute {tag} do not have {dataType}')
    # appendFile(f'{tag}={data}')
    return [tag,data]


'''
<line x1="0" y1="0" x2="200" y2="200" stroke="white" stroke-width="3" />
'''
def line(value):
    attrs = { "x1": float,  "x2": float,  "y1": float,  "y2": float, "stroke": str,  "stroke-width": float }
    data = { "x1": 0,  "x2": 0,  "y1": 100,  "y2": 100,  "stroke": "white",  "stroke-width": 1 }
    return generatorEngine('line', attrs, data, value)


'''
<polyline points="20,20 40,25 60,40 80,120 120,140 200,180" stroke="pink" stroke-width="3"/>
'''
def polyline(value):
    attrs = { "points": str, "stroke": str,  "stroke-width": float }
    data = { "points": "20,20 40,40 80,80",  "stroke": "white",  "stroke-width": 1 }
    return generatorEngine("polyline", attrs, data, value)

'''
<polygon points="200,10 250,190 160,210" stroke="yellow" stroke-width="3" fill="white" />
'''
def polygon(value):
    attrs = { "points": str, "stroke": str,  "stroke-width": float, "fill": str }
    data = { "points": "200,10 250,190 160,210",  "stroke": "white",  "stroke-width": 1, "fill": "white" }
    return generatorEngine("polygon", attrs, data, value)


'''
<rect x="-400" y="0" width="300" height="100" stroke="black" stroke-width="3" fill="white" />
rounded border ot supported
'''
def rect(value):
    attrs = { "x": float, "y": float, "width": float, "height": float, "stroke": str, "stroke-width": float, "fill": str }
    data = { "x": 0, "y": 0, "width": 300, "height": 100,  "stroke": "white",  "stroke-width": 1, "fill": "white" }
    return generatorEngine("rect", attrs, data, value)


def path(value):
    attrs = { "d": str, "stroke": str, "stroke-width": float, "fill": str }
    data = { "d": "M 10 10 C 20 20, 40 20, 50 10",  "stroke": "white",  "stroke-width": 1, "fill": "white" }
    return generatorEngine("path", attrs, data, value)


'''
<circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="white" />
'''
def circle(value):
    attrs = { "cx": float,  "cy": float,  "r": float,  "stroke": str,  "stroke-width": float,  "fill": str }
    data = { "cx": 0,  "cy": 0,  "r": 5,  "stroke": "white",  "stroke-width": 1,  "fill": "white" }
    return generatorEngine("circle", attrs, data, value)


def text(value):
    attrs = { "x": float,  "y": float,  "font-size": int,  "font-family": str,  "font-style": str,  "fill": str, "data": str }
    data = { "x": 0,  "y": 0,  "font-size": 16,  "font-family": "sans-serif",  "font-style": "normal",  "fill": "#434343", "data": "" }
    return generatorEngine("text", attrs, data, value)


# identify tags
def extractTag(tag, value):
    if(tag == "line"):
        return line(value)
    elif(tag == "circle"):
        return circle(value)
    elif(tag == "rect"):
        return rect(value)
    elif(tag == "polyline"):
        return polyline(value)
    elif(tag == "polygon"):
        return polygon(value)
    elif(tag == "path"):
        return path(value)
    elif(tag == "text"):
        return text(value)
    else:
        raise Exception(f'Unable to parse {tag}')