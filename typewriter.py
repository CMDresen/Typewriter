import os
from PIL import Image

#Set local directory
current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
os.chdir(current_directory)

#Load Images
a = Image.open('Letters/a.png')
b = Image.open('Letters/b.png')
c = Image.open('Letters/c.png')
d = Image.open('Letters/d.png')
e = Image.open('Letters/e.png')
f = Image.open('Letters/f.png')
g = Image.open('Letters/g.png')
h = Image.open('Letters/h.png')
i = Image.open('Letters/i.png')
j = Image.open('Letters/j.png')
k = Image.open('Letters/k.png')
l = Image.open('Letters/l.png')
m = Image.open('Letters/m.png')
n = Image.open('Letters/n.png')
o = Image.open('Letters/o.png')
p = Image.open('Letters/p.png')
q = Image.open('Letters/q.png')
r = Image.open('Letters/r.png')
s = Image.open('Letters/s.png')
t = Image.open('Letters/t.png')
u = Image.open('Letters/u.png')
v = Image.open('Letters/v.png')
w = Image.open('Letters/w.png')
x = Image.open('Letters/x.png')
y = Image.open('Letters/y.png')
z = Image.open('Letters/z.png')
space = Image.open('Letters/space.png')
comma = Image.open('Letters/comma.png')
topper = Image.open('Letters/topper.png')
asterisk = Image.open('Letters/asterisk.png')
leftBracket = Image.open('Letters/bracketLeft.png')
rightBracket = Image.open('Letters/bracketRight.png')
hashtag = Image.open('Letters/hashtag.png')
plus = Image.open('Letters/operatorPlus.png')
minus = Image.open('Letters/operatorMinus.png')
greaterThan = Image.open('Letters/operatorGreaterThan.png')
lessThan = Image.open('Letters/operatorLessThan.png')
exclamationMark = Image.open('Letters/punctuationExclamation.png')
questionMark = Image.open('Letters/punctuationQuestion.png')
period = Image.open('Letters/punctuationPeriod.png')
colon = Image.open('Letters/punctuationColon.png')
one     = Image.open('Letters/1.png')
two     = Image.open('Letters/2.png')
three   = Image.open('Letters/3.png')
four    = Image.open('Letters/4.png')
five    = Image.open('Letters/5.png')
six     = Image.open('Letters/6.png')
seven   = Image.open('Letters/7.png')
eight   = Image.open('Letters/8.png')
nine    = Image.open('Letters/9.png')

#Dictionary for converting between chars and Images
lettersDict = {
    'a': a,
    'b': b,
    'c': c,
    'd': d,
    'e': e,
    'f': f,
    'g': g,
    'h': h,
    'i': i,
    'j': j,
    'k': k,
    'l': l,
    'm': m,
    'n': n,
    'o': o,
    'p': p,
    'q': q,
    'r': r,
    's': s,
    't': t,
    'u': u,
    'v': v,
    'w': w,
    'x': x,
    'y': y,
    'z': z,
    'A': a,
    'B': b,
    'C': c,
    'D': d,
    'E': e,
    'F': f,
    'G': g,
    'H': h,
    'I': i,
    'J': j,
    'K': k,
    'L': l,
    'M': m,
    'N': n,
    'O': o,
    'P': p,
    'Q': q,
    'R': r,
    'S': s,
    'T': t,
    'U': u,
    'V': v,
    'W': w,
    'X': x,
    'Y': y,
    'Z': z,
    ' ': space,
    ',': comma,
    '\n': topper,
    '*': asterisk,
    '(': leftBracket,
    '[': leftBracket,
    '{': leftBracket,
    ')': rightBracket,
    ']': rightBracket,
    '}': rightBracket,
    '#': hashtag,
    '+': plus,
    '-': minus,
    '>': greaterThan,
    '<': lessThan,
    '!': exclamationMark,
    '?': questionMark,
    '.': period,
    ':': colon,
    '1': one,
    '2': two,
    '3': three,
    '4': four,
    '5': five,
    '6': six,
    '7': seven,
    '8': eight,
    '9': nine,
    '0': o
}


file1 = open('WRITE TEXT HERE.txt', 'r')
lines = file1.readlines()

for line in lines:

    #Break line into list of chars
    lettersChar = list(line)

    #Convert that list into a parallel array of Image objects
    letters = [a] * len(lettersChar)
    lettersIndex = 0
    for currentLetter in lettersChar:
        letters[lettersIndex] = lettersDict[currentLetter]
        lettersIndex += 1


    #Sum up the total width of those same Image objects
    imageWidth = 0
    for letter in letters:
        imageWidth += letter.width

    #Set the height, which, in this version, is always the same
    imageHeight = a.height

    #Create a new image with those dimensions
    word = Image.new('RGB', (imageWidth, imageHeight))

    #The line below is bad Python practice NEVER DO IT
    loopIndex = 0
    #Increment how far along the image's x-axis the next letter needs to be
    pasteDistance = 0

    for letter in letters:
        if(loopIndex > 0):
            pasteDistance += letters[loopIndex - 1].width
        word.paste(letters[loopIndex], (pasteDistance, 0))
        loopIndex += 1

    pasteDistance += letters[loopIndex - 1].width
    # word.paste(topper, (pasteDistance, 0))
    imageTitle = line.rstrip()
    imageTitle.strip(':')
    word.save('Output/' + imageTitle + '.png')