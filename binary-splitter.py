import sys

if (len(sys.argv)<2):
    print("No file provided")
    exit()

FILENAME = sys.argv[1]
MAXBYTES = 5000000
file = open(FILENAME,'rb')

count = 0

filenum = 0

print("Started")

byte = file.read(MAXBYTES)

while byte:
    count += 1
    with open((str(filenum)+".out"),'ab+') as f:
        f.write(byte)

    if (count >= MAXBYTES):
        count = 0
        filenum += 1

    byte = file.read(1)
    

print("done")