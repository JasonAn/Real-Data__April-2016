import numpy as np
import sys
import re

userinput = sys.stdin.readline()
#words = userinput.split()
words = re.findall(r"[\w']+|[.,!?;]", userinput)

eng_string = ['the', 'be', 'to', 'of', 'and']
french_string = ['etre', 'avoir', 'je', 'ne','pas']
german_string = ['das', 'ist', 'du', 'ich', 'nicht']
spanish_string = ['el', 'que', 'y', 'en', 'un']

detection = np.zeros(4)

for word in words:
    word = word.lower()
    for i in range(5):
        weight = 2 ** (5 - i)
        if word == eng_string[i]:
            detection[0] += weight
        elif word == french_string[i]:
            detection[1] += weight
        elif word == german_string[i]:
            detection[2] += weight
        elif word == spanish_string[i]:
            detection[3] += weight
        else:
            continue

if 0 == np.argmax(detection):
    print 'English'
elif 1 == np.argmax(detection):
    print 'French'
elif 2 == np.argmax(detection):
    print 'German'
elif 3 == np.argmax(detection):
    print 'Spanish'

