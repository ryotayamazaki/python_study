f = open("address.txt","r")

#print f

count = 0
word = []

for row in f:
#    word.append(row.read())
    count += 1
#    print word
#    print row
#    for col in row:
#        print col

print count

f.close
