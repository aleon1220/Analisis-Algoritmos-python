
# Division
def div(n,m):
    quo = ""
    rem = 0
    n = str(n)
    print(" " + n + "/" + str(m))
    for i in range(0,len(n)):
        c = int(str(rem)+str(n[i]))
        rem = c%m
        nquo = (c-rem)/m
        quo += str(nquo)
        print(" "*(i-len(str(c))+2) + str(c))
        print(" "*(i-len(str(nquo*m))+1) + "-" + str(nquo*m) + " "*(len(n)-i) + "(" + str(m) + "*" + str(nquo) + ")")
        print(" "*(i-len(str(nquo*m))+1) + "-"*(len(str(nquo*m))+1))
        print(" "*(i-len(str(rem))+2) + str(rem))
return int(quo),rem