f_r = open("address.txt","r")
f_w1 = open("col1.txt","w")
f_w2 = open("col2.txt","w")


#print f

count = 0
word1 = ""
word2 = ""
mode = 1
hit = 1

for row in f_r:
    for col in row:
        hit = 1
        if col == "\t":
            word1 += "\n"
            mode = 2
            hit = 0
        if col == "\n":
            word2 += "\n"
            mode = 1
            hit = 0
        if hit:
            if mode == 1:
                word1 += col
            if mode == 2:
                word2 += col
#    print row
#    word.append(row.read())
#    count += 1
#    print word
#    print row
#    for col in row:
#        print col

#print word1
#print word2
f_w1.write(word1)
f_w2.write(word2)
f_r.close
f_w1.close
f_w2.close
