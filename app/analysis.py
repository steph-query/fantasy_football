from scipy.stats import binom
import pandas as pd

##This function gives the expected loss by waiting a round. dframe should be that data
##that is being passed through; it looks like it will be the variable "players" that is 
##defined in draft_room.py. playpos should be a character string specifying the position.
##dround is the current round of the draft. playpos and dround are the same in function 2.


# loop over a list of positions to yield a dictionary
#pass dround as pick.round_number


def losscalc(dframe, playpos, dround):
    columns = ["Round", "QB", "WR/TE", "RB", "Other"]
    matrix_csv = [
    [1,0.39,0.16,0.45,0],
    [2,0.3,0.45,0.25,0],
    [3,0.15,0.75,0.1,0],
    [4,0.42,0.15,0.43,0],
    [5,0.28,0.36,0.36,0],
    [6,0.17,0.72,0.11,0],
    [7,0.11,0.74,0.15,0],
    [8,0.18,0.65,0.17,0],
    [90.1,0,0.88,0.02],
    [1,0.27,0.02,0.71,0],
    [1,0.22,0.01,0.75,0.02],
    [11,0.23,0,0.56,0.21],
    [11,0.26,0.01,0.52,0.21],
    [1,0.31,0.03,0.58,0.08],
    [16,0.15,0.04,0.35,0.46],
    [1,0,0,0,1]
    ]


    weightmatrix = pd.DataFrame(matrix_csv, columns=columns)

    ##Subsetting expected points of all players of the specified position
    points = dframe[dframe.position == playpos].points
    points = points.map(lambda x: x/16)
    #substitute dframe with players (convert to dataframe in draft_room.py) swap filter for .where



    ##Getting the probability that a player of that position would be picked this round and next round
    #change name of colum nin weightmatrix to avoid keyword conflict, change .filter to .where
    thisround = weightmatrix[playpos].ix[dround]
    nextround = weightmatrix[playpos].ix[dround + 1]
    
    ##Setting picks by round (we can define a variable for this beforehand instead of this method)
    if dround % 2 == 0:
        m = 8
        n = 4
    else:
        m = 10
        n = 5
    
    ##Calculating differences
    #make sure you can subtract (properly indexed df elements)
    diff = []
    for i in range(m+1):
        diff.append(points.iloc[0]-points.iloc[i])
    
    ##Calculating weighting system using binomial probability
    if dround % 2 == 0:   
        weights = []
        for i in range(m+1):
            prob = 0
            for l in range(max(0,(i-6)),(min(5,i) + 1)):
                prob = prob + binom.pmf(l,n,thisround) * binom.pmf((i - l),(m - n),nextround)
            weights.append(prob)
    else:
        weights = []
        for i in range(m+1):
            prob = 0
            for l in range(max(0,i-5),min(5,i)+1):
                prob = prob + binom.pmf(l,n,thisround)*binom.pmf(i-l,m-n,nextround)
            weights.append(prob)
    
    ##Calculating expected loss
    loss = []
    while len(loss) < len(diff):
    	loss.append(0)
    for i in range(len(diff)):
    	loss[i] = diff[i] * weights[i]
    loss = sum(loss)
    return loss

##This function creates a vector of probabilities that the next few players of that position
##will be available by next round

def nextround(playpos, dround):
    columns = ["Round", "QB", "WR/TE", "RB", "Other"]
    matrix_csv = [
    [1,0.39,0.16,0.45,0],
    [2,0.3,0.45,0.25,0],
    [3,0.15,0.75,0.1,0],
    [4,0.42,0.15,0.43,0],
    [5,0.28,0.36,0.36,0],
    [6,0.17,0.72,0.11,0],
    [7,0.11,0.74,0.15,0],
    [8,0.18,0.65,0.17,0],
    [90.1,0,0.88,0.02],
    [1,0.27,0.02,0.71,0],
    [1,0.22,0.01,0.75,0.02],
    [11,0.23,0,0.56,0.21],
    [11,0.26,0.01,0.52,0.21],
    [1,0.31,0.03,0.58,0.08],
    [16,0.15,0.04,0.35,0.46],
    [1,0,0,0,1]
    ]


    weightmatrix = pd.DataFrame(matrix_csv, columns=columns)
    
    thisround = weightmatrix[playpos].ix[dround]
    nextround = weightmatrix[playpos].ix[dround+1]
    
    ##Setting picks by round
    if dround % 2 == 0:
        m = 8
        n = 4
    else:
        m = 10
        n = 5
    
    ##Calculating weighting system using binomial probability
    if dround % 2 == 0: 
        pickprob = {}
        for i in range(m+1):
            prob = 0
            for l in range(max(0,i-6),min(5,i)+1):
                prob = prob + binom.pmf(l,n,thisround)*binom.pmf(i-l,m-n,nextround)
            pickprob[i] = prob
    else:
        pickprob = {}
        for i in range(m+1):
            prob = 0
            for l in range(max(0,i-5),min(5,i)+1):
                prob = prob + binom.pmf(l,n,thisround)*binom.pmf(i-l,m-n,nextround)
            pickprob[i] = prob
        ##Setting probabilities to be cumulative, i.e. now it will describe the probability that
        ##that player will still be available by next round
    for i in range(1,len(pickprob)):
    	pickprob[i] = pickprob[i-1] + pickprob[i]
    return pickprob









