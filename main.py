import os
import cv2
import nb
import blur
import dilate
import fnmatch
import sys

input = 'input'


args = sys.argv

firstArg = args[1]
thirdArg = args[3]

if args[1] == "--i":
    input = args[2]

if args[3] == "--o":
    output = args[4]

path = os.getcwd()
print ("The current working directory is %s" % path)



listOfFiles = os.listdir(input)
pattern = "*.jpg"
pattern2 = "*.png"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
            print (entry)
    elif fnmatch.fnmatch(entry,pattern2):
            print (entry)

path = "Data/output/"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)


for img in listOfFiles:
    print(img)
    out = path + img
    print(out)
    nb.transnb(f'{input}/{img}', out)
    blur.transblur(f'Data/output/{img}', 5, out)
    dilate.transdilate(f'Data/output/{img}', out)

