# Bereken-Pad-Document
### poging 1

'# moet van 11 naar 55 gaan
'# mag niet over een vorig coordinaat zijn gegaan
'# moet het bouwen als een soortvan brug naar 55

def berekenPad(invoer):
    pos = 1.1
    lijst = []
    path = []
    invoer = invoer.lower()
    for x in invoer:
        path.append(pos)
        if x == 'l':
            if pos - 0.1 not in path:
                pos -= 0.1
            else:
                print("can't pass over same coordinate, give possible instructions to solve")
        elif x == 'r':
            if pos + 0.1 not in path:
                pos += 0.1
            else:
                print("can't pass over same coordinate, give possible instructions to solve")
        elif x == 'n':
            if pos + 1 not in path:
                pos += 1
            else:
                print("can't pass over same coordinate, give possible instructions to solve")
        elif x == 'o':
            if pos - 1 not in path:
                pos -= 1
            else:
                print("can't pass over same coordinate, give possible instructions to solve")
        elif x == '?':
           print("solve")
           tempPath = []
        lijst.append(x)
        print(pos)
    if pos == 5.5:
        print("finish")
    else:
        print("didn't finish")
    print(lijst)
    print(path)
    print(pos)


berekenPad("rno")
'# rrnrnrnn
'# R?N?NRNN


#### psuedo code
loop 1
loop 2 true
loop 2
list = [empty]
seed = random
pos = 1.1
invoer = "rnrnrnrnrnr"
loop3
check if list = pos
    if list = pos then loop 2 false
append pos to list
for x in invoer
    if l then pos - 0.1
    if r then pos + 0.1
    if o then pos + 1
    if n then pos - 1
    if ? then
        for x in seed
        if 0-1 then l
        if 2-3 then r
        if 4-5 then o
        if 6-7 then n
        if 8 then r
        if 9 then n
loop 1 false
if pos = 5.5 then print "succes"

### poging 2
import random

invoer = input("geef het pad")

loop1 = True

while loop1:
    pathPos = []
    pathLetters = []
    loop2 = True
    pos = 1.1
    while loop2:
        pathPos.append(pos)
        for x in invoer:
            if x == 'l':
                pos -= 0.1
                pathLetters.append('l')
            elif x == 'r':
                pos += 0.1
                pathLetters.append('r')
            elif x == 'o':
                pos -= 1
                pathLetters.append('o')
            elif x == 'n':
                pos += 1
                pathLetters.append('n')
            elif x == '?':
                randPath = random.randint(1,4)'''

#### pseudo code [succesvol]
give string
string becomes list
check list for ?
change out ? for letter
run for x in string to calculate path
check with list if position has already been crossed if so restart
else
check if string has reached 5.5 if so print list
else restart