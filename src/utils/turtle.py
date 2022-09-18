from utils.file import simpleReadFile
import ast
import turtle
from utils.tags.path import lineCommand

PATH = 'x.txt'
INVERT = -1


def circle(attr, width, height):
    cx, cy, r, stroke, stroke_width, fill = attr['cx'], attr['cy'], attr['r'], attr['stroke'], attr['stroke-width'], attr['fill']
    print(cx,cy,r,stroke, stroke_width, fill)
    turtle.pu()
    turtle.goto(cx,cy-r)
    turtle.pd()
    turtle.color(stroke,fill)
    turtle.pensize(stroke_width)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.pu()
    print(width, height)


def line(attr):
    x1, y1, x2, y2, stroke, stroke_width = attr['x1'], attr['y1'], attr['x2'], attr['y2'],attr['stroke'], attr['stroke-width']
    print(type(x1),y1,x2,y2,stroke, stroke_width)
    turtle.pu()
    turtle.goto(x1,y1)
    turtle.pd()
    turtle.color(stroke)
    turtle.pensize(stroke_width)
    turtle.goto(x2,y2)
    turtle.pu()


def polyline(attr):
    points, stroke, stroke_width = attr['points'],attr['stroke'], attr['stroke-width']
    print(points, stroke, stroke_width)
    pointer = list(filter(None, points.split(' ')))
    turtle.pu()
    turtle.color(stroke)
    turtle.pensize(stroke_width)
    for i in range(0,len(pointer)):
        try:
            [x,y] = pointer[i].split(',')
            turtle.goto(float(x),float(y))
        except Exception as e:
            print(e)
            print(f'ERROR at {pointer[i]} in {pointer}')
        if(i == 0):
            turtle.pd()
    turtle.pu()


def polygon(attr):
    points, stroke, stroke_width, fill = attr['points'],attr['stroke'], attr['stroke-width'], attr['fill']
    print(type(points), stroke, stroke_width, fill)
    pointer = list(filter(None, points.split(' ')))
    if(len(pointer) > 2):
        turtle.pu()
        try:
            [start_x,start_y] = pointer[0].split(',')
            turtle.goto(float(start_x), float(start_y))
            turtle.pd()
            turtle.color(stroke,fill)
            turtle.pensize(stroke_width)
            turtle.begin_fill()
            rest_point = pointer[1:]
            for i in range(0, len(rest_point)):
                [x,y] = rest_point[i].split(',')
                turtle.goto(float(x),float(y))
            turtle.goto(float(start_x), float(start_y))  #explicit end
            turtle.end_fill()
        except Exception as e:
            print(f'ERROR at {pointer}')
        finally:
            turtle.pu()
    else:
        print(f'In Polygon {pointer} length should be 3 or more')


def rect(attr):
    x, y, width, height, stroke, stroke_width, fill = attr['x'], attr['y'], attr['width'], attr['height'], attr['stroke'], attr['stroke-width'], attr['fill']
    print(type(x), y, width, height, stroke, stroke_width, fill)
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    turtle.color(stroke,fill)
    turtle.pensize(stroke_width)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.right(90)
    turtle.fd(INVERT * height)
    turtle.right(90)
    turtle.fd(width)
    turtle.right(90)
    turtle.fd(INVERT * height)
    turtle.right(90)
    turtle.end_fill()
    turtle.pu()


def path(attr):
    d, stroke, stroke_width, fill = attr['d'],attr['stroke'], attr['stroke-width'], attr['fill']
    # print(type(d), stroke, stroke_width, fill)
    data = lineCommand(d)

    turtle.pu()
    turtle.color(stroke,fill)
    turtle.pensize(stroke_width)
    

    for i in data:
        if(i['cmd'] == 'm'):
            turtle.begin_fill()
            turtle.goto(i['value'][0], i['value'][1])
            turtle.pd()

        elif(i['cmd'] == 'z'):
            turtle.goto(i['value'][0], i['value'][1])
            turtle.end_fill()
            turtle.pu()

        elif(i['cmd'] == "c"):
            for plot in range(len(i['value'])-1,-1,-1):
                turtle.goto(i['value'][plot][0],i['value'][plot][1])

        else:
            turtle.goto(i['value'][0], i['value'][1])

    turtle.end_fill()
    turtle.pu()


def compileSVG(filePath):

    cmds = simpleReadFile(filePath)
    cmds = cmds.split('\n')
    dimension = cmds[0].strip('][').split(',')

    TITLE = dimension[0]
    WIDTH, HEIGHT = float(dimension[1]), float(dimension[2])
    ENDCLICK = dimension[3] in ['true', 'True', 'TRUE', '1']
    cmds = cmds[1:]

    turtle.title(TITLE)
    turtle.screensize(WIDTH-10, HEIGHT-10) # area turtle can roam /remove scrollbar
    turtle.setup(WIDTH, HEIGHT)      # screen area
    turtle.setworldcoordinates(0, HEIGHT, WIDTH,0)

    for cmd in cmds:
        if(len(cmd)):
            data = cmd.split('=')
            tag = data[0]
            attr = ast.literal_eval(data[1])
            # print(tag, attr)
            if(tag == "circle"):
                circle(attr, width, height)
            elif(tag == "line"):
                line(attr)
            elif(tag == "polyline"):
                polyline(attr)
            elif(tag == "polygon"):
                polygon(attr)
            elif(tag == "rect"):
                rect(attr)
            elif(tag == "path"):
                path(attr)
            else:
                raise Exception(f'Extraction of tag {tag} in turtle.py not present')

    if(ENDCLICK):
        turtle.exitonclick()
    else:
        turtle.done()