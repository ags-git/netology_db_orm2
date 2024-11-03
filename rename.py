import os
import codecs

x = r'8\u0411'
y = x.encode().decode('unicode-escape')
print (y)
