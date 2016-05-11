f_r = open("address.txt","r")

count = []
word = []
mode = 1
hit = 1
i = 0


for row in f_r:
    word.append(["",""])
    for col in row:
        hit = 1
        if col == "\t":
#            word[mode] += "\n"
            mode = 0
            hit = 0
        if col == "\n":
#            word[mode] += "\n"
            mode = 1
            hit = 0
        if hit:
            word[i][mode] += col
#    print i,word[i][0],word[i][1]
    i += 1
print "Reading is fin"
#print word[0][1]
count.append([word[0][1],1])
#print count[0]
#progress = 0.
for i in range(1,len(word)):
    flag = False
    for j in range(len(count)):
#        print i,j,len(count),len(word)
        if count[j][0] == word[i][1]:
            flag = True
            break
    if flag:
        count[j][1] += 1
    else:
        count.append([word[i][1],1])
#    if progress + 0.5<= float(i/len(word) * 100):
#        progress += 1
#        print progress

#word.sort(key = itemgetter(0,1) ,reverse = True)
for i in range(len(count)):
    print count[i][0],"/",count[i][1]

f_r.close
