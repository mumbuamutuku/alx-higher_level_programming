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

**4-rectangle.py** - Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)

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
<li>repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()</li>
<li> You are not allowed to import any module </li>
</ul>


**5-rectangle.py** - Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)

<ul> <li> Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted</li> </ul>

**6-rectangle.py** - Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)

<ul><li>Public class attribute number_of_instances:
<ul> <li> Initialized to 0 </li>
<li> Incremented during each new instance instantiation </li>
<li> Decremented during each instance deletion </li></ul></li></ul>

**7-rectangle.py** - Write a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)

<ul>    <li>Public class attribute print_symbol: 
<ul>    <li> Initialized to # </li>
        <li> Used as symbol for string representation </li>
        <li> Can be any type </li> </ul></li> 
</ul>

**8-rectangle.py** -Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)

**Compare rectangles**
<ul><li>Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
<ul>
<li> rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle</li>
<li>rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
</li></ul></li>
</ul>

**9-rectangle.py** - Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)

**A square is a rectangle**
<ul><li> Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size </li></ul>