weight=0
volume=0
things=[]

def readInput():
    f = open('33.txt', 'r')
    lines= [line.strip() for line in f]
    f.close()
    global weight
    weight=int(lines[0].split(' ')[0])
    global volume
    volume=int(lines[0].split(' ')[1])
    lines.remove(lines[0])
    for item in lines:
        global things
        items=item.split(' ')
        things.append((int(items[0]),float(items[1]),int(items[2])))