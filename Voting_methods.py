mathelec = { 'ABCD': 14, 'CBDA':10, 'DCBA':8, 'BDCA': 4, 'CDBA': 1}

def candidates(election):
    """Give the names of the candidates as a list.
    Do this by adjoining all ballots, then extracting the unique letters.
    """
    return sorted(list(set([x for x in ''.join(election.keys()) ])))

def votes(candidate, election, rank):
    """Give the number of votes received by candidate of a given rank.
    -election is a dictionary with keys of the form 'ABCD'
    -candidate is a string 'A' or 'B' ... or 'D'.
    -rank is an integer. e.g. rank = 1 is for first place votes.
    """
    assert rank <= len(candidates(election))
    return sum([election[ballot] for ballot in election if ballot[rank - 1] == candidate])

#################
### Plurality ###
#################

def plurality_winner(election):
    """Give the winner using the plurality method.
    -data is a dictionary with keys of the form 'ABCD'
    """
    data = [(candidate, votes(candidate, election, 1)) for candidate in candidates(election)]
    return max(data, key=lambda pair:pair[1])

# plurality_winner(mathelec)
# ('A', 14)

#############
### Borda ###
#############

def borda_score(candidate, election):
    """Compute the Borda score of a candidate.
    Every first place vote is worth n points, second place = n-1 points, ..., nth place = 1 point.
    """
    n = len(candidates(election))
    score = 0
    for rank in range(1,n+1):
        # Give (n + 1 - rank) points for each ballot of a given rank
        points = n + 1 - rank
        # Count the number of 'rank'-place ballots
        score += points * votes(candidate, election, rank)
    return score

def borda_winner(election):
    """Give the Borda winner of the election."""
    data = [(candidate, borda_score(candidate, election)) for candidate in candidates(election)]
    return max(data, key=lambda pair:pair[1])

# borda_winner(mathelec)
# ('B', 106)

################
### Pairwise ###
################

def h2h_ballot_winner(candidate1, candidate2, ballot):
    """Determine the winner on a single ballot."""
    # Make sure both candidates are on the ballot
    if (not candidate1 in ballot) and (not candidate2 in ballot):
        return 'TIE'
    if (not candidate1 in ballot):
        return candidate2
    if (not candidate2 in ballot):
        return candidate1
    # Give the winner
    if ballot.index(candidate1) < ballot.index(candidate2):
        return candidate1
    else:
        return candidate2

def pairwise_score(candidate, election):
    """Compute the pairwise score of a candidate.
    1 pt if A > B on a majority of ballots. 0.5 pts if it is a tie.
    """
    n = len(candidates(election))
    score = 0
    for challenger in candidates(election):
        if challenger == candidate:
            pass
        else:
            score_can = sum([1 for ballot in election if h2h_ballot_winner(candidate, challenger, ballot) == candidate])
            score_cha = sum([1 for ballot in election if h2h_ballot_winner(candidate, challenger, ballot) == challenger])
            if score_can == score_cha:
                score += 0.5
            elif score_can > score_cha:
                score += 1
    return score

def pairwise_comparison_winner(election):
    """Give the winner of the election using pairwise comparisons."""
    data = [(candidate, pairwise_score(candidate, election)) for candidate in candidates(election)]
    return max(data, key=lambda pair:pair[1])

# pairwise_comparison_winner(mathelec)
# ('C', 3)

##################################
### Plurality-with-elimination ###
##################################

#[To do]
