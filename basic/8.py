
#def sort(p):
#    for i in range(len(p)):
#        for j in range(i,len(p)):
#            print i,j,p[i][0],p[j][0]
#            if p[i][0] > p[j][0]:
#                print "change"
#                work = p[j]
#                p[j] = p[i]
#                p[i] = p[j]
#    return p
from operator import itemgetter
f_r = open("address.txt","r")

count = 0
word = []
mode = 0
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

word.sort()
for i in range(len(word)):
    print word[i][1],word[i][0]
#    print row
#print word
f_r.close
