# n = int(input())
# for i in range(n):
#     print('%s%s' % (' ' * (n - i - 1), '*' * (i * 2 + 1)))
n = int(input())
space = n - 1
star = 1
for i in range(1, n + 1):
    print(' ' * space + '*' * star)
    space -= 1
    star += 2
