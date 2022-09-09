n = 0
sum = 0
while True:
    n = float(input())
    if n > 500:
        n = n - (n * 0.07)
    else:
        if n < 0:
            break
    sum += n
print(sum)
