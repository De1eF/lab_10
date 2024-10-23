frq = dict()

with open("start.txt", "r", encoding = 'utf-8') as start:
    for c in start.read():
        lowerC = c.lower()
        if (ord(lowerC) in range(ord("а"), ord("я"))):
            frq[lowerC] = frq.get(lowerC, 0) + 1
    frq = dict(sorted(frq.items()))

with open("fin.txt", "w", encoding = 'utf-8') as fin:
    finText = "Кількість літер у тексті: \n__________ \n"
    for k in frq.keys():
        finText += "{0} : {1} \n".format(k, frq[k])
    fin.write(finText)
