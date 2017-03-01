# CSS Positioning & Layout

### Lesson Objectives
By the end of this lesson students will be able to: 

- Explain the CSS Box Model (lecture)
- Adjust element spacing using padding and margin (lab)
- Describe the difference between block, inline-block, and inline elements (lab)

- Explain the difference between and use cases of: static, relative, fixed, & absolute positioning (maybe)

- Create floating elements to position content removed from the standard document flow (header, then switch to flexbox)

**Lab:**
- Explain what flexbox is
- Use flexbox to position content on webpages

### Review
- Difference between block, inline, and inline-block elements.
- Classes vs id's
- CSS selectors 
  * p.className
  * p .className
  * p, .className
- What makes up a CSS property? (key:value)
- 3 ways to include CSS in a document
  * Inline Style Attribute ```style=""```
  * Inline Style Sheet ```<style>``` Tag 
  * External Style Sheet
- How are CSS rules applied? What's the order of precedence? 

## CSS Box Model
The CSS box model can seem initially difficult to understand, however it's actually quite a simple concept.

Each HTML element you put on the page is essentially a container, or a box for whatever you put inside of it, so for example:

```
<p>Hello, World!</p>
```

- The ```<p>``` tag is a box that contains the text "Hello, World!".
- Every html element is a box that holds content.
- Every html element has multiple layers to it, kind of like an onion, the layers go as follows

- Content: The text "Hello, World"
- Padding: The space between the text and the border.
- Border: The border of the box
- Margin: The space between the html element and it's surrounding content.

When you give an element a height and width, the **content** itself will be that height and width.

What the size doesn't include:

- padding
- border
- margin

![](https://dl.dropboxusercontent.com/s/capg35hblhr6o7v/Screenshot%202015-10-13%2014.11.39.png?dl=0)

You can think of the Box Model like a house where the furniture is the content, the space from the couch to the walls is the padding, the walls around the house is the border, and the yard from house to house is the margin.

- **Margin** - clears an area around the border; the margin does not have a background color, it is completely transparent (yard)
- **Border** - a border that goes around the padding and content; the border is affected by the background color of the box (house walls)
- **Padding** - clears an area around the content; the space between the content and the border; the padding is affected by the background color of the box (space between walls and furniture)
- **Content** - The content of the box, where text and images appear (furniture)

[Interactive Box Model](http://guyroutledge.github.io/box-model/)

#### Box Model Codealong

Let's set up our environment so we can start writing some HTML & CSS to help visualize the box-model.

```
$ mkdir box-model
$ cd box-model
$ touch index.html
$ mkdir css
$ touch style.css
$ cd ..
```

Let's go into our existing `index.html` and `styles.css` and add some stuff to illustrate what I mean. In `index.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Box Model Squares</title>
    <link rel="stylesheet" type="text/css" href="css/styles.css">
  </head>
  <body>
	<p>This is a paragraph</p>
	<p class="padding">This is a paragraph</p>
  </body>
```

In `styles.css`:

```css
p {
  background: red;
  height: 100px;
  width: 20%;
}
```

Let's check this out in our chrome browser with the developer tools. As you can see, everything is identical. Which makes sense. Let's go ahead and add some padding to the html element with class "padding". In `styles.css`:

```css
p {
  background: red;
  height: 100px;
  width: 20%;
}

p.padding {
  padding:10px;
}
```

Let go ahead and add `margin: 10px;` and `border: 10px solid black;` to the padding class as well. Let's inspect that element in the browser and you can see Chrome's clear depiction of content, padding, border and margin.

```css
p {
  background: red;
  border: 10px solid black;
  margin:10px;
  height: 100px;
  width: 20%;
}

p.padding {
  padding:10px;
}
```

#### Active Learning
Pair together in groups of two, Go ahead and draw the box with class `.padding` on your desk, which parts of each box are the content, padding, border & margin?


All these different sizings can be confusing. This can especially be frustrating when you think something's 20 % when in actuality it isn't.  Enter box-sizing.

At the top of our `styles.css`:

```css
* {
  box-sizing: border-box;
}
```

Now when we refresh, all of our 20% widths are the same regardless of padding. It also includes border! However, it does not include the margin. 

* Now go add four divs with separate id's into the html
* Inside our CSS page, make the squares 100px and the following colors: orange, blue, green, and purple

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Box Model Squares</title>
    <link rel="stylesheet" type="text/css" href="css/main.css">
  </head>
  <body>
    <div id="square1">square1</div>
    <div id="square2">square2</div>
    <div id="square3">square3</div>
    <div id="square4">square4</div>
  </body>
</html>
```

```css
#square1 {
  background-color: orange;
  height: 100px;
  width: 100px;
}
#square2 {
  background-color: blue;
  height: 100px;
  width: 100px;
}
#square3 {
  background-color: green;
  height: 100px;
  width: 100px;
}
#square4 {
  background-color: purple;
  height: 100px;
  width: 100px;
}
 ```
 
> In Chrome, inspect elements on existing web pages and view the box model under the "computed" tab


## CSS Properties

#### Property: Border
Borders can be set in two ways: all at once or individually

> WE DO: Let's add some thick borders to our divs

```css
div {
	border: 5px solid black;
}
```

####Property: Margin
There are three ways to set margin with CSS:

```css
 div {
	 margin-top: /*some value*/;
	 margin-right: /*some value*/;
	 margin-bottom: /*some value*/;
	 margin-left: /*some-value*/;
 }
 ```
You can set them all at once:

```css
div{
	margin: 1px 2px 3px 4px; 
}
```

You can do top-bottom and right-left:

```css
div{
	margin: 0 auto;
}
```

What if value is `auto`? This tells the document to automatically put equal left and right margins on our element, centering it on the page, as long as it has a specific width.


> YOU DO: add margin around your squares


####Property: Padding
Padding can be set in two ways (all at once or individually)

```css
div {
	padding: 25px
}
```

#### Property: Box-Sizing
`box-sizing` is a CSS3 property that helps to make building layouts more intuitive for developers.

* **content-box**: Default. The width and height of an element does __not__ include padding or borders
* **border-box**: The width of an element includes the padding and borders (not margin)

> WE DO: Add `box-sizing: border-box` property to the `div`

#### Property: Display
* An **inline** element 
	- respect left & right margins and padding, but not top & bottom
	- cannot have a width and height set
	- allow other elements to sit to their left and right
	- HTML elements inline by default:
		- span 
		- a 
		- img	
* A **block** element
	- respect all marign and padding
	- force a line break after the block element
	- HTML elements inline by default:
		- div
		- h1
		- p
		- header, footer, nav         
* An **inline-block** element
	- allow other elements to sit to their left and right
	- respect top & bottom margins and padding
	- respect height and width
* If you assign **none** as the value of the display, the element and its content disappear from the page entirely! Mention "visibility: hidden" property and how it's different from display: none


### Display Exercise

**You Do (15 min)** 

[Favorite Cities](https://gist.github.com/BritneyJo/0fc7cd6b47bf78892251a39a738eaaea)


### Property: position

* Static is the default value. An element positioned with "position: static" is not positioned in any special way. Follows the natural flow of the document. 

* Relative behaves just like "static" unless you add "top", "bottom", "left", or "right". A page element with relative positioning gives you control to absolutely position children elements inside of it.
	
	```html
	<style type="text/css">
	
	ul {
		position: relative;
		top: 400px;
		left: 50px;
	}
	
	</style>
	```


* Fixed elements are always positioned in the same location, even if the user scrolls. An element with fixed position is positioned relative to the browser window.

	```html
	<!DOCTYPE html>
	<html>
	<head>
	<title>CSS Positioning</title>
	<style type="text/css">
	
	body {
		background: #ccc;
	}
	img {
		position: fixed;
		right: 0;
		bottom: 0;
	}
	
	</style>
	</head>
	<body>
	<ul>
		<li>Austin</li>
		<li>Dallas</li>
		<li>Houston</li>
		<li>Amarillo</li>
	</ul>
	<img src="https://ga-core.s3.amazonaws.com/production/uploads/program/default_image/3677/thumb_thumb_thumb_Partner-Happy-Hours-General.jpg" alt="">
	</body>
	</html>
	```

* Absolute elements are removed from the normal flow and can overlap other elements. They are positioned relative to the browser window unless a parent element is position: relative.

	```html
	<!DOCTYPE html>
	<html>
	<head>
	<title>CSS Positioning</title>
	<style type="text/css">
	
	body {
		background: #ccc;
	}
	ul {
		position: relative;
	}
	li {
		height: 100px;
	}
	img {
		position: fixed;
		right: 0;
		bottom: 0;
	}
	.relative {
		position: relative;
		left: 150px;
	}
	.absolute {
		position: absolute;
		left: 150px;
	}
	
	</style>
	</head>
	<body>
	<ul>
		<li>Austin</li>
		<li>Dallas</li>
		<li class="absolute">Houston</li>
		<li>Amarillo</li>
	</ul>
	<img src="https://ga-core-production-herokuapp-com.global.ssl.fastly.net/assets/ga-lockup-1788582934ade008a8ea6068b784b8ee.png" alt="">
	<footer>&copy; 2015 General Assembly</footer>
	</body>
	</html>
	```

### Positioning Exercise

[Operation](https://github.com/ga-wdi-exercises/positioning_operation)

### Property: width

##### width vs. max-width

##### measurements units:

| Unit | Description                                                                                                                                                                                                                                            |
|:-----|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `px`   | Relative to the viewing device. For screen display, typically one device pixel (dot) of the display. For printers and very high resolution screens one CSS pixel implies multiple device pixels, so that the number of pixel per inch stays around 96. Set size no matter how the viewport or fonts are resized |
| `%`    | Relative to the containing block - Resized as the viewport is changed                                                                                                                                                                                                                      |
| `em`   | Relative to the font-size of the element (2em means 2 times the size of the current font). If you assign a font to 12pt, each "em" unit would be 12pt; thus, 2em would be 24pt.                                                                                                                                                              |
| `rem`  | Relative to font-size of the root element, not any parent element. Thus compounding does not occur as it does with em units.                                                                                                                                                                                                              |
| `vw`   | Relative to 1% of the width of the viewport                                                                                                                                                                                                            |
| `vh`   | Relative to 1% of the height of the viewport 


More reading: http://webdesign.tutsplus.com/articles/7-css-units-you-might-not-know-about--cms-22573

> WE DO: Let's add a section with class of container around our squares and give it a width of 400px and a background-color. How can we get the squares to be 2x2?

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Box Model Squares</title>
    <link rel="stylesheet" type="text/css" href="css/main.css">
  </head>
  <body>
    <section class="container">
      <div id="square1">square1</div>
      <div id="square2">square2</div>
      <div id="square3">square3</div>
      <div id="square4">square4</div>
    </section>
  </body>
</html>
```

```css
.container{
  width: 400px;
  background-color: aqua;
}
```

- `display: inline-block` but that puts 3 on the first line
- adjust their widths to 50%
- remove `margin:0` since margin is on the outside
- to remove that gap, remove spaces in your html `<div id="square1">square1</div><div id="square2">square2</div>`

[Fighting the space between inline block elements](https://css-tricks.com/fighting-the-space-between-inline-block-elements/)

### Property: Float

Using the "float" property, elements can be pushed to the left or right, allowing other elements to wrap around it. Floated elements are also removed from the normal flow. It's like a float toy in a pool - you float left and it will go until it hits a wall or something else. You cannot float a toy to the middle.

> WE DO: add the following styles to your favorite cities. What is the float doing?

```html
<style type="text/css">
body {
	background: #ccc;
}
li {
	background: black;
	color: white;
	width: 250px;
	margin-right: 2px;
	float: left;
	list-style-type: none;
}
img{
	display: block;
}
</style>
```

### Property: Clear

Elements that come after an element that has been floated will flow around it. To get out, use "clear". 

```css
img {
  clear: left;
  display: block;
}
```

##### "clearfix"

The "clearfix" workaround is used on parent containers with floating elements inside of them. Without it, the parent container would not get any height. Add `.clearfix` to the `ul` 
		
```css
.clearfix {
	overflow: auto;
}
```

###The Future: Flexbox

[Flexbox Froggy](http://flexboxfroggy.com)
