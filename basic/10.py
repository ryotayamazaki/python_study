from operator import itemgetter
#from tqdm import tqdm

f_r = open("col2.txt","r")
word = [""]
count = 0
check = []

for row in f_r:
    for col in row:
        if col == "\n":
            word.append("")
            count += 1
        else:
            word[count] += col

check.append([word[1],1])

print check,len(check)

#pbar = tqdm(total=len(word))
sintyoku = 0.
for i in range(1,len(word)):
    if sintyoku +0.5<= float(i) / len(word) *100:
        sintyoku += 1
        print sintyoku,"%"
#    print i
    hit = True
    for j in range(len(check)):
#        print i,j
        if word[i] == check[j][0]:
            check[j][1] += 1
            hit = False
            break
    if hit:
        check.append([word[i],1])
#    pbar.update(1)
#pbar.close()

check.sort(key = itemgetter(1),reverse = True)

for i in range(len(check)):
    print check[i][0]

f_r.close

