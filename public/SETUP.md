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


# TEXT
```svg
<svg width="240" height="320" viewBox="0 0 240 320" fill="none" xmlns="http://www.w3.org/2000/svg">
  <text x="20" y="135" class="small" font-size="13" font-family="sans-serif" font-style="normal" >my</text>
  <text x="40" y="135" class="heavy" font-size="30" font-family="sans-serif" font-style="bold" >cat</text>
  <text x="55" y="155" class="small" font-size="13" font-family="sans-serif" font-style="italic" >is</text>
  <text x="65" y="155" class="Rrrrr" font-size="40" fill="red" font-family="serif" font-style="italic" >Grumpy!</text>
</svg>
```