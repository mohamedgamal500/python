def simpleArraySum(ar):
    x = 0
    for num in ar:
        x = x+num
    return x


ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

result = simpleArraySum(ar)

print(result)
