
import re
from re import split
c=open('python_class_test.html')
text=c.read()
colours=[]
frequency={ }


colour_1=re.findall('ARSH',text)
colour_2=re.findall('YELLOW',text)
colour_3=re.findall('CREAM',text)
colour_4=re.findall('WHITE',text)
colour_5=re.findall('BLUE',text)
colour_6=re.findall('ORANGE',text)
colour_7=re.findall('BLACK',text)
colour_8=re.findall('GREEN',text)
colour_9=re.findall('BROWN',text)
colour_10=re.findall('PINK',text)
colour_11=re.findall('RED',text)
colour_12=re.findall('BLEW',text)


colour=(colour_1,colour_2,colour_3,colour_4,colour_5,colour_6,
      colour_7,colour_8,colour_9,colour_10,colour_11,colour_12)
print(colour)


c=[]
for a in colour:
    for b in a:
        c.append(b)
print(c)
print(len(c))

frequency={"YELLOW":0,"BROWN":0,"WHITE":0,"BLUE":0,"BLACK":0,"ORANGE":0,
          "GREEN":0,"PINK":0,"RED":0,"ARSH":0,"BLEW":0,"CREAM":0}
for color in c:
 if color in frequency:
    frequency[color]+=1
else:
    frequency[color]=1
print(frequency)

# frequency={"YELLOW":5,"BROWN":6,"WHITE":16,"BLUE":30,"BLACK":1,"ORANGE":9,
#            "GREEN":10,"PINK":5,"RED":9,"ARSH":1,"BLEW":1,"CREAM":2}

import statistics
#QUESTION 1
MEAN_COLOUR=len(c)/len(color)
print(MEAN_COLOUR)

#QUESTION2
MOSTLY_WORN_COLOUR='BLUE'

#QUESTION3
MEDIAN_COLOUR =statistics.median(c)
print(MEDIAN_COLOUR)

#QUESTION4
# VARIANCE_COLOUR=statistics.variance(c)

#QUESTION5
PROBABILITY_OF_RED= len(colour_11)/len(c)
print(PROBABILITY_OF_RED)
