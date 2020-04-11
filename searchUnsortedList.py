# Complete the findNumber function below.
def findNumber(arr, k):
    n = len(arr)
    if (arr[n-1] == k) :
        return "YES"
    backup = arr[n-1]
    arr[n-1] = k

    i = 0
    while(i < n) :
        if (arr[i] == k) :
            arr[n-1] = backup
            if (i < n-1):
                return "YES"
            return "NO"
        i = i + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input().strip())

    arr = []

    for _ in xrange(arr_count):
        arr_item = int(raw_input().strip())
        arr.append(arr_item)

    k = int(raw_input().strip())

    res = findNumber(arr, k)

    fptr.write(res + '\n')

    fptr.close()
