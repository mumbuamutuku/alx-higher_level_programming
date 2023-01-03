###### 0x08. Python - More Classes and Objects

**0-rectangle.py** - Write an empty class Rectangle that defines a rectangle:

**1-rectangle.py** - Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

<ul>
<li> Private instance attribute: width:
<ul>
<li> property def width(self): to retrieve it </li>
<li> property setter def width(self, value): to set it: 
    <ul> <li> width must be an integer, otherwise raise a TypeError exception with the message width must be an integer </li>
        <li> if width is less than 0, raise a ValueError exception with the message width must be >= 0 </li> </ul> </li> </ul>
<li> Private instance attribute: height:
    <ul>    <li> property def height(self): to retrieve it </li>
            <li> property setter def height(self, value): to set it: </li>
            <ul>    <li> height must be an integer, otherwise raise a TypeError exception with the message height must be an integer </li>
                    <li> if height is less than 0, raise a ValueError exception with the message height must be >= 0 </li> </ul> </ul></li>
<li> Instantiation with optional width and height: def __init__(self, width=0, height=0): </li>
<li> You are not allowed to import any module </li>
</ul>

**2-rectangle.py** - Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

<ul> <li>
Private instance attribute: width:
<ul>
<li> property def width(self): to retrieve it </li>
<li> property setter def width(self, value): to set it: 
    <ul> <li> width must be an integer, otherwise raise a TypeError exception with the message width must be an integer </li>
        <li> if width is less than 0, raise a ValueError exception with the message width must be >= 0 </li> </ul> </li> </ul></li>
<li> Private instance attribute: height:
    <ul>    <li> property def height(self): to retrieve it </li>
            <li> property setter def height(self, value): to set it: </li>
            <ul>    <li> height must be an integer, otherwise raise a TypeError exception with the message height must be an integer </li>
                    <li> if height is less than 0, raise a ValueError exception with the message height must be >= 0 </li> </ul> </ul></li>
<li> Instantiation with optional width and height: def __init__(self, width=0, height=0): </li>
<li> Public instance method: def area(self): that returns the rectangle area </li>
<li> Public instance method: def perimeter(self): that returns the rectangle perimeter:
<ul><li> if width or height is equal to 0, perimeter is equal to 0 </li></ul></li>
<li> You are not allowed to import any module </li>
</ul>

**3-rectangle.py** - Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)

<ul> <li>
Private instance attribute: width:
<ul>
<li> property def width(self): to retrieve it </li>
<li> property setter def width(self, value): to set it: 
    <ul> <li> width must be an integer, otherwise raise a TypeError exception with the message width must be an integer </li>
        <li> if width is less than 0, raise a ValueError exception with the message width must be >= 0 </li> </ul> </li> </ul></li>
<li> Private instance attribute: height:
    <ul>    <li> property def height(self): to retrieve it </li>
            <li> property setter def height(self, value): to set it: </li>
            <ul>    <li> height must be an integer, otherwise raise a TypeError exception with the message height must be an integer </li>
                    <li> if height is less than 0, raise a ValueError exception with the message height must be >= 0 </li> </ul> </ul></li>
<li> Instantiation with optional width and height: def __init__(self, width=0, height=0): </li>
<li> Public instance method: def area(self): that returns the rectangle area </li>
<li> Public instance method: def perimeter(self): that returns the rectangle perimeter:
<ul><li> if width or height is equal to 0, perimeter is equal to 0 </li></ul></li>
<li>print() and str() should print the rectangle with the character #: (see example below)
<ul>    <li>if width or height is equal to 0, return an empty string</li></ul></li>
<li> You are not allowed to import any module </li>
</ul>