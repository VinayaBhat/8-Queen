import random as r
import numpy as np
import matplotlib.pyplot as plt
#number of states in population
population_size=10
#number of iterations
NumberofGenerations=1000
#probability that mutation occurs
Mutation_probability=0.001

#number of queens present on same row: maximum=28 (all queens on same row) and minimum=0 (no queen on same row as other)
def queencountsamerow(board):
    count=0
    for i in range(board.size):
        for j in range(board.size):
            if(i!=j and board[i]==board[j]):
                count=count+1
    return count/2

#number of queens present on diagonal: maximum=28 (all queens arranged diagonally) and minimum=0 (no queen on diagonal to other)
#eg: [1,2,3,4,5,6,7,8] i=1 j=2 dx=dy=1 increment diagonal_clash, i=1 j=3 dx=dy=2 increment diagonal_clash ....
def queencountdiagonal(state):
    diagonal_clash=0
    for i in range(state.size):
        for j in range(state.size):
            if (i != j):
                dx = abs(i - j)
                dy = abs(state[i] - state[j])
                if (dx == dy):
                    diagonal_clash += 1
    return diagonal_clash/2


#generate a population with population_size states. Each state depicts the row number(1-8) of the queen assuming that there is only one queen per column.
def generateinitialpopulation():
    for i in range (1,population_size):
        population=np.random.randint(1, 9, (population_size,8))
    return population

#fitness function=number of non-attacking queens. Maximum=28(all queens attacking each other ) and minimum=0 (no queen attacking the other)
def fitness(population):
    # list containing (state,fitness_value) for the entire population
    map_fitness=[]
    #If the 8 queen problem is solved the solved list contains the goal state
    solved=[]
    for each_state in population:
        clash = 0
        row_clashes = queencountsamerow(each_state)
        diagonal_clash=queencountdiagonal(each_state)
        clash=row_clashes+diagonal_clash
        if(clash==0):
            solved.append(each_state)
        map_fitness.append((each_state,28-clash))
    return map_fitness,solved

#calculate the survival rate of each state in population
def survival(map_fitness):
    total_fitness=0
    #list containing (state,survival_rate) for the entire population
    survival_list=[]
    #calculate the total fitness function of entire population
    for each_state in map_fitness:
        total_fitness=total_fitness+each_state[1]
    #calculate survival rate of each state(survival rate=fitness_value/total_fitness) and  add it to list along with corresponding state
    for each_entry in map_fitness:
        survival_list.append((each_entry[0],(each_entry[1]/total_fitness)))
    return survival_list

#pick states randomly from population (based on roulettte wheel selection)
def random_selection(map_survival):
    random_selection_list = []
    #sortedlist=sorted(map_survival, key=lambda x: x[1])
   # max=sortedlist[population_size-1][1]
    #add until the length of list = population size
    while len(random_selection_list)!=population_size:
        #for each state generate a random number and then check if the survival rate of the state is greater or equal to that random number
            for each_state in map_survival:
                random_number = r.random()
                if random_number<=each_state[1]:
                    random_selection_list.append(each_state[0])
                    break
    return random_selection_list

#Random crossover of two parents to produce 2 offsprings
def crossover(map_random_selection):
    crossover_states=[]
    #each iteration produces 2 offsprings. To maintain population size iterate over half the population size
    for i in range((population_size//2)-1):
        #select first parent randomly
        parent1=np.array(r.choice(map_random_selection)).tolist()
        #select second parent randomly
        parent2=np.array(r.choice(map_random_selection)).tolist()
        #select point for crossover randomly
        selection=r.randint(1,7)
        #create child after crossover of parent1 and parent2 at the crossover point
        child1=parent1[0:selection]+parent2[selection:8]
        child2=parent2[0:selection]+parent1[selection:8]
        crossover_states.append(child1)
        crossover_states.append(child2)
    return crossover_states

#mutation: changes a single queen position in each state randomly with probability Mutation_probability
def mutation(population):
    mutation_list=[]
    for state in population:
        #random number = choosing a random number between 1 and 1/Mutation_probability(eg: 1/0.1=10 so random number between 1 and 10)
        random_number=r.randint(0,int(1/Mutation_probability))
        #if the random_number = 1 then change the position of a single queen randomly in the state
        if(random_number==1):
            #random column between 0 and 7
            position=r.randint(0,7)
            #randon value between 1 and 8
            value=r.randint(1,8)
            #update the queen at random position to random value (changing the row of the queen in random column)
            state[position]=value
            mutation_list.append(state)
        else:
            #no mutation
            mutation_list.append(state)
    return mutation_list

#calculate average fitness of the entire population
def calculateaveragefitness(population):
    total=0
    for eachstate in population:
        total=total+eachstate[1]
    return total/population_size

#Genetic algorithm- generate population ,random selection, crossover , random mutation for specified number of generations
def genetic_algorithm_8queen():
    #generate inital population randomly
    population=generateinitialpopulation()
    #list to maintain average fitness for each generation
    fitnesslist=[]
    solved=False
    iteration=0
    #while the goal state is not reached or until the maximum number of generations specified
    while solved!=True and iteration<NumberofGenerations:
        #return fitness of each state and goal state if problem is solved
        fitness_map,solved=fitness(population)
        if (iteration == 0):
            print("Initial Population ", fitness_map)
        #if problem not solved
        if len(solved)==0:
            ##calculate average fitness of the generation
            averagefitness=calculateaveragefitness(fitness_map)
            #print("Population with fitness ",fitness_map)
            #print("Avergae fitness of the population ",averagefitness)
            fitnesslist.append(averagefitness)
            ##return survival rate of each state
            survival_map=survival(fitness_map)
            #print("Population with survival rate ",survival_map)
            ##return randomly selected states of population
            random_selection_list=random_selection(survival_map)
            ##return population after crossover at random selected point
            crossover_list=crossover(random_selection_list)
            #print("Population after random crossover ",crossover_list)
            ##return the population after mutation
            mutated_list=mutation(crossover_list)
            #print("Population after mutation ",mutated_list)
            ##assign population after mutation as population for next generation
            population=np.asarray(mutated_list)
        else:
            ##if problem is solved
            print("Solved ",solved[0])
            print("Generation ",iteration)
            solved=True
        iteration=iteration+1
    final, solved = fitness(population)
    print("Final populations ", final)
    ## plot average fitness vs number of generations
    plt.plot(fitnesslist)
    plt.ylabel("Average Fitness")
    plt.xlabel("Number of Generations")
    image= "1.png"
    plt.savefig(image)
    plt.show()


def main():
    genetic_algorithm_8queen()


if __name__==main():
    main()

