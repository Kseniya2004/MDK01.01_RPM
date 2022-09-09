n = int(input())
iq = int(input())
print(0)
i = 1
s = iq
while i < n:
    avr = s / i
    iq = int(input())
    if iq > avr:
        print('>')
    elif iq < avr:
        print('<')
    else:
        print(0)
    i += 1
    s += iq
