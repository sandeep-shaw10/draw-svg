<p align="center">
	<img alt="draw svg" src="https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png" width="180">
	<h2 align="center">DRAW SVG</h2>
</p>

<p align="center">
Minimal SVG using Python Turtle
</p>

<p align="center">
	<a href="version">
		<img alt="v1" src="https://img.shields.io/badge/version-v1.0-orange.svg" />
	</a>
    <a href="link to license">
		<img alt="mit-license" src="https://img.shields.io/badge/License-MIT-green.svg" />
	</a>
	<a href="link to license">
		<img alt="mit-license" src="https://img.shields.io/badge/Version-Alpha-red.svg" />
	</a>
</p>

<br/><br/>

![SVG](./path.svg)


# Getting Started
- Setup [Click Here](#setup)
- Working of different Tag [Click Here](#customizing)
- Issues [Click Here](#unresolved)

# Setup

## Git Clone

```cmd
git clone https://github.com/sandeep-shaw10/draw-svg.git
cd draw-svg
```

## Set Virtual Environment

```cmd
python -m venv venv
```

## Activate Virtual Environment

```cmd
source venv/Scripts/activate
```

## Install Dependency

```cmd
pip install -r requirements.txt
```

# Running Command

## `python src/index.py draw`
```py
# Draw from the existing Decoded file
'Enter File Path:' data/bash
```

![](./public/sample.gif)

## `python src/index.py decode`
```py
# Convert the SVG file into Decoded File
'Enter SVG Input Path:' target.svg
'Enter Output Path:' output_path
```

## `python src/index.py run`
```py
# It creates and draw the file together
'Enter SVG Input Path:' target.svg
'Enter Output Path:' output_path
```

# Customizing

## Basic Turtle Window Generation

Create a file say `example`

```txt
[Turtle Logo Draw Basic,1200,600,True] 
bg="#343434"
ht=True
```

Run the command

```sh
python src/index.py draw
Enter File Path: example
```

Output

![](./public/example.jpg)

## Decoded File Format

First Line
```py
[<initial title>,<width>,<height>,<True || False>]
# No spaces between comma(',') and no (" , ')
# True => Hide on Click
# False => Hide on Button Close
```

Appearance Commands
```py
# Changes Background Colour
bg="#343434"

# True: Hide Turtle | False: Show Turtle
ht=True

# Set the Title of the Turtle Window
title="Drawing Complete"

# Set the Speed of Turtle
# Turtle’s speed range (0-10).
# Speedstrings  are mapped to speedvalues in the following way:
## ‘fastest’ :  0
## ‘fast’    :  10
## ‘normal’  :  6
## ‘slow’    :  3
## ‘slowest’ :  1
speed=0
```

## Shape Generation 

Shapes Drawing Command: `line`, `polyline`, `polygon`, `rect`, `circle`, `path`, `text`

### Lines

```svg
<line x1="0" y1="0" x2="200" y2="200" stroke="white" stroke-width="3" />
```

```txt
```

Exceptions
- Inline Styles Only 

### PolyLine

```svg
```

```txt
```

Exceptions
- Inline Styles Only 

### Polygon

```svg
```

```txt
```

Exceptions
- Inline Styles Only 

### Rect

```svg
```

```txt
```

Exceptions
- Inline Styles Only 

### Circle

```svg
```

```txt
```

Exceptions
- Inline Styles Only 

### Path

```svg
```

```txt
```

Exceptions
- Inline Styles Only 

### Text

```svg
```

```txt
```

Exceptions
- Inline Styles Only 

# Unresolved

- [ ] Float dimension
- [ ] `fill: none`
- [ ] Some Regex related problems for 
    - d="...." in path grabbing the id="xxx"
    - Various in paths like `M120,200` `M 120 200`, etcs
- [ ] Rectangular Rounded
- [ ] Curves
    - `A` : Arcs
    - `Q`
    - `S`
    - `T`
- [ ] Working with Group `<g>...</g>` to add the attributes of group into each child member 
- [ ] Works only with inline Styling


# Authors

- [@sandeep-shaw10](https://www.github.com/sandeep-shaw10)
