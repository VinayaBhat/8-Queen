# 8-Queen
Solving 8 queen problem with Genetic algorithm
Fitness function= number of non attacking queen pairs. Maximum=28: no queen attacking each other. Minimum=0: every queen attacking every other queen.

I experimented with different values of population size and mutation probability keeping the number of generations fixed to 1000. Each state is represented by the row position of the queen assuming one queen per column.  For example: [5, 5, 2, 5, 3, 6, 7, 7] represents the state in which the first queen is in column one row five, second queen in column two row 5 and so on. 

Experiment 1:
Fixed parameters: 
Mutation probability = 0.01
Number of generations = 1000
Variable parameters:
Population size

Bigger the population size faster the algorithm gives the solution (converges). With population size 10 we can see that the algorithm takes smaller steps therefore after 1000 iterations also we get the best state to have a fitness score of 24. With population size 100, the algorithm gets to see more states hence takes better steps than previous case so the maximum fitness score after 100 iterations is 27. With the population size 500 the algorithm at each iteration gets more states to deal with thus the algorithm converges to a solution in the 34th iteration. With population size 1000, at each iteration the algorithm gets to see more states thus the algorithm converges faster. We get the solution in only 10 iterations.
Therefore, we can conclude that bigger the population size faster the algorithm converges to a solution.

Experiment 2:
Fixed parameters: 
Population size=1000
Number of generations = 1000
Variable parameters:
Mutation probability

With increase in mutation probability the algorithm converges faster. Mutation probability 0.0001 means choosing a random number between 0 and 10000 and chance that this random number is 1. Similarly, Mutation probability 0.1 means choosing a random number between 0 and 10 and chance that this random number is 1. So, there is a higher probability of getting 1 when the random number is chosen between 0 to 10 than when chosen between 0 to 10000. So, the number of mutations will increase with increase in mutation probability. With increase in mutation probability the algorithm gets to see more states hence faster it converges
(*) The graph of average fitness vs generation takes average fitness of each generation therefore even though the solution is obtained the average fitness is not 28 since it takes the average off all states in the population. 
(*) Different runs may give different results since the initial population is generated randomly. 
(*) States in population have less diversity as the number of generations increase or when the algorithm nearly converges to a solution and this situation is quite common with smaller population size. 


