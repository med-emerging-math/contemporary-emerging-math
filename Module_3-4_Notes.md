# 3.4 Cool Examples

* Speedrun routing
* Swarm Intelligence and Ant Colony Optimization (ACO)

## 1. Speedrun routing

In the last five years, [speedrunning](https://en.wikipedia.org/wiki/Speedrun) video games (i.e. completing them as fast as possible) has taken off as a hobby. Two major categories of speedrunning are **any%**, where a game is beaten as quickly as possible ignoring additional quests and objectives, and **100%** where a game is beaten while also completing all additional quests and objectives. In 100% speedruns the traveling salesman problem (TSP) can become relevant as there are many objectives to achieve, but typically the order in which you achieve them is mostly up to you. As such we get a TSP.
  
> A path through the map of [Zelda: Breath of the Wild](https://www.reddit.com/r/zelda/comments/7snlhu/botw_optimal_solution_to_the_traveling_korok_seed/) that collects all 900 Korok seeds. This is a TSP with 900 nodes.

Solving these TSPs, even approximately, is relevant to the players who speedrun these games. Once someone has spent the time to find a near optimal solution to the TSP for a game, all the players can use the tour they found to help shorten their speedruns. People who test and time new routes play an important, but unglamorous part in the speedrunning community. 

There are some major challenges when modeling a video game speedrun as a TSP. One of the largest problems is that it is time consuming to find the shortest distance between two locations in a video game. In all of the examples we've looked at, the complete weighted graph and all its distances have been given to us in advance; actually finding the weights of all these edges in a video game world is time consuming. The shortest times between two locations can also depend on factors like the skill of the player, the difficulty of the movement, and sometimes random chance. As an extreme example of this, watch [this video about speedrunning stage 4-2 in the original Mario Brothers](https://www.youtube.com/watch?v=i1AHCaokqhg).

There are additional challenges in this modelling which you can explore in the exercises.

## 2. Swarm Intelligence and Ant Colony Optimization (ACO)

Ant colonies turn out to be very good at producing approximate solutions for TSPs. 

**Swarm Intelligence** is the powerful idea that giving simple instructions to individual agents in large group can produce complicated and sophisticated results. 

For example, in a group of 30 students ask each student to secretly choose two other students and then try to move to be between them. *What do you think will happen?* In practice, all 30 students clump together in one big mess. 

![](3_3_children)

As a second example, this time as each student to secretly choose another student to be their "dragon" and a student to be their "knight", and they must always keep their knight in between them and their dragon. *What do you think will happen?* In this version typically the students spread out and form small clusters. (If you decide to try this game with real students you should make a rule like no one is allowed to leave the field, otherwise students might be tempted to spread out very far!)

In both of the previous examples, the students were the individual agents and were given **local instructions** to follow, that is you told each student how they should move. Even though all the rules were about individuals, the group started to move and take shape in interesting ways. This is called [emergent behaviour](https://en.wikipedia.org/wiki/Emergence). Remarkably, even from simple local instructions, complex behaviour can emerge.

**Ant colony optimization (ACO)** is a specific type of swarm intelligence. The idea is that when an individual ant travels it leaves a pheremone trail for other ants to follow. The first ant's path will be random, and its pheremone trail will be faint. Later ants will tend to follow pheremone trails (although they may also deviate). The more ants that follow a trail, the stronger the pheremone trail becomes, encouraging more ants to follow it. The pheremones will fade over time, so short paths that have many ants traveling on them will stay strong, while long, inefficient paths will fade from disuse.

> ![](https://99percentinvisible.org/app/uploads/2015/12/desire-path-usability.png)    
> Top-down design can often be inflexible, and individual agents might find better paths. [Read more about this here](https://99percentinvisible.org/article/least-resistance-desire-paths-can-lead-better-design/).  Picture by Natalia Klishina.

This type of optimization was modeled mathematically in 1991, and has since been adapted for use in package delivery, internet traffic, and protein folding problems. It can be used for many optimization problems in graph theory, such as TSPs.

To solve a TSP using ACO, we (1) let an ant choose a tour and lay pheremones on it. (2) As many ants travese the graph, (3) shorter edges and strings of edges will be reinforced. As pheremones fade, efficient tours will emerge (4). 

> ![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Aco_TSP.svg/1000px-Aco_TSP.svg.png) [Source](https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms#/media/File:Aco_TSP.svg)

****

## Exercises

1. TSPs are more relevant to **100%** speedruns, but can also be relevant to **any%** speedruns. Watch [this video](https://www.youtube.com/watch?v=dNL8rdn00IU) about the world record progression of the Super Metroid any% speedrun.
    1. Describe how this speedrun can be modelled as a TSP. What are the nodes in this weighted graph? (This happens in the first 5 minutes of the video.)
    2. What was the original tour (by Smokey), and how did it get improved (by Behemoth)? Find a map of Super Metroid game world online and identify the positions of the nodes of the TSP.
    3. Is Behemoth's newer route always faster than Smokey's old route? What needs to happen in a speedrun for Behemoth's route to be faster than Smokey's route? (This happens around the 16 minute mark of the video.)
2. Read this [Reddit post about the challenges of using TSPs in video games](https://old.reddit.com/r/speedrun/comments/4bqsqs/have_there_been_attemps_to_model_a_run_with_the/), and find another challenge about modeling TSPs in video games (besides measuring minimal distances).
3. One of the most famous examples of emergent behaviour is [Conway's game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), which describes how the squares in a grid turn from black to white based on the colours of their neighbours. This has a very, very rich emergent behaviour that has fascinated people since its original invention. [Play around with it for a bit](https://pmav.eu/stuff/javascript-game-of-life-v3.1.1/) and describe some of the behaviour that emerges.
4. Play around with [this ACO demo](http://gordyd.github.io/js-aco/) that solves TSPs. How does ACO compare to genetic algorithms as discussed in the Module 3.3 notes?
