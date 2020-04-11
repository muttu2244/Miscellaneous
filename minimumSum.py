import math,random
def minSum(num, k):
    # Write your code here

    #count =0
    for i in range(k):
        #print(i)
        #print (num[i])
        if i<=(len(num)-1):
            num[i] = math.ceil(num[i] / 2)
        else:
            #v = random.choice(num)

            #num[num.index(v)] = math.ceil(v / 2)
            num[1] = math.ceil(num[1] / 2)
        #count = count + 1
        #if count
        print (num)


    sum = 0
    for i in range(len(num)):
        sum = sum + num[i]

    print (int(sum))
minSum([10,20,7],4)

