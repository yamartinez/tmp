OUTPUT_FILENAME = 'program.exe'
INPUT_FILE_COUNT = 1

outfile = open(OUTPUT_FILENAME,'ab+')

print("Starting.")

for i in range(INPUT_FILE_COUNT):
    with open(str(i)+'.out','rb') as file:
        b = file.read(1)
        while b:
            outfile.write(b)
            b = file.read(1)

print("Done.")