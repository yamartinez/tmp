import sys

if (len(sys.argv)<3):
    print("No file provided")
    exit()

OUTPUT_FILENAME = sys.argv[1]
INPUT_FILE_COUNT = int(sys.argv[2])

outfile = open(OUTPUT_FILENAME,'ab+')

print("Starting.")

for i in range(INPUT_FILE_COUNT):
    with open(str(i)+'.out','rb') as file:
        b = file.read()
        outfile.write(b)

print("Done.")