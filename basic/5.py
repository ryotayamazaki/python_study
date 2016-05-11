import sys

f = open("address.txt","r")

count = 0
word = []

get_data = sys.argv

#print get_data

for row in f:
    word.append(row)
    count += 1
#    print word
#    print row
#    for col in row:
#        print col

for i in range(int(get_data[1])):
    print word[i]

f.close

