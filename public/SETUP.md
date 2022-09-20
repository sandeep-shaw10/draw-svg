# Basic Turtle Operation

## Setup

```py
import turtle

# Set title
turtle.title("SVG")

# Set (width, height, bgColor)
turtle.screensize(bg="orange")
turtle.screensize(500,200) # area turtle can roam

# Set screen size
turtle.setup(520,220)

# end event
turtle.done() #end only one close
```

## Drawing 

```py
#START draw
skk = turtle.Turtle()

skk.pencolor("red")
skk.pensize(5)
skk.speed(1) #speed [1,2,3,4,5,6,7,8,9,10,0] slow=>fast
 
for i in range(4):
    skk.forward(50)
    skk.right(90)
    skk.speed(100+100*i)
#END draw

skk.pencolor("white")
skk.pensize(2)
skk.pu()
```

## End on Clicking Close

```py
turtle.done() #end only one close
```

## End on Clicking Close

```py
turtle.exitonclick() #end on click
```

# Shapes

## Circle

```svg
<circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
```

```py
skk.goto(150,0)
skk.pd()
skk.color("black","red")
skk.pensize(3)
skk.begin_fill()
skk.circle(40)  # circle(<radius>,<angle>, steps(3=>triangle, 4=>square))
skk.end_fill()
skk.pu()
```

## Rectangle

- [ ] Unsupported Rounded Border

```svg
<rect x="-400" y="0" width="300" height="100" stroke="black" stroke-width="3" fill="red" />
```

```py
skk.goto(-400,0)
skk.pd()
skk.color("black","red")
skk.pensize(3)
skk.begin_fill()
skk.fd(300)
skk.right(90)
skk.fd(150)
skk.right(90)
skk.fd(300)
skk.right(90)
skk.fd(150)
skk.end_fill()
skk.pu()
```


## Ellipse
- [ ] Unsupported


## Line

```svg
<line x1="0" y1="0" x2="200" y2="200" stroke="white" stroke-width="3" />
```

```py
skk.goto(0,0)
skk.pd()
skk.color("white")
skk.pensize(3)
skk.goto(200,200)
skk.pu()
```


## Polygon

```svg
<polygon points="200,10 250,190 160,210" stroke="yellow" stroke-width="3" fill="green" />
```

```py
skk.goto(200,10)  #start
skk.pd()
skk.color("yellow","green")
skk.pensize(3)
skk.begin_fill()
skk.goto(250,190) 
skk.goto(160,210)
skk.goto(200,10)  #explicit end
skk.end_fill()
skk.pu()
```


## Polyline

```svg
<polyline points="20,20 40,25 60,40 80,120 120,140 200,180" stroke="pink" stroke-width="3"/>
```

```py
skk.pd()
skk.color("pink")
skk.pensize(3)
skk.goto(20,20)  
skk.goto(40,25) 
skk.goto(60,40)
skk.goto(80,120) 
skk.goto(120,140) 
skk.goto(200,180) 
skk.pu()
```

## Path
The following commands are available for path data:
- [x] M.m = moveto
- [x] L.l = lineto
- [x] H,h = horizontal lineto
- [x] V,v = vertical lineto
- [x] C,c = curveto
- [ ] S,s = smooth curveto
- [ ] Q,q = quadratic Bézier curve
- [ ] T,t = smooth quadratic Bézier curveto
- [ ] A,a = elliptical Arc
- [x] Z,z = closepath

![x](https://www.w3.org/TR/SVG/images/paths/cubic02.png)


# OUTPUT FILE

```txt
[SVG Hai Bahi ,400,800,1]
speed=0
path={'d': 'M228 319.5H12C5.64873 319.5 0.5 314.351 0.5 308V12C0.5 5.64873 5.64873 0.5 12 0.5H159.175C159.571 0.5 159.952 0.656748 160.233 0.936021L239.057 79.2681C239.341 79.5497 239.5 79.9326 239.5 80.3321V308C239.5 314.351 234.351 319.5 228 319.5Z', 'stroke': '#FFC681', 'stroke-width': 1, 'fill': '#FFF9F2'}
path={'d': 'M160.5 1.20711L238.793 79.5H172C165.649 79.5 160.5 74.3513 160.5 68V1.20711Z', 'stroke': '#FFC681', 'stroke-width': 1, 'fill': '#FFF9F2'}
path={'d': 'M68.8438 244.072C69.1738 250.699 74.7344 254.914 83.1387 254.914C92.0254 254.914 97.5352 250.496 97.5352 243.387C97.5352 237.826 94.4121 234.729 86.9727 233.027L82.7578 232.062C78.2129 230.996 76.3594 229.549 76.3594 227.035C76.3594 223.861 79.1523 221.779 83.3672 221.779C87.3789 221.779 90.2227 223.836 90.6797 227.111H96.9512C96.6465 220.84 91.0859 216.447 83.3926 216.447C75.1914 216.447 69.7578 220.865 69.7578 227.467C69.7578 232.9 72.8809 236.176 79.5332 237.699L84.2812 238.791C88.9785 239.883 90.9844 241.508 90.9844 244.174C90.9844 247.297 87.8613 249.557 83.5449 249.557C78.8984 249.557 75.6484 247.424 75.2422 244.072H68.8438Z', 'stroke': 'red', 'stroke-width': 1, 'fill': '#FF8C02'}
title="Hello QWERTY"
bg="blue"
ht=1
path={'d': 'M121.59 254L134.26 217.361H127.278L118.137 246.51H117.705L108.489 217.361H101.252L114.049 254H121.59Z', 'stroke': 'red', 'stroke-width': 1, 'fill': '#FF8C02'}
path={'d': 'M170.731 239.375V234.805H155.522V239.807H164.333L164.307 240.568C164.206 245.748 160.397 249.227 154.811 249.227C148.286 249.227 144.198 244.047 144.198 235.617C144.198 227.314 148.21 222.135 154.608 222.135C159.305 222.135 162.581 224.471 163.901 228.711H170.426C169.258 221.246 163.063 216.447 154.608 216.447C144.173 216.447 137.495 223.938 137.495 235.668C137.495 247.525 144.096 254.914 154.71 254.914C164.485 254.914 170.731 248.846 170.731 239.375Z', 'stroke': 'red', 'stroke-width': 1, 'fill': '#FF8C02'}
path={'d': 'M99 117C96.7909 117 95 118.791 95 121V148.939C94.3386 148.979 93.6717 149 93 149C75.3269 149 61 134.673 61 117C61 99.3269 75.3269 85 93 85C110.673 85 125 99.3269 125 117H99ZM125 117H155C157.209 117 159 118.791 159 121V177C159 179.209 157.209 181 155 181H99C96.7909 181 95 179.209 95 177V148.939C111.741 147.906 125 134.001 125 117Z', 'stroke': 'red', 'stroke-width': 1, 'fill': '#FFC681'}
bg="red"
ht=0
text={'write':'Name', 'move':'True', 'align':'center', 'fontName':'Verdana', 'fontSize':'12', 'fontType':'bold'}
```

# TEXT
```svg
<svg width="240" height="320" viewBox="0 0 240 320" fill="none" xmlns="http://www.w3.org/2000/svg">
  <text x="20" y="135" class="small" font-size="13" font-family="sans-serif" font-style="normal" >my</text>
  <text x="40" y="135" class="heavy" font-size="30" font-family="sans-serif" font-style="bold" >cat</text>
  <text x="55" y="155" class="small" font-size="13" font-family="sans-serif" font-style="italic" >is</text>
  <text x="65" y="155" class="Rrrrr" font-size="40" fill="red" font-family="serif" font-style="italic" >Grumpy!</text>
</svg>
```