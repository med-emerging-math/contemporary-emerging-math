# contemporary-emerging-math

## Voting_methods.py

This contains an implementation of the 4 methods of voting we've studied. Here are the four main methods:

    plurality_winner()
    borda_winner()
    pairwise_comparison_winner()
    plurality_elimination_winner()

**input**: an `election` of the form `mathelec = { 'ABCD': 14, 'CBDA':10, 'DCBA':8, 'BDCA': 4, 'CDBA': 1}`.

**output**: a pair `('A', 14)` or possibly `('TIE', 14)`.

By default they only give the winner, but it's relatively easy to keep track of the ranking they output. See their `data` right before they `return` the winner; that contains a full ranking.

`plurality_elimination_winner()` is the only exception, as it is a recursive function, so it doesn't naturally keep track of the ranking. Although it should be easy enough to ask it to `print` the `loser` that it eliminates at each stage.

Note that ties are a bit annoying. Generally everything handles ties properly except in the case that `plurality_elimination_winner()` is deciding who to eliminate. In the case of a tie for fewest first place votes, it arbitrarily decided. In practice this shouldn't matter, but there are certainly datasets on which it might behave counterintuitively.
