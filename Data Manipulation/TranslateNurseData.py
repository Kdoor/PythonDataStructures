count = 0
fOut = open("nurse1.yaml", "w")
fOut.write('---' + "\n")
with open('nurse1.txt', encoding="utf8") as f:
    for line in f:
        #print(line)
        #print(count)
        #print(line)
        line = line.replace('"', r'\"')
        if count % 7 == 0:
          partitioned_string = line.partition('. ')
          print(partitioned_string)
          #This is the question number
          fOut.write(partitioned_string[0] + ':' + "\n" + "\n")
          #This is the question
          fOut.write('  ' + 'Question: ' + '"' + partitioned_string[2] + '"' + "\n" + "\n")

        if count % 7 == 2:
          #This is the question number
          #This is the question
          #strip the new lines with that split and join... TODO: so ugly please replace
          fOut.write('  ' + 'Answer1: ' + '"' + " ".join(line.split()) + '"' + "\n")
        if count % 7 == 3:
          #This is the question number
          #This is the question
          #strip the new lines with that split and join... TODO: so ugly please replace
          fOut.write('  ' + 'Answer2: ' + '"' + " ".join(line.split()) + '"' + "\n")
        if count % 7 == 4:
          #This is the question number
          #This is the question
          #strip the new lines with that split and join... TODO: so ugly please replace
          fOut.write('  ' + 'Answer3: ' + '"' + " ".join(line.split()) + '"' + "\n")
        if count % 7 == 5:
          #This is the question number
          #This is the question
          #strip the new lines with that split and join... TODO: so ugly please replace
          fOut.write('  ' + 'Answer4: ' + '"' + " ".join(line.split()) + '"' + "\n" + "\n")
        count = count + 1


