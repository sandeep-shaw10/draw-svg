import regex as re
from utils.maths.curve import bezeirCurve

'''
((M|L|m|l)\s*\-?\d+\.?\d*\s*\,?\s*\-?\d+\.?\d*)|((h|H|v|V)\s*\d+\.?\d+)|(z|Z)

\s*\-?\d+\.?\d*\s*\,?\s*(\-?\d+|\d*)\.?\d*)
'''

# line commans
m = '((M|m|l|L)\s*(\-?\d+|\d*)\.?\d*\s*\,?\s*(\-?\d+|\d*)\.?\d*)' #moveTo
# l = '((L|l)\s*\-?\d+\.?\d*\s*\,?\s*\-?\d+\.?\d*)' # Line
hv = '((h|H|v|V)\s*\d+\.?\d+)'          #horizontal and vertical 
c = '(c|C)(\s*\-?\d*\.?\s*\d*\s*(\,|\s*)){6}'     # Bézier Curves
z = '(z|Z)'                                 #end of command


def strFloatList(pattern):
    test = pattern[1:].replace("-", " -").strip()                   # c-19.6 17.71-41.1 39.17-58.1 64.42  "Minus Gap"
    # print(test, pattern)
    test = re.sub('((-?\d+|\d*)\.(\d*))', '\\1 ', test).strip()     #c.5 1.99.7 4.04.7 6.24 "Adding space to point"
    # print(test, pattern)
    test = re.sub('(\,|\s+)', ",", test)
    # print(test, pattern)
    return [float(x) for x in test.strip().split(',')]




def lineCommand(d):
    regexCMD = f'{m}|{hv}|{c}|{z}'
    d = d.replace('-.','-0.')
    patterns = re.search(regexCMD,d)
    print(d)

    data = list()       # List of command
    ref_x, ref_y = 0,0  # For relavtive command
    start_x, start_y = 0,0      # start point for each m

    if patterns:
        for pattern in re.finditer(regexCMD,d):

            cmdVal = pattern[0][0]

            if(cmdVal == 'z' or cmdVal == 'Z'):
                data.append({"cmd":"z", "value":[start_x, start_y]})

            # moveTo
            if(cmdVal == 'm' or cmdVal == 'M'):
                point = strFloatList(pattern[0])
                print('MOVE TO ',point)
                data.append({ "cmd":"m", "value":point})
                start_x, start_y = point[0], point[1]
                ref_x, ref_y = start_x, start_y
                print(ref_x,ref_y)

            # l : relative: lineTo
            if(cmdVal == 'l'):
                point = strFloatList(pattern[0])
                ref_x += point[0]
                ref_y += point[1]
                data.append({ "cmd":"ll", "value":[ref_x, ref_y]})

            # L : absolute: lineTo
            if(cmdVal == 'L'):
                point = strFloatList(pattern[0])
                ref_x = point[0]
                ref_y = point[1]
                data.append({"cmd":"lL" ,"value":point})

            # h : relative: horizontal
            if(cmdVal == 'h'):
                point = strFloatList(pattern[0])
                ref_x += point[0]
                data.append({"cmd":"lh", "value":[ref_x, ref_y]})

            # H : absolute: horizontal
            if(cmdVal == 'H'):
                point = strFloatList(pattern[0])
                ref_x = point[0]
                data.append({ "cmd":"lH", "value":[point[0], ref_y]})

            # v : relative: vertical
            if(cmdVal == 'v'):
                point = strFloatList(pattern[0])
                ref_y += point[0]
                data.append({ "cmd":"lv", "value":[ref_x, ref_y]})

            # V : absolute: vertical
            if(cmdVal == 'V'):
                point = strFloatList(pattern[0])
                ref_y = point[0]
                data.append({ "cmd":"lV", "value":[ref_x, point[0]]})

            # c : relative: Bézier Curves
            if(cmdVal == 'c'):
                point = strFloatList(pattern[0])
                print(point, pattern[0])
                pt1 = [ref_x, ref_y]
                pt2 = [ref_x + point[0], ref_y + point[1]]
                pt3 = [ref_x + point[2], ref_y + point[3]]
                pt4 = [ref_x + point[4], ref_y + point[5]]
                ref_x += point[4]
                ref_y += point[5]
                plot = bezeirCurve(pt1, pt2, pt3, pt4, 100)
                plot = plot.getPoint()
                data.append({ "cmd":"c", "value": plot})

            # C : absolute: Bézier Curves
            if(cmdVal == 'C'):
                point = strFloatList(pattern[0])
                pt1 = [ref_x, ref_y]
                pt2 = [point[0],point[1]]
                pt3 = [point[2],point[3]]
                pt4 = [point[4],point[5]]
                ref_x, ref_y = point[4], point[5]
                plot = bezeirCurve(pt1, pt2, pt3, pt4, 10)
                plot = plot.getPoint()
                data.append({ "cmd":"c", "value": plot})       
            

            # data.append(pattern[0])
    print(data)
    return data
    