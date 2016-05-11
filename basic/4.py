f_r1 = open("col1.txt","r")
f_r2 = open("col2.txt","r")


count = 0
word1 = [""]
word2 = [""]
word =""
mode = 1
hit = 1
count = 0
word = ""

for row in f_r1:
    for col in row:
        if col == "\n":
            word1.append("")
            count += 1
        else:
            word1[count] += col

count = 0
for row in f_r2:
    for col in row:
        if col == "\n":
            word2.append("")
            count += 1
        else :
            word2[count] += col
for i in range(len(word1)):
    word += word1[i]
    word += "\t"
    word += word2[i]
    word += "\n"

#print word1
#print word2
print word

f_r1.close
f_r2.close
