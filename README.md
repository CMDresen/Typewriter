# Typewriter
 A program to generate image files containing TINY text.

Made in Python 3.9.6 using the PIL library.

Typerwriter is a program I created while experimenting with pixel art. I was running in to an issue where traditional fonts were too abstract; too difficult to control, in terms of their size and dimensions.
Many common system fonts are created by rendering the characters as vectors - as such, these fonts don't translate well to pixel-based editors, such as Paint.net.
I wanted to achieve two goals: make the smallest text possible in pixel art, and to be in control of every pixel of that text.
To that end, I created Typewriter.
This program takes in strings from a text file, and outputs them as image files, where the text is rendered in the smallest legible pixel art I could achieve. 
Every text character is a maximum of 5 pixels tall - PERFECT for granular pixel art.

HOW TO USE:
1. Enter the text you would like to convert to pixel art in the "WRITE TEXT HERE.txt" file. Each line of text will be output as its own image.
2. Run the python file "typewriter.py".
3. Your images will be output to the "Output" folder.
4. That's it!