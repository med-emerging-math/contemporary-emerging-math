# 3.2 Brute Force and Greedy Algorithms

In Chapters 6.4 and 6.5 we learned two algorithms for solving Taveling Salesman problems (TSPs): the Exhaustive Method (or the Brute-Force method) and the "Go Cheap" method (the nearest-neighbour method). These two methods have traits that are applicable to other problems. 

In most optimization problems, there is an exact, but innefficent method (the Brute Force method), and there is often an inexact but efficient method (the Greedy algorithm). We will look at both of these today in contexts other than TSPs.

## 1. Brute Force

Think about the following optimization problems:

1. You are separating the students in your classroom of 10 into small groups. Each student is allowed to pick (at most) 2 other students that they do not want to be in a group with. Above all you would like to keep the number of groups to a minimum, but you don't actually care how large or small each individual group is. How can you choose the groups while respecting the requests of the students? (This is essentially the [Graph Vertex coloring prblem](https://en.wikipedia.org/wiki/Graph_coloring#Vertex_coloring). )
2. You have a couple dozen board games, and you would like to pack them into suitcases to travel with them. The board games come in many different shapes and sizes. ![](http://www.analoggames.com/wp-content/uploads/2017/09/board_game_shelf_storage_suitcase_tabletop_travel_card_gamenight_analog_games_01.jpg) How do you pack them so that you use the fewest suitcaes possible? (This is called the [Knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem). )

In both of these problems you are trying to optimize some quantity (number of suitcases, number of groups). These types of problems are very common.

The **Brute Force** method to solving these optimization problems is to list out all possible configurations that satisfy the problem and then choose the one that optimizes the quantity you want. In example 1, this means trying [all 2^9 possible ways to separate 10 students into groups](https://en.wikipedia.org/wiki/Composition_(combinatorics)#Number_of_compositions), then seeing which of these partitions uses the fewest groups *and* respects the requests of the students. Example 2 is a bit messier. Using Brute Force for that would look like listing out *all* possible ways to arrange your board games into some number of suitcases. There are lots and lots of ways to arrange them, maybe millions, but one of them has to be the best.

The obvious drawback to this is that it is very time-consuming, but at least it will always find the *best* solution. The other major advantage is that it doesn't require a lot of insight into the problem. This can be relevant when starting a new problem and exploring small cases related to your problem.

## 2. Greedy Algorithms

Another general class of algorithms relates to the nearest-neighbour algorithm for TSPs: the **greedy** algorithm. This is the method where your build a solution step-by-step and at each step you add the item that will cost you the least amount. For example, in the nearest-neighbour method for TSPs we build a Hamilton path one node at a time, and we always choose to add to the path the edge that has the least weight.

In the group selection example above, a greedy algorithm would be to pick one student, then find another student that could go with that first one to form a group of two. Then try to add in a third student, and a fourth. Keep doing this until you're forced to make a second group. Then make that second group as large as possible. Keep doing this until you've placed every student in a group.

In the Board Game example, a greedy algorithm would be to pick the largest board game you can and place it in a suitcase. For the next largest board game, put it in the first suitcase if it fits, and if not, then put it in a new suitcase. For the third largest boardgame, try to put it in one of the first two suitcases, and if it doesn't fit, then start another new suitcase. Continue doing this until all board games are in a suitcase.

These two algorithms should feel very similar to each other and to the nearest-neighbour method for TSPs. A greedy algorithm, like a Brute Force algorithm is often available when trying to solve an optimization problem.

Their major advantage is that they are *not* very time consuming to perform and they usually give reasonable results. The major downside is that they do not usually give the optimal solution.

## 3. Local vs global

The big reason that the Greedy algorithm does not always produce the optimal *global* solution is that it only looks for the best *local* addition. In other words, it does the best it can at any given stage, but it does not look into the future to see if overall if it will be helpful. 

When solving a TSP, the nearest-neighbour algorithm only looks at what adding a single node will do to the cost of the path. If we wanted a more robust nearest-neighbor algorithm we could instead ask to add two consecutive edges at a time that make the cheapest (two edge) path addition. This would be require more computation at each stage, but would often give better results. In the most extreme case we could ask the algorithm to add the `n-1` many consecutive edges of least total weight... that would be the exact same as the Brute Force algorithm!

### 4. Thinking in algorithms

When approaching a new problem, it can be helpful to ask two questions:

1. If I had a supercomputer, or an army of very dependable and dedicated people, could I solve this problem even with very little insight? **If yes, then try using a Brute Force algorithm.**
2. Can a solution to my problem be built up in stages, and is there a measurement of how good a final solution is? **If yes, then try a Greedy algorithm**.

These methods won't always be the final ones you decide on, but they can be good places to start that don't require a lot of insight into your particular problem.

## Exercises

1. Like in example 1, you want to separate five students (A,B,C,D,E) into as few groups so that their requests are respected. Find, using whatever method you like, a satisfactory set of groups if their requests are: 
  1. A does not like B and C.
  2. B does not like A.
  3. C does not like D.
  4. D does not like B or C.
  5. E does not like B.
2. A classic optimization problem is the [Assignment problem](https://en.wikipedia.org/wiki/Assignment_problem). One example of this is that your family has 4 members and there are 4 chores that need to be done. Each person must do exactly one chore, and no one can do the same chore. To make it fair, each person is allowed to rate, on a scale of -10 (strong dislike) to 0 (neutral) to 10 (strong preference), how much they would like to do each of the chores. For example, Rohan might assign a 5 to taking out garbage, a 2 to walking the dog, 10 to buying groceries, and -5 to cleaning the bathroom. **Describe a Brute Force method for solving this problem, and describe a Greedy Algorithm for solving this problem.**
3. Grid-walking problems are a class of counting problems where you ask "How many paths are there through a grid, starting in the bottom left, moving only up or right?". You can [read about them here](https://brilliant.org/wiki/rectangular-grid-walk-no-restriction/). Many of these problems require mathematical insights to solve, and part of the way to develop that insight is to perform Brute force computations on small cases, then guess a pattern. By listing out all possible paths, **find the number of paths in a 2 by 3 grid** that: 
  1. Start in the bottom left square of the grid,
  2. End in the top right of the grid,
  3. Only move right or up one square at a time (no moving diagonally or down or left).
After that, find the number of paths in a 3 by 3 grid, and a 4 by 3 grid. Then guess a general pattern.
4. Watch the ["That's All I Need"](https://youtu.be/w2X3vVMdh-s) scene from "The Jerk". Explain how Steve Martin's character is performing a type of greedy algorithm.
