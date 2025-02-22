# Typewriter
 A program to generate image files containing TINY pixel-based text.

Made in Python 3.9.6 using the PIL library.

Typerwriter is a program I created while experimenting with pixel art. I was running in to an issue where traditional fonts were too difficult to control.
Many common system fonts are created by rendering the characters as vectors - as such, these fonts don't translate well to pixel-based editors, such as Paint.net.
Therefore, I created Typewriter, in order to be able to consistently render the smallest text possible in pixel art.

This program takes in strings from a text file, and outputs them as image files, where the text is rendered in the smallest legible text I could achieve. 
Every character is a MAXIMUM of 5 pixels tall - PERFECT for granular pixel art.

HOW TO USE:
1. Enter the text you would like to convert to pixel art in the "WRITE TEXT HERE.txt" file. Each line of text will be output as its own image.
2. Run the python file "typewriter.py".
3. Your images will be output to the "Output" folder.
4. That's it!
