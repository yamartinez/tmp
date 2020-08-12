import sys

if (len(sys.argv)<3):
    print("No file provided")
    exit()

OUTPUT_FILENAME = sys.argv[1]
INPUT_FILE_COUNT = sys.argv[2]

outfile = open(OUTPUT_FILENAME,'ab+')

print("Starting.")

for i in range(INPUT_FILE_COUNT):
    with open(str(i)+'.out','rb') as file:
        b = file.read(1)
        while b:
            outfile.write(b)
            b = file.read(1)

print("Done.")