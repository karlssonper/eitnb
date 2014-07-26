eitnb
=====

eighty is the new black - source code formatting script

only look at stats
```
eitnb code.cpp
```

only look at lines > width and ending with whitespace
```
eitnb code.cpp -v --nostats
```

remove all ending whitespaces and consecutive blank lines (will modify file)
```
eitnb code.cpp --nostats -kws -kbl
```

