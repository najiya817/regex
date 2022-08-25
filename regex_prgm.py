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

print("----------------------------------")

import re
txt="Rashad middle Bingo"
x=re.search("Rashad.*Bingo$",txt)
if x:
    print("found")
else:
    print("not found")