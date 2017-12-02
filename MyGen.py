import readInput
import random

population=[]
newpopulation=[]
pcount=200
things=[]


def getPopulation():
    thingss=sorted(readInput.things,key=lambda x: x[2])
    global things
    things=thingss[::-1]
    for i in range (0,pcount):
        random.seed()
        ind=random.randint( 0, len(things))
        curr_weight=0
        curr_volume=0
        population.append([])
        population[i].append([])
        for j in range(0,ind):
            population[i][0].append(0)
        for j in range(ind,len(things)):
            if curr_weight+things[j][0]<readInput.weight and curr_volume+things[j][1]<readInput.volume:
                population[i][0].append(1)
                curr_weight+=things[j][0]
                curr_volume+=things[j][1]
            else:
                population[i][0].append(0)
        for k in range(0,len(population[i][0])):
            if population[i][0][k]==0:
                if curr_weight + things[k][0] < readInput.weight and curr_volume + things[k][1] < readInput.volume:
                    population[i][0][k]=1
                    curr_weight += things[k][0]
                    curr_volume += things[k][1]
            else:
                break

def fitnessInit():
    for i in range(0,len(population)):
        value = 0
        volume=0
        weight=0
        for j in range(0,len(population[i][0])):
            if population[i][0][j]==1:
                value+=things[j][2]
                weight+=things[j][0]
                volume+=things[j][1]
                if weight>readInput.weight or volume>readInput.volume:
                    value=0
                    break
        population[i].append([value])

def selection():
    sum=0
    parents=population.copy()
    for k in range(0,len(population)):
        sum+=population[k][1][0]
    while len(parents)>0:
#choose first
        i = 0
        random.seed()
        r = random.randint(0, round(sum))
        currsum=0
        while currsum<r and i<len(parents):
            currsum+=parents[i][1][0]
            i+=1
        sum-=parents[i-1][1][0]
        mother=parents[i-1][0]
        parents.remove(parents[i-1])
#choose second
        i=0
        random.seed()
        r = random.randint(0, round(sum))
        currsum=0
        while currsum<r and i<len(parents):
            currsum+=parents[i][1][0]
            i+=1
        sum -= parents[i - 1][1][0]
        father = parents[i - 1][0]
        parents.remove(parents[i - 1])
        crossingover(mother, father)

def getFitness(child):
    value=0
    volume = 0
    weight = 0
    for j in range(0, len(child)):
        if child[j] == 1:
            value += things[j][2]
            weight += things[j][0]
            volume += things[j][1]
            if weight > readInput.weight or volume > readInput.volume:
                value = 0
                break
    return value

def crossingover(mather, father):
    child=[]
    for i in range(0,len(mather)):
        random.seed()
        ind = random.random()
        if (ind<0.5):
            child.append(mather[i])
        else:
            child.append(father[i])
    ch=[]
    ch.append(child)
    ch.append([getFitness(child)])
    newpopulation.append(ch)

def mutation():
    was=[]
    for i in range(0,20):
        while True:
            random.seed()
            ind = random.randint(0, len(population)-1)
            try:
                was.index(ind)
            except ValueError:
                was.append(ind)
                break
        while True:
            random.seed()
            indd = random.randint(0, len(population[ind][0])-1)
            if population[ind][0][indd]==0:
                population[ind][0][indd]=1
                population[ind][1][0]+=things[indd][2]
                break

def kill():
    for item in population:
        if item[1]==0:
            population.remove(item)

def formNewPopulation():
    global population
    for i in range(0,len(population)):
        population[i][1][0]=population[i][1][0]*0.8
    spop=sorted(population+newpopulation,key=lambda x: x[1])
    spop=spop[::-1]
    population=spop[0:200]

def runGen(loopcount):
    global population
    population = []
    global newpopulation
    newpopulation = []
    global things
    things = []
    getPopulation()
    fitnessInit()
    for k in range(0,loopcount):
        selection() #calls crossingover
        mutation()
        kill()
        formNewPopulation()
    return population[0]
