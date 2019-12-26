numMove = 1
def tow(numDisk, fr, aux, to):
    if(numDisk==1):
        print("Move from %s to %s " % (str(fr), str(to)))
        numMove= numMove + 1
    else:
        tow(numDisk-1, fr, to, aux)
        tow(1, fr, aux, to)
        tow(numDisk-1, aux, fr, to)


tow(10, "Tow1", "Tow2", "Tow3")
print(numMove)