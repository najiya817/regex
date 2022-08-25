import re
txt="Rashad Bingo"
x=re.search("^Rashad",txt)
if x:
    print("found")
else:
    print("not found")

print("----------------------------------")

import re
txt="Rashad Bingo"
x=re.search("Bingo$",txt)
if x:
    print("found")
else:
    print("not found")

print("---------------------------------")

import re
txt="Rashad Bingo"
x=re.search("Rashad.*Bingo$",txt)       #check if there is anything betwn rashad and bingo
if x:
    print("found")
else:
    print("not found")

print("----------------------------------")

import re
txt="Rashad middle Bingo"
x=re.search("[midle]",txt)
if x:
    print("found")
else:
    print("not found")

print("----------------------------------")

import re
txt="Rashad Bingo"
x=re.search("[z]",txt)      #check if there is z
if x:
    print("found")
else:
    print("not found")

print("----------------------------------")

import re
txt="Rashad Bingo"
x=re.search("[a-z]",txt)        #to match letters a-z
if x:
    print("found")
else:
    print("not found")

print("---------------------------------")
import re
txt="Rashad Bingo"
x=re.search("[^bog]",txt)
if x:
    print("found")
else:
    print("not found")

print("---------------------------------")

import re
txt="Rashad Bingo"
x=re.search("Rash.?d",txt)   #check if there is only one letter btwn
if x:
    print("found")
else:
    print("not found")

print("----------------------------------")

import re
txt="Rashad Bingo"
x=re.search("Rash.+d",txt)      #.+ to check 1 or more letters..
if x:
    print("found")
else:
    print("not found")

print("-----------------------------------")

import re
txt="Rashad Bingo"
x=re.search("R....d",txt)  #number of dots =no of letters btwn
if x:
    print("found")
else:
    print("not found")

print("-----------------------------------")

import re
txt="Rashad Rango"
x=re.findall("Ra",txt)      #findall lists all with  Ra

if x:
    print("found")
else:
    print("not found")
print(x)

print("-----------------------------------")

import re
txt="Rashad Bingo dance"
x=re.split("\s",txt)
if x:
    print("found")
else:
    print("not found")
print(x)