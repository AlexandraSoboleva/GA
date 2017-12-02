import readInput
import MyGen
import LibGen

readInput.readInput()
for i in range (0,10):
    bestLibindividual=LibGen.runGen()
    bestMyindividual=MyGen.runGen(100)
    print(i,':')
    print(bestLibindividual[0],bestLibindividual[1])
    print(bestMyindividual[1][0],bestMyindividual[0])
    print('-----------------------------------------------')

