# 3.3 Adding in Randomness

We've seen many different algorithms for solving Travelling Salesman Problems (TSPs). In all cases the algorithms we looked at are **deterministic**, meaning that each time we run a particular algorithm we should get the same answer (assuming we did the calculations correctly!). We are pretty comfortable with using deterministic algorithms, so we tend to favour them over the alternative: **non-deterministic** algorithms. These are algorithms with an element of randomness whose outcome may change every time.

## Purely random algorithms

At first it might seem that algorithms with random components cannot possibly be helpful. Our intuition tells us that, for example, choosing a random route to bike to work likely won't work. Similarly, choosing a random collection of groceries at the store would leave you unable to make any normal meals. Attempting to solve a problem by randomly choosing a possible solution from among all possible solutions is called a **purely random algorithm**.

However, there are many circumstances where purely random algorithms are good *enough*, possibly with a small amount of conditioning. For example, choosing a random outfit to wear in the morning will often work just fine, and might save you time. Sure, it might not be the *perfect* outfit for the day, but it will likely be okay. Maybe choosing your outfit *completely* randomly might not work, but it could be improved by first choosing a random top, and then choosing a random bottom *from among bottoms that go well with that top*. That algorithm seems like it would be pretty effective.

> <a href="url"><img src="https://recycledrose.files.wordpress.com/2010/08/dsc_0008.jpg" align="center" width="250" ></a>    
> A somewhat random choice of clothes isn't the worst! [Source](https://recycledrose.wordpress.com/2010/08/12/day-40-mismatch-style/)

The lesson here is that, if most of the options are close enough to the optimal choice (i.e. have low **relative error**), a random choice will likely be close enough to the optimal choice.

In TSPs, a purely random algorithm is unlikely to succeed however, because in most cases, most of the paths have high relative error. It's unlikely that a randomly selected path will have low relative error.

As an extreme (and hilarious) example, [here is a visualization of "BOGOsort" (Epilepsy warning)](https://www.youtube.com/watch?v=DaPJkYo2quc) which attempts to sort a list of items from smallest to largest by taking a random permutation of the items and checking to see if it is in the correct order. As expected, it's highly unlikely that this will work even after many, many attempts.

## Mutations

Injecting a small amount of randomness into a deterministic algorithm can improve its results, sometimes remarkably.

As a first, down to Earth example, think about what sorts of restaurants you like going to (or treats you enjoy buying). If you're at all like me, then you have a shortlist of restaurants that you cycle through when you're considering going out to eat. Essentially my algorithm is "Which of these shortlisted restaurants do I feel like at the moment?". It's easy to get stuck into habits, and miss out on other potentially more interesting and enjoyable restaurants in other places. This is a good example where adding a bit of randomness into your decision making might increase your overall experience. One option would be to force yourself to choose a random restaurant every fifth time you go out to eat. Maybe it will be terrible, but maybe it will be amazing and you can add it into your shortlist. Then every other time you go out to eat you'll have more, better options.

We can apply this type of randomness to many problems: ["How do I think more creatively?"](https://bigthink.com/in-their-own-words/the-necessity-of-creative-risk-taking), "How can I get to work more efficiently?", or, "How can I teach more effectively?". In each of the cases we have some deterministic, planned out way of solving a problem, and we add small amounts of randomness to shake things up. We can call these shakeups **mutations**, or more coloquially we might think of this as **taking more risks**.

Let's now apply mutations to two of our TSP algorithms: Nearest Neighbour (NN) and Cheapest Link (CL). Both of these algorithms are greedy algorithms; we always take the cheapest option available to us at each stage. Now, instead of always taking the cheapest option, lets take the cheapest option 80 % of the time, and the other 20 % of the time lets take the second-cheapest option available. (The exact numerical choices of 80-20 aren't that important, other than I wanted to choose the cheapest option most of the time.) If we run this algorithm numerous times it will give us many tours to choose from, and hopefully at least one of them is close to optimal.

## Genetic Algorithms

Finally, we mention **genetic algorithms**, which are related to **machine learning** and **artificial intelligence**. This section is meant to be an overview - a peek inside. A detailed explanation of these things would go beyond the course, so don't worry if you don't follow every single word. Genetic algorithms (like brute force algorithms or greedy algorithms) are a whole class of algorithms, or in other words, a style of algorithm. There isn't a single "genetic algorithm".

As its core, a genetic algorithm is about building up an algorithm for completing a task, from nothing, by repetitive training and evolution. It mimics biological and culutural evolution by setting up a measure of success, and then running repeated training sessions. After each training session, the worst performers are discarded, and the strongest performers are mixed together. Let's look at an example:

> [![A computer learns to play a snake game.](https://img.youtube.com/3bhP7zulFfY/0.jpg)](https://www.youtube.com/watch?v=3bhP7zulFfY) 

In the example above, in each "generation" the computer trains 5 different snake algorithms; these are called the 5 **species** of snake. At first, all five species move randomly. After each species has attempted to play the game, we delete the one species that did the worst and copy the one the did better. We reinforce the surviving species, and (in a technical way) tell them to "keep doing more of what you're doing; you're all good snakes". We also randomly mutate small aspects of some species in hopes that they will discover something new. This goes on for many, many generations (in the video it was 25, but some genetic algorithms take thousands of generations). At the end of all of this we will have 5 species that are all surprisingly good at playing the game.

There are lots of moving parts and options in a genetic algorithm:

1. How many species do we start with?
2. How do we measure an effective species?
3. How many species do we eliminate each generation?
4. How much random mutation do we want?
5. How many generations should we run?

All of these questions depend on the particular problem you are trying to solve. For many problems, we don't have exact answers to these questions, we've merely found answers that seem to work. If you're interested in these question, [this short video](https://www.youtube.com/watch?v=nrKjSeoc7fc) goes through a genetic algorithm and shows off how changing these variables affects the outcome of the genetic algorithm.

Remarkably, these algorithms are often extremely effective and are the methods used at Google, for facial recognition, and for teaching computers to play chess.

Genetic algorithms have also been used to solve TSPs. I won't go into the details here, but you can [watch a visualization here](https://www.youtube.com/watch?v=bUEOuI2fK-M). You can read about the details [here](http://www.theprojectspot.com/tutorial-post/applying-a-genetic-algorithm-to-the-travelling-salesman-problem/5) or [here](https://medium.com/@becmjo/genetic-algorithms-and-the-travelling-salesman-problem-d10d1daf96a1). In all cases we start with many random tours and make random mutations to them, generation after generation.

If you're interested in learning more about genetic algorithms and artificial intelligence, [I wrote an introductory article about it](https://mikepawliuk.ca/2018/03/31/how-does-modern-ai-work-math-for-my-mom/) with lots of nice pictures.  

### Exercises

1. Consider the purely random method for choosing 100 dollars worth of groceries at a grocery store. Here you list all [40 000 items](https://www.marketwatch.com/story/grocery-stores-carry-40000-more-items-than-they-did-in-the-1990s-2017-06-07) in a grocery store, and choose an item one at a time until you've passed your 100 dollar limit. How effective is this method? Would you be able to survive on the groceries you chose?
2. (For the hockey fans.) Randomness is used in the NHL each year to decide the order that teams get to select players in the Rookie draft. [See here for a detailed explanation](https://www.sportsnet.ca/hockey/nhl/2018-nhl-draft-lottery-faq-need-know/). What are the advantages of adding randomness into this ordering?
3. Near the end of [this video about playing around with the variables in a genetic algorithm](https://www.youtube.com/watch?v=nrKjSeoc7fc) the presenter connects the genetic algorithm to the purely random algorithm. Explain that connection.
4. Play around with [this genetic algorithm that designs racing cars](http://rednuht.org/genetic_cars_2/). Play around with the variables. How would you *deterministically* design a car for this game, and how do you think that car would do against a 50th generation car from this genetic algorithm?
5. Think back to the voting systems in Module 2. How could randomness be introduced into some of these voting systems in a way that would improve them? (There's no "correct" solution here; it's meant to be exploratory.)
