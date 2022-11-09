from listfiles import *

files = getFiles()
f = open("Readme.md", "w")

count = 0
for file in files:
    print(file)
    countLinesForFile = len(open('./features/' + file).readlines())
    count += countLinesForFile
    f.write(str(file) + "(" + str(countLinesForFile) + ")\n")

f.write("Total" + "(" + str(count) + ")\n")

print(count)

