import sys

f = open("address.txt","r")

count = 0
word = []

get_data = sys.argv

#print get_data

for row in f:
    word.append(row)
    count += 1

#print len(word) , int(get_data[1]),len(word)-int(get_data[1])

#print word[len(word) -1]

for i in range(len(word)-int(get_data[1]),len(word)):
    print word[i]

f.close


