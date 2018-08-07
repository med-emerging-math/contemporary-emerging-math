# 3.4 Cool Examples

* Speedrun routing
* Swarm Intelligence and Ant Colony Optimization (ACO)
* Google Maps

## 1. Speedrun routing

In the last five years, [speedrunning](https://en.wikipedia.org/wiki/Speedrun) video games (i.e. completing them as fast as possible) has taken off as a hobby. Two major categories of speedrunning are **any%**, where a game is beaten as quickly as possible ignoring additional quests and objectives, and **100%** where a game is beaten while also completing all additional quests and objectives. In 100% speedruns the traveling salesman problem (TSP) can become relevant as there are many objectives to achieve, but typically the order in which you achieve them is mostly up to you. As such we get a TSP.
  
> A path through the map of [Zelda: Breath of the Wild](https://www.reddit.com/r/zelda/comments/7snlhu/botw_optimal_solution_to_the_traveling_korok_seed/) that collects all 900 Korok seeds. This is a TSP with 900 nodes.

Solving these TSPs, even approximately, is relevant to the players who speedrun these games. Once someone has spent the time to find a near optimal solution to the TSP for a game, all the players can use the tour they found to help shorten their speedruns. People who test and time new routes play an important, but unglamorous part in the speedrunning community. 

There are some major challenges when modeling a video game speedrun as a TSP. One of the largest problems is that it is time consuming to find the shortest distance between two locations in a video game. In all of the examples we've looked at, the complete weighted graph and all its distances have been given to us in advance; actually finding the weights of all these edges in a video game world is time consuming. The shortest times between two locations can also depend on factors like the skill of the player, the difficulty of the movement, and sometimes random chance. As an extreme example of this, watch [this video about speedrunning stage 4-2 in the original Mario Brothers](https://www.youtube.com/watch?v=i1AHCaokqhg).

There are additional challenges in this modelling which you can explore in the exercises.

## 2. Swarm Intelligence and Ant Colony Optimization (ACO)



## Exercises

1. TSPs are more relevant to **100%** speedruns, but can also be relevant to **any%** speedruns. Watch [this video](https://www.youtube.com/watch?v=dNL8rdn00IU) about the world record progression of the Super Metroid any% speedrun.
  1. Describe how this speedrun can be modelled as a TSP. What are the nodes in this weighted graph? (This happens in the first 5 minutes of the video.)
  2. What was the original tour (by Smokey), and how did it get improved (by Behemoth)? Find a map of Super Metroid game world online and identify the positions of the nodes of the TSP.
  3. Is Behemoth's newer route always faster than Smokey's old route? What needs to happen in a speedrun for Behemoth's route to be faster than Smokey's route? (This happens around the 16 minute mark of the video.)
2. Read this [Reddit post about the challenges of using TSPs in video games](https://old.reddit.com/r/speedrun/comments/4bqsqs/have_there_been_attemps_to_model_a_run_with_the/), and find another challenge about modeling TSPs in video games (besides measuring minimal distances).
