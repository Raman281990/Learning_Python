##Reading lines from a txt file and removing new line character
fileHandle = open("Arrays.txt")
for lines in fileHandle:
    lines = lines.rstrip()
    if lines.startswith("find"):
        print(lines)

## Reading a file and calculating average of extracted data
fname = input("Enter  file name")
fileX = open(fname)

totalLines = 0
countValues = 0.0
avg = 0.0
for lines in fileX:
    if not lines.startswith("X-DSPAM-Confidence: "):
        continue
    else:
        totalLines += 1
        line = lines.split(":")
        countValues += float(line[1])
avg = countValues / totalLines
print("Average spam confidence:" + str(avg))


fh = open("Arrays.txt",'r')
fh.close()


