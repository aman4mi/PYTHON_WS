import csv
import winsound

frequency = 500  # Set Frequency To 2500 Hertz
duration = 400  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

count = 0
fo = open("foo.txt", "wb")

# Close opend file

with open('sample_csv2.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        count += 1
        row = ' <@91319@> '.join(row)
        row = str(count)+" + "+row
        row += "||"
        row = row.replace("||", "\n")

        fo.write(row)
        #if count==5:
        winsound.Beep(frequency, duration)
        #print(row)


csvFile.close()
fo.close()
