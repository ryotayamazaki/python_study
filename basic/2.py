f_r = open("address.txt","r")
#f_w1 = open("col1.txt","w")
#f_w2 = open("col2.txt","w")


#print f

count = 0
word1 = ""
word2 = ""
word = ""
mode = 1

for row in f_r:
    for col in row:
#        if mode == 1:
#            word += col
#        if mode == 2:
#            word += col
        if col == "\t":
            word += " "
#            mode = 2
        elif col == "\n":
            word += "\n"
#            mode = 1
        else:
            word += col
#    print row
#    word.append(row.read())
#    count += 1
#    print word
#    print row
#    for col in row:
#        print col

print word

f_r.close
